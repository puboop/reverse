# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-20
# @Author  : white
# @FileName: login.py
# @Software: PyCharm
# **************************************
username = "+86 "
username += "12345678900"
password = "white666"

def str_to_hex(string):
    '''
    string: 待转换的字符串
    '''
    _str = str()
    for i in string:
        # 获取字符的十进制
        int_num = ord(i)
        if i == "4" or i == "5" or i == "6" or i == "7":
            if int(i) % 2:
                int_num -= 5
            else:
                int_num -= 3
            # 获取字符的十六进制
            _str += hex(int_num)[2:]
            continue

        if int_num % 2:
            int_num += 3
        else:
            int_num += 5
        # 获取字符的十六进制
        _str += hex(int_num)[2:]
    return _str
print(str_to_hex(username))
