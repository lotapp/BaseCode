const fs = require("fs");
const url = require("url");
const http = require("http");

http.createServer((request, response) => {
    let { pathname } = url.parse(request.url);
    console.log(pathname);
    let file_path = `www${pathname}`;

    let show_404 = () => {
        response.writeHeader(404);
        response.write("404 Not Found");
        response.end();
    }

    let write_html = (time) => {
        // 设置响应头
        response.setHeader("Last-Modified", time);
        // 读取文件并返回
        let rs = fs.createReadStream(file_path);
        rs.pipe(response);
        // 读取出错
        rs.on("error", ex => {
            show_404();
        });
    }

    // 获取请求文件的状态
    fs.stat(file_path, (ex, stats) => {
        if (ex) {
            show_404();
        } else {
            let client_time = request.headers["if-modified-since"];
            let time_GMT = stats.ctime.toGMTString();
            // 浏览器有页面缓存
            if (client_time) {
                console.log(client_time);
                // 文件状态时间没服务端新
                if (new Date(client_time) < stats.ctime) {
                    // 响应浏览器
                    write_html(time_GMT);
                } else {
                    // 重定向到浏览器本地缓存的文件
                    response.writeHeader(304);
                    response.end();
                }
            } else {
                write_html(time_GMT);
            }
        }
    }); // fs.stat 结束



}).listen(8080, () => {
    console.log("服务器已经启动，端口：8080");
});

// Expires：可以设置失效时间
// Expires: Sat, 15 Dec 2018 10:33:48 GMT

// Cache-Control：可以指定文件不缓存（有实时性和安全性的需求才考虑）
// Cache-Control: no-cache

// Request Header：浏览器发送给服务器的HTTP请求头标签
// if-modified-since: Sat, 15 Dec 2018 10:41:57 GMT

// Response Header：服务器响应客户端的HTTP请求头标签
// last-modified: Sat, 15 Dec 2018 10:41:21 GMT