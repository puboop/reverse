# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-20
# @Author  : white
# @FileName: login.py
# @Software: PyCharm
# **************************************
import time
import requests
import base64
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
from Crypto.PublicKey import RSA
username = "16500000000"
password = "000"
def get_key():
    url = "https://passport.bilibili.com/x/passport-login/web/key?_=" + str(int(time.time() * 1000))
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "cache-control": "no-cache",
        "origin": "https://www.bilibili.com",
        "pragma": "no-cache",
        "referer": "https://www.bilibili.com/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers)
    return res.json()

def encrypt_password(public_key, string):
    '''
    public_key: 为加密的key；格式为 -----BEGIN PUBLIC KEY-----\nMAIN_KEY\n-----END PUBLIC KEY-----
    string: 为待加密的字符串
    '''
    rsakey = RSA.importKey(public_key)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(string).encode()))
    return cipher_text.decode()

def login():
    DATA = get_key()
    _public_key = DATA["data"]["key"]
    _hash = DATA["data"]["hash"]
    url = "https://passport.bilibili.com/x/passport-login/web/login"
    params = {
        "source": "main-fe-header",
        "username": username,
        "password": encrypt_password(_public_key, _hash + password),
        "validate": "待定",
        "token": "待定",
        "seccode": "待定|jordan",
        "challenge": "待定"
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "cache-control": "no-cache",
        "content-length": "410",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://www.bilibili.com",
        "pragma": "no-cache",
        "referer": "https://www.bilibili.com/",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.post(url=url, headers=headers, data=params)
    print(res.text)

login()
