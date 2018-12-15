const fs = require("fs");

fs.stat("www/test.html", (ex, stats) => {
    if (ex) {
        console.log(ex);
    } else {
        // mtime：最后一次修改时间
        console.log(stats.mtime);
        
        // UTC：世界统一时间：GMT ==> UTC
        console.log(stats.mtime.toUTCString());
        console.log(stats.mtime.toGMTString());
    }
});