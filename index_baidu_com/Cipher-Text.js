const CryptoJS = require("crypto-js");
const encrypt = (word, k, i) => {
    var key = CryptoJS.enc.Utf8.parse(k ? k : "guusaiaaqkqqaawu");
    var iv = CryptoJS.enc.Utf8.parse(i ? i : "1234567887654321");
    let srcs = CryptoJS.enc.Utf8.parse(word);
    let encrypted = CryptoJS.AES.encrypt(srcs, key, {
        iv: iv, mode: CryptoJS.mode.CBC, padding: CryptoJS.pad.Pkcs7
    });
    // return encrypted.ciphertext.toString().replace("\n", "");
    return encrypted.toString().replace("\n", "");
}

function white_encrypt(info) {
    return info["timeStamp"] + info["text"]["clientTs"] + "_" + encrypt(JSON.stringify(info["text"]), info["key"], info["iv"])
}

// 测试用例
// var info = {
//     'text': {
//         'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
//         'url': 'https://index.baidu.com/v2/main/index.html#/trend/python?words=python',
//         'platform': 'Win32',
//         'clientTs': 1670245897141,
//         'version': '1.0.0.5'
//     }, 'timeStamp': '1670223943370_', 'key': 'guusaiaaqkqqaawu', 'iv': '1234567887654321'
// }
// 正确结果
// 1670223943370_1670245897141_ah1FYfCV2eybsyHk8F9OTr/ATPp3UTWmDFaNOqji53jPvPkIppyR/vUjpX19GjoYQsXeXxHtypGQs+6pdIApwzxc9biVuHh81hBQV45PWv0CafKZJkzqHJcuCNxSpxd6z9aoaIeqgxD3eU4hk9Z+K8nc50hBrVajMZTeOwrYsXaeiIU4iEgX7rP/nJ0Dijew0LBuJgia2wWjYH8dC1Bs8U+WrYVMzXj4A49wFrl15nxveAhEJcAZTrbgOQglFlekvJY/lRhxLmg1DR2dHKCQ/PLAknZB9C77TJlT8Lxt90BxLkf4NO6rsdEYav0J3UNPif5iRQNiB0IJPSyNR6XmgwiQveqxkP0/Fz1FMcr00zo=
