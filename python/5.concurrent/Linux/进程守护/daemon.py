import os
import time
import signal
from sys import stdin, stdout, stderr


class Daemon(object):
    def __init__(self, p_name, p_script):
        self.p_name = p_name
        self.p_script = p_script

    @staticmethod
    def write_log(msg):
        # 追加方式写
        with open("info.log", "a+") as f:
            f.write(msg)
            f.write("\n")

    def is_running(self, p_name):
        """是否在运行"""
        try:
            # grep -v grep 不显示grep本身，wc -l是计数用的
            result = os.popen(
                "ps ax | grep %s | grep -v grep" % p_name).readlines()
            if len(result) > 0:
                return True
            else:
                return False
        except Exception as ex:
            self.write_log(ex)
            return False

    def is_restart(self, p_script):
        """重启程序"""
        try:
            if os.system(p_script) == 0:
                return True
            else:
                return False
        except Exception as ex:
            self.write_log(ex)
            return False

    def heartbeat(self, signalnum, frame):
        """心跳检查"""
        if not self.is_running(self.p_name):
            self.write_log("[%s]程序(%s)已挂，准备重启" % (time.strftime("%Y-%m-%d %X"),
                                                  self.p_name))
            if not self.is_restart(self.p_script):
                self.is_restart(self.p_script)  # 再给一次机会

    def run(self):
        """运行守护进程"""
        pid = os.fork()
        if pid > 0:
            exit(0)

        os.setsid()  # 子进程创建新会话
        os.chdir("/home/dnt")  # 改变当前工作目录
        os.umask(0)  # 获取777权限

        # 5. 关闭文件描述符
        os.close(stdin.fileno())
        os.close(stdout.fileno())
        os.close(stderr.fileno())

        # 【必须】6. 自己的逻辑代码
        # 捕捉设置的定时器
        signal.signal(signal.SIGALRM, self.heartbeat)
        # 第一次2s后执行，以后5s执行一次
        signal.setitimer(signal.ITIMER_REAL, 2, 5)

        self.write_log("[%s]daeman running" % time.strftime("%Y-%m-%d %X"))
        self.write_log("p_name:%s，p_script:%s" % (self.p_name, self.p_script))

        while True:
            time.sleep(5)  # 不用担心影响signal（优先级别高）


def main():
    try:
        pro = Daemon("test.py", "python3 ~/demo/test.py")
        pro.run()
    except Exception as ex:
        Daemon.write_log(ex)


if __name__ == '__main__':
    main()
