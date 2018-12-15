const os = require("os");
const http = require("http");
const process = require("process");
const cluster = require("cluster");

// 主进程：分配任务
if (cluster.isMaster) {
    console.log(`主进程PID：${process.pid}`);
    for (let i = 0; i < os.cpus().length; i++) {
        cluster.fork();
    }
} else {
    // 子进程执行任务
    http.createServer((request, response) => {
        console.log(`当前进程PID：${process.pid}，父进程PPID：${process.ppid}`);
        response.write("Fork Test");
        response.end();
    }).listen(8080, () => {
        console.log(`服务器启动成功，当前端口：8080，进程PID：${process.pid}`);
    });
}