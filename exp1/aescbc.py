def char_to_binary(character) -> int:
    """_summary_
    将一个字符转为ASCII码
    Args:
        character (_type_): _description_ 一个字符

    Returns:
        int: _description_ 该字符对应的ASCII码
    """
    ascii_value = ord(character)
    return int(ascii_value)


def convertToINTArray(s: str) -> list:
    """
    将长度为16的字符串转为4*4的二维数组
    Args:
        s (str): _description_ 长度为16的字符串
    Returns:
        list: _description_ 4*4的二维数组，每个元素为对应字符的ASCII码(int)
    """
    init = []
    for i in range(4):
        t = []
        for j in range(4):
            t.append(char_to_binary(s[i+4*j]))
        init.append(t)
    return init


S = [[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
      0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
     [0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
      0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
     [0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
      0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
     [0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
      0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
     [0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
      0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
     [0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
      0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
     [0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
      0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
     [0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
      0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
     [0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
      0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
     [0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
      0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
     [0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
      0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
     [0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
      0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
     [0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
      0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
     [0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
      0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
     [0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
      0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
     [0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
      0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]]

S1 = [[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
      [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87,
          0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
      [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d,
          0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
      [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2,
          0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
      [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16,
          0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
      [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda,
          0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
      [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a,
          0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
      [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02,
          0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
      [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea,
          0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
      [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85,
          0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
      [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89,
          0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
      [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20,
          0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
      [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31,
          0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
      [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d,
          0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
      [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0,
          0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
      [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]]


def getL_R(ele: int):
    return (ele >> 4) & 0x0f, ele & 0x0f


def subBytes(ls: list):
    for i in range(4):
        for j in range(4):
            x, y = getL_R(ls[i][j])
            ls[i][j] = S[x][y]


def desubBytes(ls: list):
    for i in range(4):
        for j in range(4):
            x, y = getL_R(ls[i][j])
            ls[i][j] = S1[x][y]


def shiftRows(ls: list):
    for i in range(len(ls)):
        ls[i] = ls[i][i:] + ls[i][:i]


def deshiftRows(ls: list):
    for i in range(len(ls)):
        ls[i] = ls[i][-i:] + ls[i][:-i]


ColM = [[2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]]
deColM = [[0xe, 0xb, 0xd, 0x9],
          [0x9, 0xe, 0xb, 0xd],
          [0xd, 0x9, 0xe, 0xb],
          [0xb, 0xd, 0x9, 0xe]]


def GFMul(n: int, s: int) -> int:
    """
    Args:
        n (int): _description_ 矩阵中的值,只取低4位
        s (int): _description_

    Returns:
        int: _description_
    """
    n &= 0x0f
    s &= 0xff
    sum = s
    result = 0
    while n != 0:
        if n & 0x01:
            result = result ^ sum
        n = n >> 1
        sum = GFMul2(sum)
    return result


def GFMul2(s: int) -> int:
    """_summary_
    累计计算s*x, s*x^2等
    Args:
        s (int): _description_

    Returns:
        int: _description_
    """
    result = s << 1
    a7 = result & 0x00000100
    if a7 != 0:
        result = result & 0x000000ff
        result = result ^ 0x1b
    return result


def mixColumns(ls: list):
    result = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = ls[i][j]
    for i in range(4):
        for j in range(4):
            ls[i][j] = GFMul(ColM[i][0], result[0][j]) ^ GFMul(ColM[i][1], result[1][j]) ^ GFMul(
                ColM[i][2], result[2][j]) ^ GFMul(ColM[i][3], result[3][j])


def deMixColumns(ls: list):
    result = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = ls[i][j]
    for i in range(4):
        for j in range(4):
            ls[i][j] = GFMul(deColM[i][0], result[0][j]) ^ GFMul(deColM[i][1], result[1][j]) ^ GFMul(
                deColM[i][2], result[2][j]) ^ GFMul(deColM[i][3], result[3][j])


Rcon = [[0x01, 0x00, 0x00, 0x00],
        [0x02, 0x00, 0x00, 0x00],
        [0x04, 0x00, 0x00, 0x00],
        [0x08, 0x00, 0x00, 0x00],
        [0x10, 0x00, 0x00, 0x00],
        [0x20, 0x00, 0x00, 0x00],
        [0x40, 0x00, 0x00, 0x00],
        [0x80, 0x00, 0x00, 0x00],
        [0x1b, 0x00, 0x00, 0x00],
        [0x36, 0x00, 0x00, 0x00]]


def addRoundKey(ls: list, round: int) -> None:
    """_summary_

    Args:
        ls (list): _description_
        round (int): _description_ round循环round共有10轮，区间[1，10]。额外的一个算0
    """
    global W
    for j in range(4):
        for i in range(4):
            ls[i][j] = ls[i][j] ^ W[round*4+j][i]
            
def addIV(ls: list, IV: list) -> None:
    """_summary_

    Args:
        ls (list): _description_ 
        IV (list): _description_ IV4*4列表
    """
    for j in range(4):
        for i in range(4):
            ls[i][j] = ls[i][j] ^ IV[i][j]

def copyC2IV(C:list, IV: list) -> None:
    """_summary_
    存储上一轮的密文，用作下一轮的向量矩阵
    Args:
        C (list): _description_
        IV (list): _description_
    """
    for j in range(4):
        for i in range(4):
            IV[i][j] = C[i][j]


def T(numls: list, round: int) -> list:
    result = []
    numls = numls[1:] + numls[:1]
    for i in range(len(numls)):
        x, y = getL_R(numls[i])
        numls[i] = S[x][y]
    result = [x ^ y for x, y in zip(numls, Rcon[round])]
    return result


def extendKey(K_init: list) -> list:
    W = [0 for i in range(44)]
    NK = 4
    for i in range(44):
        if i < 4:
            W[i] = [K_init[0][i], K_init[1][i],
                    K_init[2][i], K_init[3][i]]
        else:
            temp = W[i-1].copy()
            if i % NK == 0:
                temp = T(temp, (i//NK)-1)
            W[i] = [x ^ y for x, y in zip(W[i-NK], temp)]
    return W


def printW() -> None:
    print('*'*5, '轮密钥', '*'*5)
    for i in range(len(W)):
        s = '0x'
        for ele in W[i]:
            s += hex(ele)[-2:].replace('x', '0')
        print(f'W[{i}]:{s}', end=' ')
        if (i+1) % 4 == 0:
            print('')


def convertArrayToStr(ls: list) -> str:
    """_summary_
    将4*4的int数组转换为16进制字符串
    Args:
        ls (list): _description_ 输入的4*4int数组

    Returns:
        str: _description_ 构造的字符串
    """
    s = ''
    for j in range(4):
        for i in range(4):
            print(hex(ls[i][j]), end=' ')
            s += (hex(ls[i][j])+' ')
    print('')
    return s


def convert1dTo2d(ls: list) -> list:
    """_summary_

    Args:
        ls (list): _description_ 将长度为16的int列表转为4*4的二维int列表

    Raises:
        ValueError: _description_ 

    Returns:
        list: _description_
    """
    if len(ls) != 16:
        raise ValueError('该密文分组长度不是16')
    result = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            result[i][j] = ls[i+4*j]
    return result

# %%


def aes(MINGWEN: str, KEY: str):
    """
    aes加密算法
    """
    if len(MINGWEN) == 0 or len(MINGWEN) % 16 != 0:
        print("明文字符必须是16的倍数,将采用重复补齐")
        originlen = len(MINGWEN)
        index = 0
        while len(MINGWEN) % 16 != 0:
            MINGWEN += MINGWEN[index]
            index += 1
            index %= originlen
        print("重复补齐后:", MINGWEN)
    if len(KEY) != 16:
        print("密钥长度必须为16")
        exit()
    if len(IVECTORSTR) != 16:
        raise ValueError('初始向量长度必须为16')
    global W
    IVARRAY:list[list[int]] =   convertToINTArray(IVECTORSTR)
    print(IVARRAY)
    W = extendKey(convertToINTArray(KEY))
    printW()
    print('*'*5, '加密后的ASCII码(16进制表示)', '*'*5)
    for i in range(0, len(MINGWEN), 16):
        parray = convertToINTArray(MINGWEN[i:i+16])
        addIV(parray, IVARRAY)
        addRoundKey(parray, 0)
        for i in range(1, 10, 1):
            subBytes(parray)
            shiftRows(parray)
            mixColumns(parray)
            addRoundKey(parray, i)
        subBytes(parray)
        shiftRows(parray)
        addRoundKey(parray, 10)
        copyC2IV(parray, IVARRAY)
        miwenstring = convertArrayToStr(parray)
        with open(FILENAME1, 'a') as f:
            f.write(miwenstring+'\n')
        f.close()


def deaes(ls: list):
    """_summary_
    对一组4*4的密文二维数组解密
    Args:
        ls (list): _description_  4*4的密文二维数组

    Returns:
        _type_: _description_  4*4的明文二维数组
    """
    addRoundKey(ls, 10)
    deshiftRows(ls)
    desubBytes(ls)
    for i in range(9, 0, -1):
        addRoundKey(ls, i)
        deMixColumns(ls)
        deshiftRows(ls)
        desubBytes(ls)
    addRoundKey(ls, 0)
    return ls


def pre_deaes():
    """_summary_
    读取文件中的密文并16位一组进行分组，调用deaes()函数解密
    Returns:
        _type_: _description_  返回解密后的字符串
    """
    if len(IVECTORSTR) != 16:
        raise ValueError('初始向量长度必须为16')
    with open(FILENAME2, 'r') as f:
        miwenstring = f.readlines()
    f.close()
    IVARRAY:list[list[int]] =   convertToINTArray(IVECTORSTR)
    res = ''  # 保存解密后的明文字符串
    print('*'*5, '解密后的ASCII码(16进制表示)', '*'*5)
    for ele in miwenstring:
        s = ele.split()
        s = [int(_, 16) for _ in s]
        carray = convert1dTo2d(s)
        mintarray = deaes(carray)
        addIV(mintarray, IVARRAY)
        res += generateMString(mintarray)
        convertArrayToStr(mintarray)
        copyC2IV(convert1dTo2d(s), IVARRAY)
    print('*'*5, '解密后的明文', '*'*5)
    print(res)
    with open(FILENAME2, 'a') as f:
        f.write(res+'\n')
    f.close()
    return res


def generateMString(ls: list) -> str:
    """_summary_
    将4*4的明文二维数组转换为字符串
    Args:
        ls (list): _description_ 解密后的4*4明文二维数组

    Raises:
        ValueError: _description_ 对不满足4*4的二维数组抛出异常

    Returns:
        str: _description_ 对应的明文字符串
    """
    if len(ls) != 4:
        raise ValueError()
    for i in range(4):
        if len(ls[i]) != 4:
            raise ValueError()
    res = ''
    for j in range(4):
        for i in range(4):
            res += chr(ls[i][j])
    return res


if __name__ == '__main__':
    W = []
    MINGWEN: str = 'itisaesclass1234itisaesclass1234'  # 默认值
    KEY: str = 'securitysecurity'  # 默认值
    FILENAME1: str = '密码.txt'
    FILENAME2: str = '密码.txt'
    IVECTORSTR: str = '1234567890abcdef'
    print('代码编写环境:Python 3.11.9 ')
    print('*'*20, 'AES(CBC模式)', '*'*20)

    # 加密过程
    MINGWEN = input('请输入明文字符串：(长度必须是16的倍数)\n')
    KEY = input('请输入密钥字符串：(128bits密钥)\n')
    IVECTORSTR = input('请输入初始向量字符串IV：(128bits向量)\n')
    FILENAME1 = input('请输入保存密文的文件名：\n')
    print('*'*15, '开始加密', '*'*15)
    aes(MINGWEN, KEY)
    print('*'*15, '加密完成', '*'*15)

    while True:
        choice = input('是否解密？(y(Y)/n(N))')
        if choice == 'n' or choice == 'N':
            exit()
        elif choice == 'y' or choice == 'Y':
            break
        else:
            print('输入有误，请重新输入')
            continue

    # 解密过程
    print('*'*15, '开始解密', '*'*15)
    FILENAME2 = input('请输入保存密文的文件名：\n')
    IVECTORSTR = input('请输入初始向量字符串IV：(128bits向量)\n')
    pre_deaes()
    print('*'*15, '解密完成', '*'*15)
