const fs = require("fs");

fs.stat("www/test.html", (ex, status) => {
    if (ex) {
        console.log(ex);
    } else {
        // ctime：状态时间
        console.log(status.ctime);
        console.log(status.ctime.toUTCString());
    }
});