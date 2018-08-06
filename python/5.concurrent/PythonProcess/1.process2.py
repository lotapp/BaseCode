import os
from multiprocessing import Process


class My_Process(Process):
    # 重写了Proce类的Init方法
    def __init__(self, name):
        self.__name = name
        Process.__init__(self)  # 调用父类方法

    # 重写了Process类的run()方法
    def run(self):
        print("[子进程-%s]PID：%d，PPID：%d" % (self.__name, os.getpid(),
                                          os.getppid()))


def main():
    print("[父进程]PID：%d，PPID：%d" % (os.getpid(), os.getppid()))
    p = My_Process("萌萌哒")  # 如果不指定方法，默认调Run方法
    p.start()
    p.join()  # 父进程回收子进程资源（内部调用了wait系列方法）


if __name__ == '__main__':
    main()