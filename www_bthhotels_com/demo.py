# **************************************
# --*-- coding: utf-8 --*--
# @Time    : 2023-02-03
# @Author  : white
# @FileName: demo.py
# @Software: PyCharm
# **************************************
import requests
import re
from lxml import etree

def font_params():
    font_source = {
        "0": "$E0BD,$E0C5,$E1AB,$E1F5,$E2C5,$E36E,$E37C,$E380,$E69F,$E6C4,$E6CD,$E6FD,$E702,$E703,$E844,$E900,$E935,$EB3F,$EB89,$EBBE,$EC45,$ECA2,$ECCB,$ED2D,$ED32,$EED3,$EF9D,$EFCF,$F007,$F0EC,$F11B,$F12B,$F130,$F1AB,$F211,$F2A0,$F2B4,$F345,$F377,$F380,$F3BA,$F41E,$F536,$F544,$F58F,$F5EE,$F6AF,$F6CE,$F6E0,$F811".split(
            ","),
        "1": "$E0F8,$E0FB,$E15D,$E1B7,$E25C,$E314,$E4A1,$E515,$E522,$E55F,$E741,$E7B2,$E7FC,$E822,$E862,$E899,$E914,$E921,$E94E,$EA9F,$EAEE,$EB0A,$EB69,$EB77,$EC60,$EC6C,$EC8B,$EC8C,$ECC2,$ECF1,$EEE2,$EFCC,$EFEF,$F0CE,$F19A,$F1B7,$F294,$F469,$F57F,$F5DB,$F6A2,$F745,$F75B,$F767,$F78A,$F7BE,$F7FB,$F81A,$F830,$F8AB".split(
            ","),
        "2": "$E0AF,$E0E7,$E151,$E1BC,$E228,$E38C,$E3F4,$E492,$E548,$E649,$E74D,$E826,$E933,$E938,$E955,$E9CE,$EAC7,$EBE1,$EC13,$EC30,$EC4C,$EC85,$ECAF,$ECE9,$ECF2,$EE8D,$EEA2,$EFA4,$F04D,$F0F9,$F0FD,$F126,$F148,$F193,$F1C8,$F1D1,$F1D3,$F25A,$F319,$F329,$F34B,$F3C2,$F3F0,$F409,$F42C,$F4BA,$F58C,$F5BC,$F815,$F86E".split(
            ","),
        "3": "$E01C,$E083,$E087,$E09A,$E18B,$E1FF,$E297,$E397,$E4C5,$E513,$E6AE,$E6CC,$E712,$E7AF,$E81E,$E837,$E84C,$E8C6,$E8D1,$EAE1,$EB94,$EC43,$ECF3,$ED99,$ED9D,$EDCD,$EE09,$EE6C,$EE6E,$EEDB,$EF39,$F00E,$F02F,$F03C,$F079,$F093,$F0D2,$F0F6,$F13E,$F1D6,$F1DB,$F3A1,$F455,$F45A,$F535,$F569,$F5FD,$F714,$F7F6,$F87E".split(
            ","),
        "4": "$E076,$E0FF,$E10A,$E129,$E165,$E1E0,$E22B,$E23A,$E283,$E2D6,$E34E,$E370,$E37D,$E3E1,$E3F0,$E59F,$E5B3,$E5DC,$E669,$E7E7,$E7FF,$E80E,$E8A3,$E957,$E98E,$EA7F,$EB87,$EC91,$ECD6,$ED73,$EE20,$EE59,$EEB3,$EFA3,$EFDE,$EFED,$F053,$F091,$F0A5,$F0AE,$F0C2,$F1E9,$F248,$F2B3,$F2ED,$F43C,$F476,$F7BF,$F839,$F863".split(
            ","),
        "5": "$E01F,$E167,$E16D,$E241,$E2C3,$E394,$E415,$E471,$E4E9,$E4F0,$E531,$E54F,$E558,$E5E0,$E6C2,$E71D,$E74F,$E773,$E781,$E91E,$E956,$E9E0,$EB81,$EB8A,$EC7A,$EDB0,$EDDA,$EE39,$EEDA,$EEE0,$EF0C,$F165,$F230,$F239,$F242,$F299,$F34A,$F38E,$F3AD,$F3FC,$F443,$F457,$F4BE,$F58B,$F5ED,$F61D,$F64A,$F6D8,$F77B,$F7A5".split(
            ","),
        "6": "$E072,$E0A8,$E0C9,$E128,$E22A,$E23E,$E24B,$E293,$E40D,$E561,$E65F,$E67F,$E6E5,$E742,$E778,$E866,$E86B,$E92C,$E971,$E9AF,$EA0A,$EA5B,$EA93,$EAF0,$EB8B,$ECBE,$EDA2,$EE81,$EF05,$EF48,$EF6A,$EF6F,$F087,$F15A,$F1B2,$F1DE,$F254,$F375,$F4E4,$F517,$F518,$F62D,$F6B0,$F6E9,$F6F3,$F784,$F838,$F84C,$F85F,$F8DF".split(
            ","),
        "7": "$E0D8,$E0EE,$E191,$E214,$E233,$E2F1,$E3BC,$E3FE,$E465,$E527,$E56B,$E57E,$E5F8,$E62E,$E6B2,$E823,$E838,$E851,$E89C,$E8CE,$E993,$E9BF,$E9E4,$E9FD,$EADC,$EB48,$EB97,$EBD9,$EC17,$EE04,$EEB5,$EEBD,$EECE,$EF5C,$EF7A,$F018,$F12E,$F27D,$F298,$F2DE,$F301,$F397,$F53A,$F578,$F5C8,$F746,$F888,$F89B,$F8A6,$F8BC".split(
            ","),
        "8": "$E0B7,$E0C4,$E0F0,$E141,$E147,$E1A1,$E28E,$E3D4,$E404,$E405,$E473,$E480,$E512,$E5EE,$E68A,$E69C,$E71E,$E7AE,$E942,$EB4C,$EBC4,$EBCB,$EBD5,$EC10,$EC68,$ECBF,$ECE1,$ECE7,$ED0B,$ED3D,$EDB7,$EE30,$EE73,$EF12,$F19D,$F1BB,$F1D7,$F209,$F2B6,$F37A,$F43F,$F480,$F496,$F4DF,$F54E,$F556,$F73B,$F7F2,$F831,$F8B7".split(
            ","),
        "9": "$E067,$E09D,$E0B5,$E2A8,$E2CB,$E333,$E51E,$E555,$E5BD,$E5C9,$E5FF,$E64E,$E6AD,$E6E2,$E726,$E769,$E8A5,$E8B4,$E8CC,$E8F6,$E96A,$EAD7,$EB26,$EB51,$EB62,$EB63,$EB9A,$EDC0,$EE90,$EF04,$EFF9,$F065,$F077,$F12A,$F184,$F227,$F250,$F268,$F406,$F4A5,$F514,$F549,$F587,$F622,$F629,$F678,$F6CD,$F7E1,$F807,$F821".split(
            ",")
    }
    font_handle = dict()
    for _k, _v in font_source.items():
        font_handle[_k] = list()
        for _vv in _v:
            font_handle[_k].append(f"&#x{_vv[1:]};")
    return font_handle

def font_map(S):
    font_map = font_params()

    def su(num):
        # 取出匹配的字符
        num = num.group()
        for k, v in font_map.items():
            if num in v:
                return k

    return re.sub("&#x.*?;", su, S)

def get_data():
    headers = {
        "referer": "https://www.bthhotels.com/list/hangzhou",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    }
    url = "https://www.bthhotels.com/list/shanghai"
    res = requests.get(url, headers=headers)
    html = etree.HTML(font_map(res.text))
    html2 = etree.HTML(res.text)
    titles = html2.xpath('//p[@class="namenav"]')
    rooms = html.xpath('//ul[@class="list_recommend_intro"]')
    data = dict()
    for _yy, _uu in zip(titles, rooms):
        data["title"] = _yy.xpath("string(.)").strip().replace("\n", "").replace(" ", "")
        data["price"] = _uu.xpath('string(.//ul[@class="list_intro_money_top"])').strip().replace("\n", "").replace(" ",
                                                                                                                    "")
        print(data)

get_data()
