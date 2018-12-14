const fs = require("fs");
const zlib = require("zlib");

// 读写流
let gz = zlib.createGzip();
// 读流
let rs =fs.createReadStream("./www/jquery-2.1.1.js");
// 写流
let ws =fs.createWriteStream("test.js.gz");
// 可以这么理解：（gz是读写流）
// rs水龙头先传给了gz，gz又当一个水龙头传给了ws
rs.pipe(gz).pipe(ws);

ws.on("finish",()=>{
    console.log("写入完毕");
});