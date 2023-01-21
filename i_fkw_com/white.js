function o(u, z) {
    var w = (u & 65535) + (z & 65535)
        , v = (u >> 16) + (z >> 16) + (w >> 16);
    return (v << 16) | (w & 65535)
}
function s(u, v) {
    return (u << v) | (u >>> (32 - v))
}
function c(A, w, v, u, z, y) {
    return o(s(o(o(w, A), o(u, y)), z), v)
}
function b(w, v, B, A, u, z, y) {
    return c((v & B) | ((~v) & A), w, v, u, z, y)
}
function i(w, v, B, A, u, z, y) {
    return c((v & A) | (B & (~A)), w, v, u, z, y)
}
function n(w, v, B, A, u, z, y) {
    return c(v ^ B ^ A, w, v, u, z, y)
}
function a(w, v, B, A, u, z, y) {
    return c(B ^ (v | (~A)), w, v, u, z, y)
}
function d(F, A) {
    F[A >> 5] |= 128 << ((A) % 32);
    F[(((A + 64) >>> 9) << 4) + 14] = A;
    var w, z, y, v, u, E = 1732584193, D = -271733879, C = -1732584194, B = 271733878;
    for (w = 0; w < F.length; w += 16) {
        z = E;
        y = D;
        v = C;
        u = B;
        E = b(E, D, C, B, F[w], 7, -680876936);
        B = b(B, E, D, C, F[w + 1], 12, -389564586);
        C = b(C, B, E, D, F[w + 2], 17, 606105819);
        D = b(D, C, B, E, F[w + 3], 22, -1044525330);
        E = b(E, D, C, B, F[w + 4], 7, -176418897);
        B = b(B, E, D, C, F[w + 5], 12, 1200080426);
        C = b(C, B, E, D, F[w + 6], 17, -1473231341);
        D = b(D, C, B, E, F[w + 7], 22, -45705983);
        E = b(E, D, C, B, F[w + 8], 7, 1770035416);
        B = b(B, E, D, C, F[w + 9], 12, -1958414417);
        C = b(C, B, E, D, F[w + 10], 17, -42063);
        D = b(D, C, B, E, F[w + 11], 22, -1990404162);
        E = b(E, D, C, B, F[w + 12], 7, 1804603682);
        B = b(B, E, D, C, F[w + 13], 12, -40341101);
        C = b(C, B, E, D, F[w + 14], 17, -1502002290);
        D = b(D, C, B, E, F[w + 15], 22, 1236535329);
        E = i(E, D, C, B, F[w + 1], 5, -165796510);
        B = i(B, E, D, C, F[w + 6], 9, -1069501632);
        C = i(C, B, E, D, F[w + 11], 14, 643717713);
        D = i(D, C, B, E, F[w], 20, -373897302);
        E = i(E, D, C, B, F[w + 5], 5, -701558691);
        B = i(B, E, D, C, F[w + 10], 9, 38016083);
        C = i(C, B, E, D, F[w + 15], 14, -660478335);
        D = i(D, C, B, E, F[w + 4], 20, -405537848);
        E = i(E, D, C, B, F[w + 9], 5, 568446438);
        B = i(B, E, D, C, F[w + 14], 9, -1019803690);
        C = i(C, B, E, D, F[w + 3], 14, -187363961);
        D = i(D, C, B, E, F[w + 8], 20, 1163531501);
        E = i(E, D, C, B, F[w + 13], 5, -1444681467);
        B = i(B, E, D, C, F[w + 2], 9, -51403784);
        C = i(C, B, E, D, F[w + 7], 14, 1735328473);
        D = i(D, C, B, E, F[w + 12], 20, -1926607734);
        E = n(E, D, C, B, F[w + 5], 4, -378558);
        B = n(B, E, D, C, F[w + 8], 11, -2022574463);
        C = n(C, B, E, D, F[w + 11], 16, 1839030562);
        D = n(D, C, B, E, F[w + 14], 23, -35309556);
        E = n(E, D, C, B, F[w + 1], 4, -1530992060);
        B = n(B, E, D, C, F[w + 4], 11, 1272893353);
        C = n(C, B, E, D, F[w + 7], 16, -155497632);
        D = n(D, C, B, E, F[w + 10], 23, -1094730640);
        E = n(E, D, C, B, F[w + 13], 4, 681279174);
        B = n(B, E, D, C, F[w], 11, -358537222);
        C = n(C, B, E, D, F[w + 3], 16, -722521979);
        D = n(D, C, B, E, F[w + 6], 23, 76029189);
        E = n(E, D, C, B, F[w + 9], 4, -640364487);
        B = n(B, E, D, C, F[w + 12], 11, -421815835);
        C = n(C, B, E, D, F[w + 15], 16, 530742520);
        D = n(D, C, B, E, F[w + 2], 23, -995338651);
        E = a(E, D, C, B, F[w], 6, -198630844);
        B = a(B, E, D, C, F[w + 7], 10, 1126891415);
        C = a(C, B, E, D, F[w + 14], 15, -1416354905);
        D = a(D, C, B, E, F[w + 5], 21, -57434055);
        E = a(E, D, C, B, F[w + 12], 6, 1700485571);
        B = a(B, E, D, C, F[w + 3], 10, -1894986606);
        C = a(C, B, E, D, F[w + 10], 15, -1051523);
        D = a(D, C, B, E, F[w + 1], 21, -2054922799);
        E = a(E, D, C, B, F[w + 8], 6, 1873313359);
        B = a(B, E, D, C, F[w + 15], 10, -30611744);
        C = a(C, B, E, D, F[w + 6], 15, -1560198380);
        D = a(D, C, B, E, F[w + 13], 21, 1309151649);
        E = a(E, D, C, B, F[w + 4], 6, -145523070);
        B = a(B, E, D, C, F[w + 11], 10, -1120210379);
        C = a(C, B, E, D, F[w + 2], 15, 718787259);
        D = a(D, C, B, E, F[w + 9], 21, -343485551);
        E = o(E, z);
        D = o(D, y);
        C = o(C, v);
        B = o(B, u)
    }
    return [E, D, C, B]
}
function p(v) {
    var w, u = "";
    for (w = 0; w < v.length * 32; w += 8) {
        u += String.fromCharCode((v[w >> 5] >>> (w % 32)) & 255)
    }
    return u
}
function j(v) {
    var w, u = [];
    u[(v.length >> 2) - 1] = undefined;
    for (w = 0; w < u.length; w += 1) {
        u[w] = 0
    }
    for (w = 0; w < v.length * 8; w += 8) {
        u[w >> 5] |= (v.charCodeAt(w / 8) & 255) << (w % 32)
    }
    return u
}
function k(u) {
    return p(d(j(u), u.length * 8))
}
function f(w, z) {
    var v, y = j(w), u = [], x = [], A;
    u[15] = x[15] = undefined;
    if (y.length > 16) {
        y = d(y, w.length * 8)
    }
    for (v = 0; v < 16; v += 1) {
        u[v] = y[v] ^ 909522486;
        x[v] = y[v] ^ 1549556828
    }
    A = d(u.concat(j(z)), 512 + z.length * 8);
    return p(d(x.concat(A), 512 + 128))
}
function t(w) {
    var z = "0123456789abcdef", v = "", u, y;
    for (y = 0; y < w.length; y += 1) {
        u = w.charCodeAt(y);
        v += z.charAt((u >>> 4) & 15) + z.charAt(u & 15)
    }
    return v
}
function m(u) {
    return unescape(encodeURIComponent(u))
}
function q(u) {
    return k(m(u))
}
function l(u) {
    return t(q(u))
}
function h(u, v) {
    return f(m(u), m(v))
}
function r(u, v) {
    return t(h(u, v))
}
function white(pwd){
    return l(pwd)
}
// 测试用例
// console.log(white("123456"));
