# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2022-12-11
# @Author  : white
# @FileName: 某加速.py
# @Software: PyCharm
# **************************************
import requests
import execjs
import io
import re
import ddddocr

username = '12356520'
pwd = 'sdfasd'
_csrfToken = str()
headers = {
    "Host": "www.15yunmall.com",
    "Referer": "http://www.15yunmall.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.37"
}

# 提供cookie持久化，就是在后端有cookie返回时自动添加到配置中，后续使用session的请求都会携带cookie
session = requests.Session()

def get_pwd():
    '''获取加密码'''
    return execjs.compile(open('./pwd.js', encoding='utf-8').read()).call('white', pwd)

def get_code():
    '''获取验证码，并进行验证'''
    url = 'http://www.15yunmall.com/very/code.html'
    res = session.get(url, headers=headers).content
    with open('11.png', 'wb') as f:
        f.write(res)
    # 保存为内存对象，加快读取速度
    tu = io.BytesIO(res)
    # 调用识别模块
    ocr = ddddocr.DdddOcr()
    img = tu.getvalue()
    # 文字识别模块
    string = ocr.classification(img)
    print('识别文本：', string)
    # 运算
    if '+' in string:
        try:
            a = int(string[0])
            b = int(string[2])
            A = a + b
            print('运算结果：', A)
            # 再次return确保最外面的调用能接受到结果
            return A
        except:
            print('识别出错，重试！')
            return get_code()
    elif string[0] == string[1]:
        try:
            a = int(string[0])
            b = int(string[2])
            A = a - b
            print('运算结果：', A)
            return A
        except:
            print('识别出错，重试！')
            return get_code()
    else:
        try:
            a = int(string[0])
            b = int(string[1])
            A = a - b
            print('运算结果：', A)
            return A
        except:
            print('识别出错，重试！')
            return get_code()

def get_Token_cookie():
    '''获取_csrfToken与cookie'''
    global _csrfToken
    url = 'http://www.15yunmall.com/pc/login/index'
    res = session.get(url, headers=headers)
    print(res.request.headers)
    _csrfToken = re.search('value="([0-9a-z]+)"\sname="_csrfToken"', res.text).group(1)

def sign():
    '''登录操作'''
    # 先请求token以及cookie，请求验证码时，要带上这两者，后端会将验证码与token关联起来
    get_Token_cookie()
    url = 'http://www.15yunmall.com/pc/login/check'
    data = {
        "u[loginType]": "name", # phone代表手机号， name代表用户名
        "u[phone]": username,
        "u[password]": get_pwd(),
        "u[veryCode]": get_code(),
        "u[token]": "",
        "_csrfToken": _csrfToken
    }
    res = session.post(url, headers=headers, data=data)
    # print(res.request.headers)
    status_code = {
        '31': '恭喜，登陆成功。',
        '32': '登陆失败。',
        '33': '用户名或密码错误。',
        '35': '该用户已被管理员锁定。',
        '311': '该账号已绑定设备，请在绑定的设备登陆。',
        '20001': '验证码填写错误!'
    }
    # 返回的字符串中被添加了特殊字符，导致不能直接比较
    # \xef\xbb\xbf这个是我通过将返回的字符进行二进制编码后得到的
    n = b'\xef\xbb\xbf'.decode('utf-8')
    num = res.text.replace(n, '')
    for k, v in status_code.items():
        if k == num:
            print('响应结果：', v)

    # print(num)

sign()
