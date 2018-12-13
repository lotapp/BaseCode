const path = require("path");

let file_name = "/images/png/小明.png";


// 文件路径 /images/png
console.log(path.dirname(file_name));

// 提取出用 `/` 隔开的 `path` 的最后一部分
// 小明.png
console.log(path.basename(file_name));

// 文件后缀 .png
console.log(path.extname(file_name));

// 文件信息 {root: "/", dir: "/images/png", base: "小明.png", ext: ".png", name: "小明"}
console.log(path.parse(file_name));

// ------------------------------
// 当前文件所在文件夹绝对路径
console.log(path.resolve());
// 文件的绝对路径
console.log(path.resolve(file_name));

// console.log(path);