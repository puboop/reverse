var $$O0 = require('crypto-js')
var skeParsed = {
    "words": [
        1867535458,
        1798661458,
        1296266034,
        860309831
    ],
    "sigBytes": 16
}

function encryption(t) {
    const r = encodeURI(JSON["stringify"](t || {}, null, 2))
        , n = $$O0['enc']['Utf8']['parse'](r)
        , s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'['split']("")
        , o = Array['from']({
        length: 16
    })['map'](() => s[Math['floor'](Math['random']() * s['length'])])['join']("")
        , i = QQ0109OO()
        , c = $$O0['AES']['encrypt'](n, skeParsed, {
        iv: i,
        mode: $$O0['mode']['CBC'],
        padding: $$O0['pad']['Pkcs7']
    })['toString']();
    return {
        iv: $$O0['enc']['Utf8']['parse'](o),
        data: btoa(c)
    }
}

function QQ0109OO() {
    const t = 'BmStJeaRsVFZubmH'['split']("")
        , r = new Date()['getHours']() % 9;
    let n = "";
    return t['forEach']((s, o) => {
            n += o === r ? r : s
        }
    ),
        $$O0['enc']['Utf8']['parse'](n)
}

function white(phone) {
    const {iv: r, data: n} = encryption({phone: phone});
    return [r.toString(), n.toString()]
}

// 测试用例
// const {iv: r, data: n} = encryption({phone: '13500000000'});
// console.log(r.toString());
// console.log(n.toString());
