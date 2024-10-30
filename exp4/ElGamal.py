import random
from sympy import isprime
import hashlib

def quick_pow(m: int, e: int, n: int) -> int:
    """模运算下的快速幂
    Args:
        m (int): _description_  底数
        e (int): _description_  指数
        n (int): _description_  模数
    Returns:
        int: _description_ 计算结果
    """
    ans = 1
    while e:
        if e & 1:  # 是奇数
            ans = ans * m % n
        m = (m * m) % n  # 底数平方
        e >>= 1  # 指数右移 /2
    return ans

def MR_isprime(num: int) -> bool:
    """
    利用Miller-Rabin算法实现素数检测
    Params:
        num (int): 待检测的数
    Returns:
        bool: 是否为素数
    """
    # 节约部分时间
    if num % 2 == 0 and num != 2:
        return False
    num1 = num - 1
    powof2 = 2
    k = 1
    while True:
        if num1 % powof2 == 0:
            q = num1//powof2
            if q % 2 == 1:
                break
        if powof2 > num1:
            return False
        powof2 *= 2
        k += 1
    a = random.randint(1+1, num1-1)
    if quick_pow(a, q, num) in (1, num-1):     
        return True
    for j in range(1, k, 1):
        if  quick_pow(a, (2**j)*q, num) == num-1:
            return True
    return False

def get_prime_p(min_num:int=2*15, max_num:int=2**16-1)->int:
    """_summary_
    产生大素数p
    Args:
        min_num (int, optional): _description_. Defaults to 2**128.
        max_num (int, optional): _description_. Defaults to 2**129-1.

    Raises:
        Exception: _description_

    Returns:
        int: _description_ 返回的p 和 g
    """
    p = random.randint(min_num, max_num)
    while True:
        if MR_isprime(p):
            break
        p += 1
    if not isprime(p):
        raise Exception('p is not prime')
    return p

def check_arrequal(std, real):
    if len(std) != len(real):
        raise Exception('长度不一致')
    for i in range(len(std)):
        if std[i] != real[i]:
            return False
    return True
    

def find_primitive_root_g(p:int):
    if not MR_isprime(p):
        raise Exception('p is not prime')
    SEP = 20
    rootls = []
    std = list(range(1,p))
    for i in range(2, p, p//SEP):
        quick_pow_res = [quick_pow(i, j, p) for j in range(1, p)]
        quick_pow_res.sort()
        if check_arrequal(std, quick_pow_res):
            rootls.append(i)
    if len(rootls) == 0:
        raise Exception('no primitive root found')
    return random.choice(rootls)

def get_xy(p:int, g:int)->tuple[list[int], int]:
    """_summary_
    产生x和y，返回公钥私钥
    Args:
        p (int): _description_
        g (int): _description_

    Returns:
        tuple[list[int], int]: _description_ 公钥和私钥
    """
    x = random.randint(1+1, p-1-1)
    y = quick_pow(g, x, p)
    return [p, g, y], x


def gcd_isprime(a: int, b: int) -> bool:
    """
    欧几里得算法：判断两个数是否互素
    Args:
        a (iny): _description_ 数字1
        b (int): _description_ 数字2
    Returns:
        bool: _description_ 
    """
    while a != 0 and b != 0:
        a, b = b % a, a
    if a == 0:
        return b == 1
    else:
        return a == 1
    
def get_k(p:int)->int:
    k = random.randint(1+1, p-1-1)
    while True:
        if gcd_isprime(k, p-1):
            return k
        k += 1
        if k >= p-2:
            k = random.randint(1+1, p-1-1)
            
def get_sha256_hash(input_string):
    # 创建一个SHA256哈希对象
    sha256 = hashlib.sha256()
    # 更新哈希对象以包含要散列的字符串的字节
    sha256.update(input_string.encode('utf-8'))
    # 返回十六进制的哈希值
    return sha256.hexdigest()

def extend_gcd(a: int, b: int) -> tuple:
    """
    扩展欧几里得算法
    Args:
        a (int): _description_
        b (int): _description_
    Returns:
        tuple: _description_
    """
    if a == 0:
        return (b, 0, 1)

    gcd, x1, y1 = extend_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return (gcd, x, y)

def get_d(e: int, fi: int) -> int:
    """
    拓展欧几里得算法找到e在mod(fi(n))下的逆元
    Args:
        e  (int): _description_ 
        fi (int): _description_ 模数
    Returns:
        int: _description_ e在模fi下的乘法逆元
    """
    if not gcd_isprime(e, fi):
        raise Exception('e and fi(n) is not prime')
    gcd, x, _ = extend_gcd(e, fi)
    return x % fi

def sig(m:str, k:int, p:int, g:int, x:int)->tuple:
    m_hash = get_sha256_hash(m)
    r = quick_pow(g, k, p)
    kni = get_d(k, p-1)
    s = (((kni % (p-1))*(int(m_hash, 16) % (p-1)) % (p-1)) - 
         ((kni % (p-1))*(x*r             % (p-1)) % (p-1))) % (p-1)
    return r, s

def verify(m, r, s, p, y, g):
    m_hash = get_sha256_hash(m)
    res1 = (quick_pow(y, r, p)*quick_pow(r, s, p)) % p
    res2 = quick_pow(g, int(m_hash, 16), p)
    return res1 == res2

def genInfo(s:str)->str:
    l = 50
    res = '*'*((l-len(s))//2) + s + '*'*((l-len(s))//2)
    res = res + '*' if len(res)!=l else res
    return res


if __name__ == '__main__':
    ##密钥生成
    print(genInfo('sk & pk generation'))
    p = get_prime_p()
    g =find_primitive_root_g(p)
    pk, sk = get_xy(p, g)
    print("公钥pk:\np:{}, g:{}, y:{}".format(*pk))
    print("私钥sk:\nx:{}".format(sk))
    p, g, y = pk
    x = sk
     
    ##所签名的消息
    m = '220111011'
    mwrong = '220111012'
    
    ##第一次签名
    print(genInfo('signature 1'))
    print(f"待签名消息:{m}")
    k = get_k(p)
    print(f"随机数k:{k}")
    r, s = sig(m, k, p, g, x)
    print(f"签名信息:r:{r}, s:{s}")
    print(genInfo('signature verification 1'))
    print(f"待验证消息:{m}")    
    print("是否通过签名验证:", verify(m, r, s, p, y, g))
    
    ##第2次签名
    print(genInfo('signature 2'))
    print(f"待签名消息:{m}")
    k = get_k(p)
    print(f"随机数k:{k}")
    r, s = sig(m, k, p, g, x)
    print(f"签名信息:r:{r}, s:{s}")
    print(genInfo('signature verification 2'))
    print(f"待验证消息:{m}")    
    print("是否通过签名验证:", verify(m, r, s, p, y, g))
    
    ##模拟消息m在传送过程中被篡改的情况
    ##第3次签名
    print(genInfo('signature 3'))
    print(f"待签名消息:{m}")
    k = get_k(p)
    print(f"随机数k:{k}")
    r, s = sig(m, k, p, g, x)
    print(f"签名信息:r:{r}, s:{s}")
    print(genInfo('signature verification 3'))
    print(f"待验证消息(被纂改后的错误m):{mwrong}")    
    print("是否通过签名验证:", verify(mwrong, r, s, p, y, g))
    
    
    