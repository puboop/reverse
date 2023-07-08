# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-07-05
# @Author  : white
# @FileName: google_translate.py
# @Software: PyCharm
# **************************************
import requests
from urllib.parse import quote
from typing import Union

# python 按位异或 按位或 https://blog.csdn.net/qq_46614154/article/details/105537609
# js 按位异或 按位或 https://blog.csdn.net/romeo12334/article/details/81234991

class GoogleEncryption:
    def __init__(self, Vp="469040.3323378158"):
        self.Vp = Vp

    def _c_int(self, x, nbits=32):
        return (x & ((1 << (nbits - 1)) - 1)) - (x & (1 << (nbits - 1)))

    def _c_uint(self, x, nbits=32):
        return x & ((1 << nbits) - 1)

    def _zo(self, data):
        b = list()
        for d in range(len(data)):
            e = ord(data[d])
            if 128 > e:
                b.append(e)
            else:
                if 2048 > e:
                    b.append(e >> 6 | 192)
                else:
                    if 55296 == (e & 64512) and d + 1 < len(data) and 56320 == (len(data) + 1) & 64512:
                        d += 1
                        e = 65536 + ((e & 1023) << 10) + (ord(data[d]) & 1023)
                        b.append(e >> 18 | 240)
                        b.append(e >> 12 & 63 | 128)
                    else:
                        b.append(e >> 12 | 224)
                        b.append(e >> 6 & 63 | 128)
                    b.append(e & 63 | 128)
        return b

    def _Up(self, a, b):
        for c in range(0, len(b) - 2, 3):
            d = b[c + 2]
            d = (ord(d[0]) - 87) if "a" <= d else int(d)
            wa = self._c_uint(a)
            d = wa >> d if "+" == b[c + 1] else wa << d
            a = (a + d & 4294967295) if "+" == b[c] else a ^ d
        return self._c_int(a)

    def Wp(self, data: str):
        b = self.Vp.split(".")
        c = int(b[0])
        a = self._zo(data)
        d = c
        for e in range(len(a)):
            d += a[e]
            d = self._Up(d, "+-a^+6")
        d = self._Up(d, "+-3^+b+-f")
        d ^= self._c_int(int(b[1]))
        if 0 > d:
            d = (d & 2147483647) + 2147483648
        b = int(d % 1E6)
        return f"{b}.{b ^ c}"

class GoogleTranslate(GoogleEncryption):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    params = {
        "client": "webapp",
        "sl": "auto",
        "tl": "en",
        "hl": "en",
        "tc": 0,
        "tk": None,
    }
    data = {
        "q": list(),
    }
    url = "https://translate.googleapis.com/translate_a/t"

    def __init__(self, Vp=None):
        if Vp is not None:
            super(GoogleTranslate, self).__init__(Vp=Vp)
        else:
            super(GoogleTranslate, self).__init__()

    def translate(self, text: Union[list, str]):
        self.data["q"].clear()
        if isinstance(text, list):
            self.data["q"] = text
        else:
            self.data["q"].append(text)
        self.params["tk"] = self.Wp("".join(self.data["q"]))
        data = "q=" + "&q=".join(self.data["q"])
        data = quote(data).replace("%3D", "=").replace("%26", "&")
        res = requests.post(url=self.url, headers=self.headers, data=data, params=self.params)
        try:
            for i in res.json():
                print(i[0])
        except Exception as e:
            print(res.text)

if __name__ == '__main__':
    g = GoogleTranslate()
    g.translate(["哪里有人会喜欢孤独，不过是不喜欢失望。", "我只愿面朝大海，春暖花开。"])
    g.translate("你应该是一场梦，我应该是一阵风。")
