const cypto = require("crypto");

let obj = cypto.createHash("md5");
// // PS：分多次提交也一样：
// obj.update("123");
// obj.update("456");
obj.update("123456");
// e10adc3949ba59abbe56e057f20f883e
console.log(obj.digest("hex"));

let obj2 = cypto.createHash("sha1"); //cypto.createHash("sha256");
obj2.update("123456");
// 7c4a8d09ca3762af61e59520943dc26494f8941b
// 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
console.log(obj2.digest("hex"));