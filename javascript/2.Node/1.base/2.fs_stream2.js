const fs = require("fs");

let rs = fs.createReadStream("知识星球.png");
let ws = fs.createWriteStream("test.png");
rs.pipe(ws); // 创建一个管道，流从r端到w端

// 可以理解为错误触发的事件
// 处理流事件 --> data, end, error
rs.on("error", ex => {
    console.log("读取失败", ex);
});

rs.on("end", () => {
    console.log("读取完成");
});

ws.on("error", ex => {
    console.log("写入失败", ex);
});
// 注意，写入流完成不叫end
ws.on("finish", () => {
    console.log("写入完成");
});