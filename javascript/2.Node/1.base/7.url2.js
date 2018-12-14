const fs = require("fs");
const url = require("url");
const http = require("http");

// 创建服务
let server = http.createServer((request, response) => {
    // 请求
    // {a, b} = {a:21,b=34,c=22} 只要对应即可解包，如果想取别名可以使用：{a:xx, b} = {...}
    let { pathname, query } = url.parse(request.url, true);
    console.log(query, pathname);

    // 读取对应文件
    fs.readFile(`www${pathname}`, (ex, data) => {
        if (ex) {
            // 返回404状态码，并设置编码为UTF-8
            response.writeHeader(404, {
                "Content-Type": "text/html;charset=utf-8"
            });
            // 提示需要在 writeHeader 之后，不然访问的是浏览器404页面
            response.write("<h1>访问的页面不存在～</h1>");
        } else {
            response.write(data);
        }
        // 响应结束
        response.end();
    });
});
// 服务器启动并监听指定端口
server.listen(8080);