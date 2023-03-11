import execjs
import requests

phone = "13500000000"
def login():
    url = "https://h5three.changanford.cn/jump2023-api/h5/game/user/login-smscode"
    encrypt_data = execjs.compile(open("encrypt.js", encoding="u8").read()).call("white", phone)
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "cache-control": "no-cache",
        "content-length": "120",
        "content-type": "application/json",
        "origin": "https://evossys.changanford.cn",
        "pragma": "no-cache",
        "referer": "https://evossys.changanford.cn/",
        "salt-token": encrypt_data[0],
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.post(url=url, headers=headers, data=encrypt_data[1]).text
    print(res)

login()
