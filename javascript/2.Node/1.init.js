// ES6语法：import http from "http"; （现在还没能完全支持）
const http = require("http")

let server = http.createServer((request, response) => {
    // 每次请求都会执行这个方法
    console.log(request.url);

    response.write("<h1>Test NodeJS</h>");
    response.end() // 告诉浏览器响应结束

});

server.listen(8080); // 这个和其他语言不一样，直接监听对应的端口