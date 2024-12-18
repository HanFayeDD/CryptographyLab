import random
from sympy import isprime
import time
from concurrent import futures


def process_string(filename: str=None, textcontent: str=None) -> tuple[str, str]:
    """
    采用方法2进行处理，两个字符拼接成一共有6位的十进制数
    不足用000补齐
    可以输入保存密文的文件名，也可以直接输入明文字符串
    Args:
        filename (str):明文文件名字
        textcontent (str): 明文字符串
    Returns:
        tuple(str, str): 返回的ASCII码字符串(已经补齐)，文件内容
    """
    if filename is not None:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
    elif textcontent is not None:
        content = textcontent
    else:
        raise ValueError()
    fillcode = '000'
    fillflag = False if len(content) % 2 == 0 else True
    res = ''
    for ele in content:
        t = str(ord(ele))
        if len(t) == 2:
            t = '0'+t
        res += t
    if fillflag:
        print(f'内容长度为{len(content)}奇数，用000进行补全')
        res += fillcode
    return res, content

def ascciitostr(s:str)->str:
    """
    将解密后的的明文asccii串转为明文字符串
    Args:
        s (str): _description_ 解密后的的明文asccii串
    Raises:
        Exception: _description_ 解密后的的明文asccii串不是3的倍数
    Returns:
        str: _description_ 明文字符串
    """
    if len(s) % 3 != 0:
        raise Exception('明文ascii码不是3的倍数')
    r = ''
    for i in range(0, len(s), 3):
        r += chr(int(s[i:i+3]))
    return r


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


def getp_q(min_num: int = 1000, max_num: int = 10000) -> tuple:
    """
    获取p和q
    Args:
        min_num (int): 范围最小值
        max_num (int): 范围最大值
    Returns:
        tuple: (p, q)
    """
    p = 0
    q = 0
    while abs(p-q) < int((max_num-min_num)//5):
        p = random.randint(min_num, max_num)
        q = random.randint(min_num, max_num)
    print(f'init p:{p}, init q:{q}')
    # print('*'*20+  'info' + '*'*20)
    while not MR_isprime(p):
        p += 1
    while not MR_isprime(q):
        q += 1
    # print('*'*20+  'find p and q' + '*'*20)
    print(f'last p:{p}, last q:{q}')
    if not (isprime(p) and isprime(q)):
        raise Exception('p or q at least one is not prime')
    return (p, q)


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


def get_e(p: int, q: int) -> int:
    """
    求出fi(n)并利用欧几里得算法找到随机整数e
    Args:
        p (int): _description_
        q (int): _description_

    Returns:
        int: _description_
    """
    fi: int = (p-1)*(q-1)
    lowerbound = int((fi-1)//5)
    upperbound = fi-1
    e = random.randint(lowerbound, upperbound)
    while not gcd_isprime(e, fi):
        e = random.randint(lowerbound, upperbound)
    return e


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
    TODO:拓展欧几里得算法
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

def get_Params(min_boundary:int =2**128, max_boundary:int=2**129-1) -> tuple:
    p, q = getp_q(min_num=min_boundary, max_num=max_boundary)
    e = get_e(p, q)
    d = get_d(e, (p-1)*(q-1))
    lenmod = len(str(p*q))
    print(f'密文中一个分组的长度:{lenmod}')
    print('*'*10+' info begin '+'*'*10)
    print(f'p:{p}\nq:{q}\nn:{p*q}\ne:{e}\nd:{d}\nφ(n):{(p-1)*(q-1)}')
    print('*'*10+' info end '+'*'*10)
    return p, q, e, d, lenmod

         
def encodethread(content: str) -> str:
    """"
    Args:
        content (str): _description_ 传入的文本内容的ASCII码字符
 
    Returns:
        str: _description_
    """
    miwen = ''
    with futures.ThreadPoolExecutor() as executor:
        to_do = []
        results = [None] * (len(content) // 6)  # 创建一个列表来存储结果

        for index in range(0, len(content), 6):
            buf = str(content[index:index+6])
            future = executor.submit(quick_pow, int(buf), e, p*q)
            to_do.append((index // 6, future))  # 记录提交的顺序和任务

        # 等待所有任务完成并按照提交顺序获取结果
        for idx, future in to_do:
            res = future.result()
            results[idx] = str(res).zfill(lenmod)

        # 按照提交顺序构建 miwen
        miwen = ''.join(results)
        return miwen
    
def encodeprocess(content: str) -> str:
    """"
    Args:
        content (str): _description_ 传入的文本内容的ASCII码字符
 
    Returns:
        str: _description_
    """
    miwen = ''
    with futures.ProcessPoolExecutor() as executor:
        to_do = []
        results = [None] * (len(content) // 6)  # 创建一个列表来存储结果

        for index in range(0, len(content), 6):
            buf = str(content[index:index+6])
            future = executor.submit(quick_pow, int(buf), e, p*q)
            to_do.append((index // 6, future))  # 记录提交的顺序和任务

        # 等待所有任务完成并按照提交顺序获取结果
        for idx, future in to_do:
            res = future.result()
            results[idx] = str(res).zfill(lenmod)

        # 按照提交顺序构建 miwen
        miwen = ''.join(results)
        return miwen

            
            
        
    

if __name__ == '__main__':
    c, content = process_string(filename="exp2/speed_test.txt")

    
    if len(c) % 6 != 0:
        raise Exception('C is not a multiple of 6')

    p, q, e, d, lenmod = get_Params()
    t1 = time.time()
    minthread = encodethread(c)
    t2 = time.time()
    print(f'并行加密时间(产生参数+加密，不包括IO读取):{t2-t1:.6f}秒')
    t1 = time.time()
    minprocess = encodeprocess(c)
    t2 = time.time()
    print(f'并行加密时间(产生参数+加密，不包括IO读取):{t2-t1:.6f}秒')
    
    
    
    t1 = time.time()
    miwen = ''
    for i in range(0, len(c), 6):
        buf = str(c[i:i+6])
        temp = str(quick_pow(int(buf), e, p*q))
        temp = temp.zfill(lenmod)
        miwen += temp
    t2 = time.time()
    print(f'加密时间(产生参数+加密，不包括IO读取):{t2-t1:.6f}秒')
    print("是否相等:", minthread==minprocess==miwen)

  