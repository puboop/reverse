const CryptoJS = require("crypto-js");
function encryptByAES(message){
    var key = "u2oh6Vu^HWe4_AES";
	let CBCOptions = {
		iv: CryptoJS.enc.Utf8.parse(key),
		mode:CryptoJS.mode.CBC,
		padding: CryptoJS.pad.Pkcs7
	};
	let aeskey = CryptoJS.enc.Utf8.parse(key);
	let secretData = CryptoJS.enc.Utf8.parse(message);
	let encrypted = CryptoJS.AES.encrypt(
		secretData,
		aeskey,
		CBCOptions
	);
	return CryptoJS.enc.Base64.stringify(encrypted.ciphertext);
}
function white(data){
    return encryptByAES(data);
}
// 测试用例
// console.log(white("123456"));
