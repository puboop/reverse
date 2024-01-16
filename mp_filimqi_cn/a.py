# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2024-01-10
# @Author  : white
# @FileName: a.py
# @Software: PyCharm
# **************************************
import execjs
import time
import requests

with open("签名.js", encoding="utf-8") as f:
    js_file = f.read()
sign = execjs.compile(js_file)
time_stamp = int(time.time() * 1000)
sign_data = sign.call("white", str(time_stamp))
print(sign_data, time_stamp)

url = f"https://mp.filimqi.cn/api/resources?&t={time_stamp}"

headers = {
    "Host"              : "mp.filimqi.cn",
    "Connection"        : "keep-alive",
    "Content-Length"    : "60",
    "Pragma"            : "no-cache",
    "Cache-Control"     : "no-cache",
    "sec-ch-ua"         : "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile"  : "?0",
    "User-Agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "content-type"      : "application/x-www-form-urlencoded",
    "openid"            : "undefined",
    "token"             : sign_data[1],
    "request-token"     : sign_data[0],
    "sec-ch-ua-platform": "\"Windows\"",
    "Accept"            : "*/*",
    "Origin"            : "https://mp.filimqi.cn",
    "Sec-Fetch-Site"    : "same-origin",
    "Sec-Fetch-Mode"    : "cors",
    "Sec-Fetch-Dest"    : "empty",
    "Accept-Encoding"   : "gzip, deflate, br",
    "Accept-Language"   : "zh-CN,zh;q=0.9",
    # "Cookie"            : "XSRF-TOKEN=eyJpdiI6ImhZbFFHNjZBeWo5YmhLMm91ZFBTQ1E9PSIsInZhbHVlIjoiS3R4dW45OWJLQVV6ODBia1AxZUg2N1JSdlF4UjFjNEJzK1pEYkpVRGw4VVMxbnFCSmJIa2M3TUlEMmZmZDd5M3BoTEh2bEROaENaaW9QM0ZZQnhQT1BXNEcxQXpGSnlEMzdpRlMxWnhmYVZJanJuWTVTYnFIV2g2WVo3ZUxmNFgiLCJtYWMiOiI0MWJmZTZkMjhiZDg1NWFjM2ZiNWVkN2ZlNmJkOTcwNGY5Yzk0MDhmYWE2ZTljYjVlNzRhYTVjNjdiYjhkZmZiIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6Inc1L2E2VDBsVkgramVabU8xZGh1amc9PSIsInZhbHVlIjoib0ZvS1hqYWxNUVBaODk4bDFhQXprSWZTYVNFNjJQT05nQ0NKVis4eEU1Qmo5OE1KNiszUW4zR3lVKzQyQnZ6NjVsYjJIazFPTktZZmVEV0NtMUExUmRYZFgxOGtPQjE2VnMxN3FqY1FpeWRoam82d1NWYkZlNTJiRkIvcG81cE4iLCJtYWMiOiI0MTBkZWRiOWNmNWNjZjBlMDJjYWNlYWJkODRkNzIzZmUzNjQ0YTkxZDI2N2NiYzQ4MDY2NmQ3ZGRhMDk4MzVkIiwidGFnIjoiIn0%3D"
}

body = {
    "user_id": "807",
    "unionid": "ogHOR0Q9EKF-vkg6H_VNnyD1zMk8",
    "key"    : "",
    "page"   : "3"
}
res = requests.post(url=url, headers=headers, data=body)
print(res.json())
