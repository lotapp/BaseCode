const fs = require("fs");

let rs = fs.ReadStream("知识星球.png");
let ws = fs.WriteStream("test.png");
// 可以这么理解，rs是水龙头防水的地方，写反了也就出不了水了
rs.pipe(ws); // 创建一个管道，流从r端到w端