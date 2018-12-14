const fs = require("fs");
const url = require("url");
const http = require("http");

let server = http.createServer((request, response) => {
    let { pathname } = url.parse(request.url, true);
    console.log(pathname);

    let rs = fs.createReadStream(`www${pathname}`);
    // `request`和`response`就是一个典型的读写流（`ReadStream`、`WriteStream`）
    rs.pipe(response);
    
    // 读取完毕 ==> 本次相应结束
    rs.on("end", () => {
        response.end();
    });
    
    // 读取失败 ==> 404
    rs.on("error", ex => {
        response.writeHeader(404);
        response.write("404 Not Found");
        response.end();
    });
});

server.listen(8080);