var n = [
    "aHR0cHM6Ly9tcA==",
    "anBMUk8=",
    "Z2V0VGltZQ==",
    "aVRWdHI=",
    "V25PS2g=",
    "cmVxdWVzdA==",
    "c2hvd0xvYWRpbg==",
    "akFYWWo=",
    "ZHlWalA=",
    "dGhlbg==",
    "Z2V0",
    "Z2V0U3RvcmFnZQ==",
    "TXF5bEU=",
    "ZGVk",
    "dXNlckluZm8=",
    "Y09DT1g=",
    "T1VEUm0=",
    "Y29udGVudC10eQ==",
    "bGVuZ3Ro",
    "bWV0aG9k",
    "QUJDREVGR0hKSw==",
    "dkZ1Qm8=",
    "dUtMS1g=",
    "WmFiY2RlZmhpag==",
    "a2Vu",
    "Y2F0Y2g=",
    "dGl0bGU=",
    "cm0tdXJsZW5jbw==",
    "cG9zdA==",
    "R0VU",
    "aGlkZUxvYWRpbg==",
    "bi9hcGk=",
    "bi94LXd3dy1mbw==",
    "TU5QUVJTVFdYWQ==",
    "b3Blbmlk",
    "PyZ0PQ==",
    "dUhiRlg=",
    "U3luYw==",
    "WENDVXc=",
    "QW51S3E=",
    "TFZUaHI=",
    "UE9TVA==",
    "cnNFSWY=",
    "ZWpVYWM=",
    "aGVhZGVy",
    "UkNiV3g=",
    "ZGF0YQ==",
    "bXBfb3Blbmlk",
    "SE5KWUE=",
    "LmZpbGltcWkuYw==",
    "a21ucHJzdHd4eQ==",
    "eUhaRng=",
    "dHlwZQ==",
    "Y0dWbFA=",
    "UkhEUFA=",
    "bmpNRWI=",
    "dXJs",
    "b3lIdUs=",
    "bm90TG9naW5Vcw==",
    "bG9hZGluZy4uLg==",
    "YlBrZmI=",
    "a2hXemg=",
    "YXBwbGljYXRpbw==",
    "cmVxdWVzdC10bw==",
    "ejIzNDU2Nzg=",
    "d3NEdUQ=",
    "Z25iQmU=",
    "cmFuZG9t",
    "UWlncnc=",
    "bW5IVkE=",
    "cWxKc2Q=",
    "WHdPZFg="
]

var I = function A(B, g) {
    B -= 0;
    var E = n[B];
    void 0 === A["DbYZDg"] && (function () {
        var A;
        try {
            var B = Function('return (function() {}.constructor("return this")( ));');
            A = B()
        } catch (g) {
            A = window
        }
        A["atob"] || (A["atob"] = function (A) {
                for (var B, g, E = String(A)["replace"](/=+$/, ""), i = "", Q = 0, n = 0; g = E["charAt"](n++); ~g && (B = Q % 4 ? 64 * B + g : g,
                Q++ % 4) ? i += String["fromCharCode"](255 & B >> (-2 * Q & 6)) : 0)
                    g = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="["indexOf"](g);
                return i
            }
        )
    }(),
        A["aXFxPe"] = function (A) {
            for (var B = atob(A), g = [], E = 0, i = B["length"]; E < i; E++)
                g += "%" + ("00" + B["charCodeAt"](E)["toString"](16))["slice"](-2);
            return decodeURIComponent(g)
        }
        ,
        A["WgNtEM"] = {},
        A["DbYZDg"] = !0);
    var i = A["WgNtEM"][B];
    return void 0 === i ? (E = A["aXFxPe"](E),
        A["WgNtEM"][B] = E) : E = i,
        E
}

function get_request_token(A) {
    var B = {
        XwOdX: function (A, B) {
            return A(B)
        },
        MqylE: function (A, B) {
            return A(B)
        },
        jAXYj: function (A, B) {
            return A + B
        }
    };
    B[I("0x2a")] = I("0x23"),
        B["oyHuK"] = function (A, B) {
            return A || B
        }
        ,
        B[I("0x28")] = I("0x14") + I("0x21") + I("0x17") + I("0x32") + I("0x40"),
        B[I("0x27")] = function (A, B) {
            return A < B
        }
        ,
        B[I("0x10")] = function (A, B) {
            return A * B
        }
    ;
    var g = B;
    A = g[I("0x39")](A, 32);
    for (var E = g[I("0x28")], Q = E[I("0x12")], n = "", w = 0; g[I("0x27")](w, A); w++)
        if ("aqyJU" !== I("0x45"))
            n += E["charAt"](Math["floor"](g["OUDRm"](Math[I("0x43")](), Q)));
        else {
            var c = {
                Qigrw: function (A, B) {
                    return g[I("0xc")](A, B)
                }
            }
                , o = c
                , C = {};
            C["url"] = g[I("0x7")](g[I("0x7")](g[I("0x7")](M, options[I("0x38")]), g["rsEIf"]), t) || "",
                C[I("0x13")] = options[I("0x34")] || "GET",
                C[I("0x2e")] = options[I("0x2e")] || {},
                C[I("0x2c")] = options[I("0x2c")],
                uni[I("0x5")](C)["then"]((function (A) {
                        var B = (0,
                            i.default)(A, 2)
                            , E = (B[0],
                            B[1]);
                        g[I("0x47")](resolve, E),
                            uni[I("0x1e") + "g"]()
                    }
                ))["catch"]((function (A) {
                        o[I("0x44")](reject, A),
                            uni[I("0x1e") + "g"]()
                    }
                ))
        }
    return n
}

//////////////////////////token


function token(A, B, g) {
    function CcC(A) {
        var B, g = "", E = 32 * A.length;
        for (B = 0; B < E; B += 8)
            g += String.fromCharCode(A[B >> 5] >>> B % 32 & 255);
        return g
    }


    function AaA(A) {
        var B, g = [];
        for (g[(A.length >> 2) - 1] = void 0,
                 B = 0; B < g.length; B += 1)
            g[B] = 0;
        var E = 8 * A.length;
        for (B = 0; B < E; B += 8)
            g[B >> 5] |= (255 & A.charCodeAt(B / 8)) << B % 32;
        return g
    }


    function OoO(A, B) {
        function Q(A, B) {
            var g = (65535 & A) + (65535 & B);
            return (A >> 16) + (B >> 16) + (g >> 16) << 16 | 65535 & g
        }

        function n(A, B, g, E, i, n) {
            return Q(function (A, B) {
                return A << B | A >>> 32 - B
            }(Q(Q(B, A), Q(E, n)), i), g)
        }

        function I(A, B, g, E, i, Q, I) {
            return n(B & g | ~B & E, A, B, i, Q, I)
        }

        function M(A, B, g, E, i, Q, I) {
            return n(B & E | g & ~E, A, B, i, Q, I)
        }

        function w(A, B, g, E, i, Q, I) {
            return n(B ^ g ^ E, A, B, i, Q, I)
        }

        function c(A, B, g, E, i, Q, I) {
            return n(g ^ (B | ~E), A, B, i, Q, I)
        }

        function o(A, B) {
            A[B >> 5] |= 128 << B % 32,
                A[14 + (B + 64 >>> 9 << 4)] = B;
            var g, E, i, n, o, a = 1732584193, C = -271733879, r = -1732584194, p = 271733878;
            for (g = 0; g < A.length; g += 16)
                E = a,
                    i = C,
                    n = r,
                    o = p,
                    C = c(C = c(C = c(C = c(C = w(C = w(C = w(C = w(C = M(C = M(C = M(C = M(C = I(C = I(C = I(C = I(C, r = I(r, p = I(p, a = I(a, C, r, p, A[g], 7, -680876936), C, r, A[g + 1], 12, -389564586), a, C, A[g + 2], 17, 606105819), p, a, A[g + 3], 22, -1044525330), r = I(r, p = I(p, a = I(a, C, r, p, A[g + 4], 7, -176418897), C, r, A[g + 5], 12, 1200080426), a, C, A[g + 6], 17, -1473231341), p, a, A[g + 7], 22, -45705983), r = I(r, p = I(p, a = I(a, C, r, p, A[g + 8], 7, 1770035416), C, r, A[g + 9], 12, -1958414417), a, C, A[g + 10], 17, -42063), p, a, A[g + 11], 22, -1990404162), r = I(r, p = I(p, a = I(a, C, r, p, A[g + 12], 7, 1804603682), C, r, A[g + 13], 12, -40341101), a, C, A[g + 14], 17, -1502002290), p, a, A[g + 15], 22, 1236535329), r = M(r, p = M(p, a = M(a, C, r, p, A[g + 1], 5, -165796510), C, r, A[g + 6], 9, -1069501632), a, C, A[g + 11], 14, 643717713), p, a, A[g], 20, -373897302), r = M(r, p = M(p, a = M(a, C, r, p, A[g + 5], 5, -701558691), C, r, A[g + 10], 9, 38016083), a, C, A[g + 15], 14, -660478335), p, a, A[g + 4], 20, -405537848), r = M(r, p = M(p, a = M(a, C, r, p, A[g + 9], 5, 568446438), C, r, A[g + 14], 9, -1019803690), a, C, A[g + 3], 14, -187363961), p, a, A[g + 8], 20, 1163531501), r = M(r, p = M(p, a = M(a, C, r, p, A[g + 13], 5, -1444681467), C, r, A[g + 2], 9, -51403784), a, C, A[g + 7], 14, 1735328473), p, a, A[g + 12], 20, -1926607734), r = w(r, p = w(p, a = w(a, C, r, p, A[g + 5], 4, -378558), C, r, A[g + 8], 11, -2022574463), a, C, A[g + 11], 16, 1839030562), p, a, A[g + 14], 23, -35309556), r = w(r, p = w(p, a = w(a, C, r, p, A[g + 1], 4, -1530992060), C, r, A[g + 4], 11, 1272893353), a, C, A[g + 7], 16, -155497632), p, a, A[g + 10], 23, -1094730640), r = w(r, p = w(p, a = w(a, C, r, p, A[g + 13], 4, 681279174), C, r, A[g], 11, -358537222), a, C, A[g + 3], 16, -722521979), p, a, A[g + 6], 23, 76029189), r = w(r, p = w(p, a = w(a, C, r, p, A[g + 9], 4, -640364487), C, r, A[g + 12], 11, -421815835), a, C, A[g + 15], 16, 530742520), p, a, A[g + 2], 23, -995338651), r = c(r, p = c(p, a = c(a, C, r, p, A[g], 6, -198630844), C, r, A[g + 7], 10, 1126891415), a, C, A[g + 14], 15, -1416354905), p, a, A[g + 5], 21, -57434055), r = c(r, p = c(p, a = c(a, C, r, p, A[g + 12], 6, 1700485571), C, r, A[g + 3], 10, -1894986606), a, C, A[g + 10], 15, -1051523), p, a, A[g + 1], 21, -2054922799), r = c(r, p = c(p, a = c(a, C, r, p, A[g + 8], 6, 1873313359), C, r, A[g + 15], 10, -30611744), a, C, A[g + 6], 15, -1560198380), p, a, A[g + 13], 21, 1309151649), r = c(r, p = c(p, a = c(a, C, r, p, A[g + 4], 6, -145523070), C, r, A[g + 11], 10, -1120210379), a, C, A[g + 2], 15, 718787259), p, a, A[g + 9], 21, -343485551),
                    a = Q(a, E),
                    C = Q(C, i),
                    r = Q(r, n),
                    p = Q(p, o);
            return [a, C, r, p]
        }

        return o(A, B)
    }


    function p(A) {
        var B, g, E = "";
        for (g = 0; g < A.length; g += 1)
            B = A.charCodeAt(g),
                E += "0123456789abcdef".charAt(B >>> 4 & 15) + "0123456789abcdef".charAt(15 & B);
        return E
    }

    function RrR(A) {
        return unescape(encodeURIComponent(A))
    }

    function F(A) {
        return function (A) {
            return CcC(OoO(AaA(A), 8 * A.length))
        }(RrR(A))
    }

    function Q_default(A, B, g) {
        // return B ? g ? t(B, A) : function (A, B) {
        //     return p(t(A, B))
        // }(B, A) : g ? F(A) : function (A) {
        //     return p(F(A))
        // }(A)
        return p(F(A))
    }

    var E = {
        uKLKX: function (A, B) {
            return A + B
        },
        khWzh: function (A, B) {
            return A + B
        }
    };
    E["HNJYA"] = function (A, B) {
        return A(B)
    }
    ;
    // var i = E
    //     // , n = i["uKLKX"](i["khWzh"](A, B), g)
    //     , M = i["HNJYA"](Q_default, A + B + g);
    var M = Q_default(A + B + g)
    return M
}

function white(time_stamp) {
    var request_token = get_request_token(99);
    var sign = token(request_token, "https://mp.filimqi.cn/api", time_stamp);
    return [request_token, sign]
}

function white_test() {
    var time_stamp = (new Date)["getTime"]();
    var request_token = get_request_token(99);
    // var time_stamp = 1705384822822;
    // var request_token = "PRmWsxynrCEn4JaSYt6ZD6Z53jQFpXHcdA4dbh5cdzQPzbm25fkyBjcSehj6cACxNSzf5MRtp7HGrnXZ6Cabn8AkDQwWifzFDfy";
    //[-262127070, 1577214238, 1155401283, 644789940]  224260f01e61025e4306de44b4b66e26
    console.log(token(request_token, 'https://mp.filimqi.cn/api', time_stamp));
}

white_test()