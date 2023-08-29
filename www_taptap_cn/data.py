import random
import re
import time
try:
    import execjs
except:
    pass
import pandas as pd
import requests


class GetComment:

    def __init__(self, referer):
        self.cookies = {
            "acw_sc__v2": "64e1bd723bb3f79adb22fdc374d87edfd988b5e7",
        }
        self.headers = {
            "Referer"   : referer,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203",
        }
        self.url = "https://www.taptap.cn/webapiv2/moment-comment/v1/by-moment"
        self.js_code = '''
        function _0x4818(arg1) {
    var posList = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
    var mask = '3000176000856006061501533003690027800375';
    var outPutList = [];
    var arg2 = "";
    var arg3 = "";
    for (var i = 0; i < arg1['length']; i++) {
        var this_i = arg1[i];
        for (var j = 0; j < posList['length']; j++) {
            if (posList[j] == i + 1) {
                outPutList[j] = this_i
            }
        }
    }
    arg2 = outPutList['join']("");
    for (var i = 0; i < arg2['length'] && i < mask['length']; i += 2) {
        var GxjQsM = '1|4|3|0|2'['split']("|")
            , QoWazb = 0;
        while (!![]) {
            switch (GxjQsM[QoWazb++]) {
                case "0":
                    if (xorChar['length'] == 1) {
                        xorChar = "0" + xorChar
                    }
                    continue;
                case "1":
                    var strChar = parseInt(arg2['slice'](i, i + 2), 16);
                    continue;
                case "2":
                    arg3 += xorChar;
                    continue;
                case "3":
                    var xorChar = (strChar ^ maskChar)['toString'](16);
                    continue;
                case "4":
                    var maskChar = parseInt(mask['slice'](i, i + 2), 16);
                    continue
            }
            break
        }
    }
    return arg3;
}

function white(arg1) {
    return _0x4818(arg1);
}

function test() {
    var arg1 = "E0353A9BC794DE54451A9AC1AE58E4F4D349F6F5";
    console.log(_0x4818(arg1));
}
'''
        self.params = {
            "from"        : "10",
            "limit"       : "10",
            "moment_id"   : "433727128970725816",
            "order"       : "desc",
            "regulate_all": "false",
            "sort"        : "rank",
            "X-UA"        : "V=1&PN=WebApp&LANG=zh_CN&VN_CODE=102&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=c88b8a25-c63f-40fa-a137-942311b5f47a&DT=PC&OS=Windows&OSV=7.0.0"
        }
        self.server_pool = ['木兰山中', '苗疆密林', '离忧谷', '天山雪谷', '无名幻境', '龙泉剑庐', '洞庭月夜',
                            '水月山庄',
                            '墨家古阵',
                            '天津晓月', '明月楼', '桃花坞', '柳剑山庄', '南海之滨']

    def get_acw_sc_js(self, arg1):
        result = execjs.compile(self.js_code).call("white", arg1)
        print("js加密结果>" + result)
        return result

    def get_acw_sc_py(self, arg1):
        posList = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21,
                   32,
                   26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36]
        mask = '3000176000856006061501533003690027800375'
        outPutList = [None] * len(arg1)
        arg3 = ""
        for i in range(len(arg1)):
            this_i = arg1[i]
            for j in range(len(posList)):
                if posList[j] == i + 1:
                    outPutList[j] = this_i
        arg2 = "".join(outPutList)
        for i in range(0, len(mask), 2):
            GxjQsM = '1|4|3|0|2'.split("|")
            for QoWazb in range(len(GxjQsM)):
                tmp_var = GxjQsM[QoWazb]
                if tmp_var == "0":
                    if len(xorChar) == 1:
                        xorChar = "0" + xorChar
                elif tmp_var == "1":
                    strChar = int(arg2[i:i + 2], 16)
                elif tmp_var == "2":
                    arg3 += xorChar
                elif tmp_var == "3":
                    xorChar = hex(strChar ^ maskChar)
                    if len(xorChar) != 4:
                        xorChar = "0" + xorChar[-1:]
                    else:
                        xorChar = xorChar[-2:]
                elif tmp_var == "4":
                    maskChar = int(mask[i:i + 2], 16)
        print("py加密结果>" + arg3)
        return arg3

    def response(self, params):
        res = requests.get(url=self.url, headers=self.headers, cookies=self.cookies, params=params)
        print("获取返回结果>" + res.text)
        if "acw_sc__v2" in res.text:
            arg1 = res.text.split("arg1='")[1].split("';")[0]
            print("重新加密>" + arg1)
            self.cookies["acw_sc__v2"] = self.get_acw_sc_py(arg1)
            return self.response(params)
        try:
            data = res.json()['data']['list']
            return data
        except:
            return False

    def get_comment(self, data):
        col = ['社区用户名', '楼层', '服务器名', '角色id', '回复内容', '回复时间']
        df = pd.DataFrame(columns=col)
        for room in data:
            DATA = {
                "社区用户名": "",
                "楼层"      : "",
                "回复时间"  : "",
                "服务器名"  : "",
                "角色id"    : "",
                "回复内容"  : "",

            }
            DATA["社区用户名"] = room["author"]["name"]
            DATA["楼层"] = room["position"]
            timeArray = time.localtime(room["created_time"])
            ostime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            DATA["回复时间"] = ostime
            for house in room["contents"]["json"]:
                text = house["children"][0]["text"].strip()  # 除去首尾空格
                if text:
                    DATA["回复内容"] += text + "/"
                # 从回复内容中匹配ID及服务器
                ID = re.search("\d{7,9}", DATA["回复内容"])
                if ID:
                    DATA["角色id"] = ID.group()
                else:
                    DATA["角色id"] = None
                n = 0  # 用于判断是否匹配到服务器
                for str1 in self.server_pool:
                    if str1 in DATA["回复内容"] and n == 0:
                        DATA["服务器名"] = str1
                        n += 1
                if n == 0:
                    DATA["服务器名"] = None
            df = df._append([DATA], ignore_index=True, verify_integrity=False)
        return df

    def run(self, page):
        col = ['社区用户名', '楼层', "服务器名", "角色id", '回复内容', '回复时间']
        dff = pd.DataFrame(columns=col)
        for page_n in range(0, page * 10, 10):
            self.params['from'] = str(page_n)
            result = self.response(self.params)
            if result is False:
                break
            dff = dff._append(self.get_comment(result), ignore_index=True)
            time.sleep(random.randint(1, 5))  # m每爬一次休息1秒
        # dff.to_excel("data.xlsx", index=False)
        return dff


if __name__ == '__main__':
    referfer = "https://www.taptap.cn/moment/433727128970725816"
    page = 21
    c = GetComment(referfer)
    result = c.run(page)
