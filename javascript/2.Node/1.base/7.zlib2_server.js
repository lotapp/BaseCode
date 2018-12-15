const fs = require("fs");
const zlib = require("zlib");
const http = require("http");

let server = http.createServer((request, response) => {
    // let { pathname } = url.parse(request.url);
    console.log(request.url);
    let rs = fs.createReadStream(`www${request.url}`);
    let gz = zlib.createGzip();

    // 响应之前告诉浏览器是gzip的格式
    response.setHeader("Content-Encoding", "gzip");
    // 返回gzip压缩后的文件
    rs.pipe(gz).pipe(response);

    // 读取失败，404错误
    rs.on("error", ex => {
        response.removeHeader("Content-Encoding");
        // 返回404状态码，并设置编码为UTF-8
        response.writeHeader(404, {
            "Content-Type": "text/html;charset=utf-8"
        });
        // 提示需要在 writeHeader 之后，不然访问的是浏览器404页面
        response.write("<h2>您访问的页面不存在～</h2>");
        response.end();
    });
});

server.listen(8080, () => {
    console.log("服务器启动成功,端口：8080");
});