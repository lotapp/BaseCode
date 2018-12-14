const fs = require("fs");

data = { "name": "小明", "age": "23" };
fs.writeFile("to.txt", data, ex => {
    if (ex) {
        console.log(ex);
    }
});

fs.readFile("to.txt", (ex, data) => {
    if (ex) {
        console.log(ex);
    } else {
        console.log(data);
        console.log(data.toJSON());
        console.log(data.toString());
        console.log(data.toLocaleString());
    }
});