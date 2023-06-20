# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-06-16
# @Author  : white
# @FileName: bing.py
# @Software: PyCharm
# **************************************
import requests
'''
加密参数请求接口：
https://edge.microsoft.com/translate/auth

翻译的接口：
https://api-edge.cognitive.microsofttranslator.com/translate?from=en&to=zh-CHS&api-version=3.0&includeSentenceLength=true
'''

def get_encryption():
    url = "https://edge.microsoft.com/translate/auth"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5,zh-TW;q=0.4",
        "Cache-Control": "no-cache",
        "Origin": "https://www.grepper.com",
        "Pragma": "no-cache",
        "Referer": "https://www.grepper.com/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Mesh-Client-Arch": "x86_64",
        "Sec-Mesh-Client-Edge-Channel": "stable",
        "Sec-Mesh-Client-Edge-Version": "114.0.1823.55",
        "Sec-Mesh-Client-Os": "Windows",
        "Sec-Mesh-Client-Os-Version": "10.0.17763",
        "Sec-Mesh-Client-Webview": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.55"
    }
    res = requests.get(url=url, headers=headers)
    return res.text

def translate():
    url = "https://api-edge.cognitive.microsofttranslator.com/translate"
    params = {
        "from": "en",
        "to": "zh-CHS",
        "api-version": "3.0",
        "includeSentenceLength": "true"
    }
    data = [
        {
            "Text": "I would be content with only two strokes of luck in my life: once to meet you, and once to walk with you forever. I never told you how lucky I am to have met you."
        },
    ]
    bearer = get_encryption()
    headers = {
        "Accept": "*/*",
        # "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5,zh-TW;q=0.4",
        "Authorization": f"Bearer {bearer}",
        "Cache-Control": "no-cache",
        # "Content-Length": "1494",
        "Content-Type": "application/json",
        "Origin": "https://www.grepper.com",
        "Pragma": "no-cache",
        "Referer": "https://www.grepper.com/",
        "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Microsoft Edge\";v=\"114\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.55"
    }
    res = requests.post(url=url, headers=headers, params=params, json=data)
    print(res.text)

if __name__ == '__main__':
    translate()