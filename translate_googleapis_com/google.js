var Vp = "469040.3323378158"
// var Vp = "406398.2087938574"
// var Vp = "469087.555664397"

var zo = function (a) {
    for (var b = [], c = 0, d = 0; d < a.length; d++) {
        var e = a.charCodeAt(d);
        128 > e ? b[c++] = e : (2048 > e ? b[c++] = e >> 6 | 192 : (55296 == (e & 64512) && d + 1 < a.length && 56320 == (a.charCodeAt(d + 1) & 64512) ? (e = 65536 + ((e & 1023) << 10) + (a.charCodeAt(++d) & 1023),
            b[c++] = e >> 18 | 240,
            b[c++] = e >> 12 & 63 | 128) : b[c++] = e >> 12 | 224,
            b[c++] = e >> 6 & 63 | 128),
            b[c++] = e & 63 | 128)
    }
    return b
}
Up = function (a, b) {
    for (var c = 0; c < b.length - 2; c += 3) {
        var d = b.charAt(c + 2);
        d = "a" <= d ? d.charCodeAt(0) - 87 : Number(d);
        d = "+" == b.charAt(c + 1) ? a >>> d : a << d;
        a = "+" == b.charAt(c) ? a + d & 4294967295 : a ^ d
    }
    return a
}

Wp = function (a) {
    var b = Vp.split(".")
        , c = Number(b[0]) || 0;
    a = zo(a);
    for (var d = c, e = 0; e < a.length; e++)
        d += a[e],
            d = Up(d, "+-a^+6");
    d = Up(d, "+-3^+b+-f");
    d ^= Number(b[1]) || 0;
    0 > d && (d = (d & 2147483647) + 2147483648);
    b = d % 1E6;
    return b.toString() + "." + (b ^ c)
}

function white(data) {
    return Wp(data)
}

// 测试案例
// var translate_str = "我爱你xxs"
// console.log(white(translate_str));
/*
469087.555664397  915358.712641
406398.2087938574  783736.902662
469040.3323378158  74754.396338
 */