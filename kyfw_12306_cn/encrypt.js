var u = [];
var v = [];
var d = typeof Uint8Array !== "undefined" ? Uint8Array : Array;
var t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
for (var o = 0, a = t.length; o < a; ++o) {
    u[o] = t[o];
    v[t.charCodeAt(o)] = o
}
v["-".charCodeAt(0)] = 62;
v["_".charCodeAt(0)] = 63;

function s(r) {
    return u[r >> 18 & 63] + u[r >> 12 & 63] + u[r >> 6 & 63] + u[r & 63]
}

function p(r) {
    var e;
    var n = r.length;
    var t = n % 3;
    var o = [];
    var a = 16383;
    for (var f = 0, i = n - t; f < i; f += a) {
        o.push(l(r, f, f + a > i ? i : f + a))
    }
    if (t === 1) {
        e = r[n - 1];
        o.push(u[e >> 2] + u[e << 4 & 63] + "==")
    } else if (t === 2) {
        e = (r[n - 2] << 8) + r[n - 1];
        o.push(u[e >> 10] + u[e >> 4 & 63] + u[e << 2 & 63] + "=")
    }
    return o.join("")
}

function h(r, e, n) {
    return (e + n) * 3 / 4 - n
}

function c(r) {
    var e = r.length;
    if (e % 4 > 0) {
        throw new Error("Invalid string. Length must be a multiple of 4")
    }
    var n = r.indexOf("=");
    if (n === -1) n = e;
    var t = n === e ? 0 : 4 - n % 4;
    return [n, t]
}

function l(r, e, n) {
    var t;
    var o = [];
    for (var a = e; a < n; a += 3) {
        t = (r[a] << 16 & 16711680) + (r[a + 1] << 8 & 65280) + (r[a + 2] & 255);
        o.push(s(t))
    }
    return o.join("")
}

base64js = {
    byteLength: function f(r) {
        var e = c(r);
        var n = e[0];
        var t = e[1];
        return (n + t) * 3 / 4 - t
    },
    toByteArray: function i(r) {
        var e;
        var n = c(r);
        var t = n[0];
        var o = n[1];
        var a = new d(h(r, t, o));
        var f = 0;
        var i = o > 0 ? t - 4 : t;
        var u;
        for (u = 0; u < i; u += 4) {
            e = v[r.charCodeAt(u)] << 18 | v[r.charCodeAt(u + 1)] << 12 | v[r.charCodeAt(u + 2)] << 6 | v[r.charCodeAt(u + 3)];
            a[f++] = e >> 16 & 255;
            a[f++] = e >> 8 & 255;
            a[f++] = e & 255
        }
        if (o === 2) {
            e = v[r.charCodeAt(u)] << 2 | v[r.charCodeAt(u + 1)] >> 4;
            a[f++] = e & 255
        }
        if (o === 1) {
            e = v[r.charCodeAt(u)] << 10 | v[r.charCodeAt(u + 1)] << 4 | v[r.charCodeAt(u + 2)] >> 2;
            a[f++] = e >> 8 & 255;
            a[f++] = e & 255
        }
        return a
    },
    fromByteArray: function p(r) {
        var e;
        var n = r.length;
        var t = n % 3;
        var o = [];
        var a = 16383;
        for (var f = 0, i = n - t; f < i; f += a) {
            o.push(l(r, f, f + a > i ? i : f + a))
        }
        if (t === 1) {
            e = r[n - 1];
            o.push(u[e >> 2] + u[e << 4 & 63] + "==")
        } else if (t === 2) {
            e = (r[n - 2] << 8) + r[n - 1];
            o.push(u[e >> 10] + u[e >> 4 & 63] + u[e << 2 & 63] + "=")
        }
        return o.join("")
    }
}

/////////////SM4//////////////

function _toConsumableArray(arr) {
    return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread();
}

function _nonIterableSpread() {
    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}

function _unsupportedIterableToArray(o, minLen) {
    if (!o) return;
    if (typeof o === "string") return _arrayLikeToArray(o, minLen);
    var n = Object.prototype.toString.call(o).slice(8, -1);
    if (n === "Object" && o.constructor) n = o.constructor.name;
    if (n === "Map" || n === "Set") return Array.from(o);
    if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen);
}

function _iterableToArray(iter) {
    if (typeof Symbol !== "undefined" && Symbol.iterator in Object(iter)) return Array.from(iter);
}

function _arrayWithoutHoles(arr) {
    if (Array.isArray(arr)) return _arrayLikeToArray(arr);
}

function _arrayLikeToArray(arr, len) {
    if (len == null || len > arr.length) len = arr.length;
    for (var i = 0, arr2 = new Array(len); i < len; i++) {
        arr2[i] = arr[i];
    }
    return arr2;
}

var UINT8_BLOCK = 16;
var Sbox = [0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05, 0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99, 0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62, 0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6, 0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8, 0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35, 0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87, 0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e, 0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1, 0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3, 0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f, 0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51, 0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8, 0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0, 0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84, 0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48];
var CK = [0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269, 0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9, 0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249, 0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9, 0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229, 0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299, 0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209, 0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279];
var FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc];
/**
 * 将字符串转为Unicode数组
 * @example "1234" => [49, 50, 51, 52];
 * @param {String} str 要转换的字符串
 * @returns {Number[]} 转换后的数组
 */

var stringToArray = function stringToArray(str) {
    if (!/string/gi.test(Object.prototype.toString.call(str))) {
        str = JSON.stringify(str);
    }

    return unescape(encodeURIComponent(str)).split("").map(function (val) {
        return val.charCodeAt();
    });
};

var rotateLeft = function rotateLeft(x, y) {
    return x << y | x >>> 32 - y;
};

var tauTransform = function tauTransform(a) {
    return Sbox[a >>> 24 & 0xff] << 24 | Sbox[a >>> 16 & 0xff] << 16 | Sbox[a >>> 8 & 0xff] << 8 | Sbox[a & 0xff];
};

var tTransform1 = function tTransform1(z) {
    var b = tauTransform(z);
    var c = b ^ rotateLeft(b, 2) ^ rotateLeft(b, 10) ^ rotateLeft(b, 18) ^ rotateLeft(b, 24);
    return c;
};

var tTransform2 = function tTransform2(z) {
    var b = tauTransform(z);
    var c = b ^ rotateLeft(b, 13) ^ rotateLeft(b, 23);
    return c;
};

var EncryptRoundKeys = function EncryptRoundKeys(key) {
    var keys = [];
    var mk = [key[0] << 24 | key[1] << 16 | key[2] << 8 | key[3], key[4] << 24 | key[5] << 16 | key[6] << 8 | key[7], key[8] << 24 | key[9] << 16 | key[10] << 8 | key[11], key[12] << 24 | key[13] << 16 | key[14] << 8 | key[15]];
    var k = new Array(36);
    k[0] = mk[0] ^ FK[0];
    k[1] = mk[1] ^ FK[1];
    k[2] = mk[2] ^ FK[2];
    k[3] = mk[3] ^ FK[3];

    for (var i = 0; i < 32; i++) {
        k[i + 4] = k[i] ^ tTransform2(k[i + 1] ^ k[i + 2] ^ k[i + 3] ^ CK[i]);
        keys[i] = k[i + 4];
    }

    return keys;
};

var getChainBlock = function getChainBlock(arr) {
    var baseIndex = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 0;
    var block = [arr[baseIndex] << 24 | arr[baseIndex + 1] << 16 | arr[baseIndex + 2] << 8 | arr[baseIndex + 3], arr[baseIndex + 4] << 24 | arr[baseIndex + 5] << 16 | arr[baseIndex + 6] << 8 | arr[baseIndex + 7], arr[baseIndex + 8] << 24 | arr[baseIndex + 9] << 16 | arr[baseIndex + 10] << 8 | arr[baseIndex + 11], arr[baseIndex + 12] << 24 | arr[baseIndex + 13] << 16 | arr[baseIndex + 14] << 8 | arr[baseIndex + 15]];
    return block;
};

var doBlockCrypt = function doBlockCrypt(blockData, roundKeys) {
    var xBlock = new Array(36);
    blockData.forEach(function (val, index) {
        return xBlock[index] = val;
    }); // loop to process 32 rounds crypt

    for (var i = 0; i < 32; i++) {
        xBlock[i + 4] = xBlock[i] ^ tTransform1(xBlock[i + 1] ^ xBlock[i + 2] ^ xBlock[i + 3] ^ roundKeys[i]);
    }

    var yBlock = [xBlock[35], xBlock[34], xBlock[33], xBlock[32]];
    return yBlock;
};

var padding = function padding(originalBuffer) {
    if (originalBuffer === null) {
        return null;
    }

    var paddingLength = UINT8_BLOCK - originalBuffer.length % UINT8_BLOCK;
    var paddedBuffer = new Array(originalBuffer.length + paddingLength);
    originalBuffer.forEach(function (val, index) {
        return paddedBuffer[index] = val;
    });

    // paddedBuffer.fill(paddingLength, originalBuffer.length); // IE 11 及更早版本不支持 fill() 方法

    for (var i = 0; i < paddingLength; i++) {
        originalBuffer.push(paddingLength)
    }
    paddedBuffer = originalBuffer;

    return paddedBuffer;
};

var dePadding = function dePadding(paddedBuffer) {
    if (paddedBuffer === null) {
        return null;
    }

    var paddingLength = paddedBuffer[paddedBuffer.length - 1];
    var originalBuffer = paddedBuffer.slice(0, paddedBuffer.length - paddingLength);
    return originalBuffer;
};

var check = function check(name, str) {
    if (!str || str.length != 16) {
        console.error("".concat(name, " should be a 16 bytes string."));
        return false;
    }

    return true;
};
/**
 * CBC加密模式
 * @example encrypt_cbc("1234", "1234567890123456", "1234567890123456") => "K++iI4IhSGMnEJZT/jv1ow=="
 * @param {any} plaintext 要加密的数据
 * @param {String} key
 * @param {String} iv
 * @param {String} mode base64 | "text"
 * @returns {String} 加密后的字符串
 */


var encrypt_cbc = function encrypt_cbc(plaintext, key, iv) {
    var mode = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : "base64";

    if (!check("iv", iv) && !check("key", key)) {
        return;
    }

    var encryptRoundKeys = EncryptRoundKeys(stringToArray(key));
    var plainByteArray = stringToArray(plaintext);
    var padded = padding(plainByteArray);
    var blockTimes = padded.length / UINT8_BLOCK;
    var outArray = []; // init chain with iv (transform to uint32 block)

    var chainBlock = getChainBlock(stringToArray(iv)); // console.log(padded, blockTimes, encryptRoundKeys, chainBlock);

    for (var i = 0; i < blockTimes; i++) {
        // extract the 16 bytes block data for this round to encrypt
        var roundIndex = i * UINT8_BLOCK;
        var block = getChainBlock(padded, roundIndex); // xor the chain block

        chainBlock[0] = chainBlock[0] ^ block[0];
        chainBlock[1] = chainBlock[1] ^ block[1];
        chainBlock[2] = chainBlock[2] ^ block[2];
        chainBlock[3] = chainBlock[3] ^ block[3]; // use chain block to crypt

        var cipherBlock = doBlockCrypt(chainBlock, encryptRoundKeys); // make the cipher block be part of next chain block

        chainBlock = cipherBlock;

        for (var l = 0; l < UINT8_BLOCK; l++) {
            outArray[roundIndex + l] = cipherBlock[parseInt(l / 4)] >> (3 - l) % 4 * 8 & 0xff;
        }
    } // cipher array to string

    if (mode === 'base64') {
        return base64js.fromByteArray(outArray);
    } else {
        // text
        return decodeURIComponent(escape(String.fromCharCode.apply(String, outArray)));
    }
};
/**
 * ECB加密模式
 * @example encrypt_ecb("1234", "1234567890123456") => "woPrxebr8Xvyo1qG8QxAUA=="
 * @param {any} plaintext 要加密的数据
 * @param {String} key
 * @param {String} iv
 * @param {String} mode base64 | "text"
 * @returns {String} 加密后的字符串
 */


var encrypt_ecb = function encrypt_ecb(plaintext, key) {
    var mode = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : "base64";

    // if (!check("iv", iv)) {
    //   return;
    // }

    var encryptRoundKeys = EncryptRoundKeys(stringToArray(key));
    var plainByteArray = stringToArray(plaintext);
    var padded = padding(plainByteArray);
    var blockTimes = padded.length / UINT8_BLOCK;
    var outArray = []; // CBC mode
    // init chain with iv (transform to uint32 block)

    for (var i = 0; i < blockTimes; i++) {
        // extract the 16 bytes block data for this round to encrypt
        var roundIndex = i * UINT8_BLOCK;
        var block = getChainBlock(padded, roundIndex);
        var cipherBlock = doBlockCrypt(block, encryptRoundKeys);

        for (var l = 0; l < UINT8_BLOCK; l++) {
            outArray[roundIndex + l] = cipherBlock[parseInt(l / 4)] >> (3 - l) % 4 * 8 & 0xff;
        }
    } // cipher array to string

    if (mode === 'base64') {
        return base64js.fromByteArray(outArray);
    } else {
        // text
        return decodeURIComponent(escape(String.fromCharCode.apply(String, outArray)));
    }
};
/**
 * CBC解密模式
 * @example decrypt_cbc("K++iI4IhSGMnEJZT/jv1ow==", "1234567890123456", "1234567890123456") => "1234"
 * @param {any} plaintext 要解密的数据
 * @param {String} key
 * @param {String} iv
 * @param {String} mode base64 | "text"
 * @returns {String} 解密后的字符串
 */


var decrypt_cbc = function decrypt_cbc(ciphertext, key, iv) {
    var mode = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : "base64";

    if (!check("iv", iv) && !check("key", key)) {
        return;
    } // get cipher byte array

    var cipherByteArray = null;
    var decryptRoundKeys = EncryptRoundKeys(stringToArray(key)).reverse();

    if (mode === 'base64') {
        // cipher is base64 string
        cipherByteArray = base64js.toByteArray(ciphertext);
    } else {
        // cipher is text
        cipherByteArray = stringToArray(ciphertext);
    }

    var blockTimes = cipherByteArray.length / UINT8_BLOCK;
    var outArray = []; // init chain with iv (transform to uint32 block)

    var chainBlock = getChainBlock(stringToArray(iv));
    // console.log(cipherByteArray, decryptRoundKeys, chainBlock);

    for (var i = 0; i < blockTimes; i++) {
        // extract the 16 bytes block data for this round to encrypt
        var roundIndex = i * UINT8_BLOCK; // make Uint8Array to Uint32Array block

        var block = getChainBlock(cipherByteArray, roundIndex); // reverse the round keys to decrypt

        var plainBlockBeforeXor = doBlockCrypt(block, decryptRoundKeys); // xor the chain block

        var plainBlock = [chainBlock[0] ^ plainBlockBeforeXor[0], chainBlock[1] ^ plainBlockBeforeXor[1], chainBlock[2] ^ plainBlockBeforeXor[2], chainBlock[3] ^ plainBlockBeforeXor[3]]; // make the cipher block be part of next chain block

        chainBlock = block;

        for (var l = 0; l < UINT8_BLOCK; l++) {
            outArray[roundIndex + l] = plainBlock[parseInt(l / 4)] >> (3 - l) % 4 * 8 & 0xff;
        }
    } // depadding the decrypted data

    var depaddedPlaintext = dePadding(outArray); // transform data to utf8 string

    return decodeURIComponent(escape(String.fromCharCode.apply(String, _toConsumableArray(depaddedPlaintext))));
};
/**
 * ECB解密模式
 * @example decrypt_ecb("woPrxebr8Xvyo1qG8QxAUA==", "1234567890123456") => "1234"
 * @param {any} plaintext 要解密的数据
 * @param {String} key
 * @param {String} mode base64 | "text"
 * @returns {String} 解密后的字符串
 */


var decrypt_ecb = function decrypt_ecb(ciphertext, key) {
    var mode = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : "base64";

    // if (!check("iv", iv)) {
    //   return;
    // }
    // get cipher byte array

    var decryptRoundKeys = EncryptRoundKeys(stringToArray(key)).reverse();
    var cipherByteArray = null;

    if (mode === 'base64') {
        // cipher is base64 string
        cipherByteArray = base64js.toByteArray(ciphertext);
    } else {
        // cipher is text
        cipherByteArray = stringToArray(ciphertext);
    }

    var blockTimes = cipherByteArray.length / UINT8_BLOCK;
    var outArray = [];

    for (var i = 0; i < blockTimes; i++) {
        // extract the 16 bytes block data for this round to encrypt
        var roundIndex = i * UINT8_BLOCK; // make Uint8Array to Uint32Array block

        var block = getChainBlock(cipherByteArray, roundIndex); // reverse the round keys to decrypt

        var plainBlock = doBlockCrypt(block, decryptRoundKeys);

        for (var l = 0; l < UINT8_BLOCK; l++) {
            outArray[roundIndex + l] = plainBlock[parseInt(l / 4)] >> (3 - l) % 4 * 8 & 0xff;
        }
    } // depadding the decrypted data

    var depaddedPlaintext = dePadding(outArray); // transform data to utf8 string

    return decodeURIComponent(escape(String.fromCharCode.apply(String, _toConsumableArray(depaddedPlaintext))));
};

function white(data) {
    return encrypt_ecb(data, "tiekeyuankp12306")
}

console.log(white('123456'));

