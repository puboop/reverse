# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-01-16
# @Author  : white
# @FileName: login.py
# @Software: PyCharm
# **************************************
import requests
import execjs
url = "https://i.fkw.com/ajax/login_h.jsp?dogSrc=3"
account = "00000000000"
password = "123456"
params = {
    "cacct": account,
    "sacct": "",
    "pwd": execjs.compile(open("white.js", encoding="utf-8").read()).call("white", password),
    "autoLogin": "false",
    "staffLogin": "false",
    "bizType": "5",
    "dogId": "0",
    "fromsite": "false",
    "cmd": "loginCorpNews"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie": "_cliid=ebsWni5Fp0vRqdK0; loginReferer=https://cn.bing.com/; loginComeForm=fkjz; first_ta=3800; _ta=3800; _tp=-; _newUnion=0; _kw=0; _s_pro=i.fkw.com%2F; _c_pro=i.fkw.com%2F; reg_sid=0; ss_ta=3800; wxRegBiz=none; _faiHeDistictId=1bae64f5a2b2f130; _vid_url=https%3A%2F%2Fi.fkw.com%2F%3F_ta%3D3800",
    "Host": "i.fkw.com",
    "Origin": "https://i.fkw.com",
    "Referer": "https://i.fkw.com/?_ta=3800",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}
res = requests.post(url=url, headers=headers, data=params)
print(res.text)
