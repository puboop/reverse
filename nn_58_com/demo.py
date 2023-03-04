import requests
from lxml import etree
import re
import base64
from fontTools.ttLib import TTFont

def get_font(data):
    a = re.search("utf-8;base64,(.*?)'", data).group(1)
    file_name = "white.xml"
    with open(file_name, mode="wb") as f:
        base64_str = base64.b64decode(a)
        f.write(base64_str)
    font = TTFont(file_name)
    font_map = dict()
    for _k, _v in font.getReverseGlyphMap().items():
        if "uni" in _k:
            font_map[_v - 1] = f"&#x{_k[3:]};".replace("00", "").lower()
    print(font_map)
    return font_map

def get_data():
    url = "https://nn.58.com/ershouche/"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,it;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "f=n; commontopbar_ipcity=nn%7C%E5%8D%97%E5%AE%81%7C0; userid360_xml=2223456397D75F7CA7DEF0A6DC8A00E3; time_create=1680537725422; fzq_h=c0a85b121842469f755ea1b2ce3f538d_1677944324089_7bbec4b642ac4e1391c9f8a894d329cd_47901724501614866947866381702450081086; sessionid=b829c0a2-65c2-48fe-b6a2-182916ee1f49; id58=pQ7fMGQDZgSh/osnH2V+Ag==; 58tj_uuid=decafe04-a84f-4f88-a386-c2aaac4f7140; new_uv=1; utm_source=; spm=; init_refer=; wmda_uuid=c59902e88a37e5b74039d3e24099c01b; wmda_new_uuid=1; wmda_session_id_1732038237441=1677944324708-34fdd8bd-c4fb-c83a; 58home=nn; als=0; new_session=0; f=n; wmda_visited_projects=%3B1732038237441%3B11187958619315; xxzl_sid=\"5TCm5Z-Nam-LeZ-SD4-1bYCqA0yK\"; fzq_js_usdt_infodetail_car=2d53db353b80bb60753e571d4803488d_1677944847754_7; ppStore_fingerprint=44C932AFA11211258B0B048A71C2850C6AF6A94B6EF6F272%EF%BC%BF1677944848039; xxzl_token=\"kB3AEdPBEgzL15iWKwh+5ZGzafT+VPO0PoT/wsLtHXzXJXBKC65777s0GENHIgD1in35brBb//eSODvMgkQULA==\"; city=nn; commontopbar_ipcity=nn%7C%E5%8D%97%E5%AE%81%7C0; xxzl_cid=1138045b7d624ed1a24ffd33411a308a; wmda_session_id_11187958619315=1677947133939-2ae9f6ed-c569-5ebb; fzq_js_usdt_infolist_car=c12a4adef5a12b0ef8c8b864ea042299_1677947139333_9; xxzl_deviceid=sddC1lW9lMK0YIyGt2JPqS4gY%2FAvoQP7ET6vJ3XzRfNgI%2BIB3NVdj6pwoG5oTXDB",
        "Host": "nn.58.com",
        "Pragma": "no-cache",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.get(url=url, headers=headers).text
    map_font = get_font(res)
    for __k, __v in map_font.items():
        res = res.replace(__v, str(__k))

    html = etree.HTML(res)
    rooms = html.xpath("//ul/li")
    for _i in rooms:
        title = _i.xpath('string(.//div[@class="info--desc"])').strip().replace("\n", "").replace("\t", "").replace(" ",
                                                                                                                    "")
        price = _i.xpath('string(.//div[@class="info--price"])').strip().replace(" ", "").replace("\n", "")
        if title and price:
            print({"title": title, "price": price})

get_data()
