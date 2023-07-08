# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-07-05
# @Author  : white
# @FileName: google_translate.py
# @Software: PyCharm
# **************************************
import execjs
import requests
from urllib.parse import quote

url = "https://translate.googleapis.com/translate_a/t"
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

params = {
    "client": "webapp",
    "sl": "auto",
    "tl": "en",
    "tc": 0,
    "tk": None,
}
data = {
    "q": ["你应该是一场梦，我应该是一阵风。"]
}

tk = execjs.compile(open("google.js", encoding="utf-8").read()).call("white", "".join(data["q"]))
params["tk"] = tk
data = "q=" + "&q=".join(data["q"])
data = quote(data).replace("%3D", "=").replace("%26", "&")
res = requests.post(url=url, headers=headers, data=data, params=params)
print(res.text)
