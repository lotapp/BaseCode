const url = require("url");
const http = require("http");

// 创建服务
let server = http.createServer((request, response) => {
    // 请求
    // {a, b} = {a:21,b=34,c=22} 只要对应即可解包，如果想取别名可以使用：{a:xx, b} = {...}
    let { pathname, query } = url.parse(request.url, true);
    console.log(query, pathname);
    
    // 响应
    response.write("<h1>test</h1>");
    response.end();
});
// 服务器启动并监听指定端口
server.listen(8080);