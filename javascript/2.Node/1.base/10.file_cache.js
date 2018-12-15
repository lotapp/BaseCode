const fs = require("fs");
const url = require("url");
const http = require("http");

http.createServer((request, response) => {
    let { pathname } = url.parse(request.url);
    let file_path = `www${pathname}`;
    console.log(pathname);

    // 提炼一个404响应方法
    let write_404 = () => {
        response.writeHeader(404);
        response.write("404 Not Found");
        response.end();
    }

    // 文件状态
    fs.stat(file_path, (ex, stats) => {
        if (ex) {
            write_404();
        } else {
            // 封装一个正常响应的方法
            let write_html = () => {
                // 不管啥情况，反正要返回`Last-Modified`
                response.setHeader("Last-Modified", stats.mtime.toUTCString());
                var rs = fs.createReadStream(file_path);
                rs.pipe(response);

                // 文件读取如果出错，就返回404
                rs.on("error", ex => {
                    write_404();
                });
            }

            // 看看浏览器有没有发送`If-Modified-Since`的请求头
            // 必须小写，不然不能解析（接口是小写）
            // console.log(req.headers['If-Modified-Since']);
            // console.log(req.headers['if-modified-since']);
            let client_time = request.headers["if-modified-since"];
            // 说明之前访问过，现在是浏览器再次请求
            if (client_time) {
                // 易错：比较毫秒（getTime）会有问题，转换成`秒`并取整（Math.floor:返回小于或等于其数值参数的最大整数）
                client_time = Math.floor(new Date(client_time).getTime() / 1000);
                let server_time = Math.floor(stats.mtime.getTime() / 1000);
                // 如果页面修改过
                if (server_time > client_time) {
                    console.log("页面修改过");
                    write_html();
                } else {
                    console.log("304");
                    // 没有修改就返回304，让浏览器读本地文件
                    response.writeHeader(304);
                    response.end();
                }
            } else {
                // 正常的页面请求（200）
                console.log("200");
                write_html();
            }
        }
    });
}).listen(8080, () => {
    console.log("服务器成功启动，端口：8080");
});

// Request Header：浏览器发送给服务器的HTTP请求头标签
// `If-Modified-Since`: Sat, 15 Dec 2018 10:41:57 GMT
// `If-Modified-Since`是一个条件式请求首部，服务器只在所请求的资源在给定的日期时间之后对内容进行过修改的情况下才会将资源返回(状态码为200)
// 如果请求的资源从那时起未经修改，那么返回一个不带有消息主体的304响应，而在`Last-Modified`首部中会带有上次修改时间

// Response Header：服务器响应客户端的HTTP请求头标签
// Last-Modified: Sat, 15 Dec 2018 10:41:21 GMT

// Expires：可以设置失效时间
// Expires: Sat, 15 Dec 2018 10:33:48 GMT

// https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Caching_FAQ
// Cache-Control：可以指定文件不缓存（有实时性和安全性的需求才考虑）
// Cache-Control: no-cache