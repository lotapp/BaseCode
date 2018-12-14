const fs = require("fs");

// readFile("xxx",call_back(err,data))
fs.readFile("test.txt", (ex, data) => {
    if (ex) {
        console.log("读取错误：", ex);

        // 不存在我就创建一个文件 writeFile("xxx", "内容", call_back(err))
        fs.writeFile("test.txt", "mmd", ex => {
            if (ex) {
                console.log("写入错误：", ex);
            }
        });
    } else {
        // 没有错误就输出
        console.log(data.toString());
    }
});

console.log("[ReadFile异步验证]我出现就是异步");

// ------------------------------------------------
// 追加写入 appendFile("xxx",call_back(err))
fs.appendFile("test.txt", "我是小明", ex => {
    if (ex) {
        console.log(ex);
    } else {
        // 没错误就看看test.txt的内容
        fs.readFile("test.txt", (ex, data) => {
            if (ex) {
                console.log("读取错误：", ex);
            } else {
                console.log(data.toString());
            }
        });
    }
});

// ------------------------------------------------
// PS：如果文件不是文本文件，就不能toString了
fs.readFile("知识星球.png", (ex, data) => {
    if (ex) {
        console.log("读取错误：", ex);
    } else {
        console.log(data); // 看看buffer是啥样的
        fs.writeFile("test.png", data, ex => {
            if (ex) {
                console.log("复制错误：", ex);
            }
        });
    }
});