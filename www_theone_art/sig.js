const CryptoJS = require("crypto-js");
window = global;
window.deciphering = function (e, t) {
    t = t || 32;
    var a = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
        , n = a.length;
    for (let c = 0; c < t; c++)
        a.charAt(Math.floor(Math.random() * n));
    return e
}
window.e = "4tBlCLWFZ3eD93CvDE2lpw=="
window.d = "5opkytHOggKj5utjZOgszg=="

// 加密
function encrypt(t, a) {
    var key = CryptoJS.enc.Base64.parse(e);
    let word = JSON.stringify({
        id: t.substr(0, t.length - 1),
        sum: a
    });
    let srcs = CryptoJS.enc.Utf8.parse(word);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}

// 解密
function tripleAesDecrypt(srcs) {
    var key = CryptoJS.enc.Base64.parse(d);
    let dataresult = CryptoJS.AES.decrypt(srcs, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    }).toString(CryptoJS.enc.Utf8)
        , dataResultFun = dataresult.split(",")[0].substr(4)
        , dataResultId = dataresult.split(",")[1].split("=")[1]
        , sigresult = eval(dataResultFun);
    sigData = encrypt(dataResultId, sigresult)
    return sigData
}

// 测试用例
// var srcs = 'truiLeKm7AKyuie+33QCYXJuXc32vhWjvkQn2l3Z6YqeVHDS68uSuIdsQ7/BbGuzdkRQHmRUiLBjgUKIpwI5g5AFMHngY6I9MLDmSgQ4F6dhW2UCotDRo0gDayBnXNKzJhkZTK0QxlinmU60CGhpP8LJjogP0706HUurTmTC/a8/NnglN/krLc9v1ES/+nyGjKYK7nhs+QQiKkI84Eu7IQ=='
// console.log(tripleAesDecrypt(srcs));
