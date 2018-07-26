import os


def main():
    pid = os.fork()
    if pid == 0:
        # 第二个参数不能为None,，第一个路径为绝对路径 eg：os.execl("/bin/ls"," ")
        os.execl("/bin/ls", "ls", "-al")
        # os.execlp("ls", "ls", "-al")  # 执行Path环境变量可以搜索到的命令
        print("exec函数族会替换代码，我是不会被执行的，除非上面的出问题了")

    print("-" * 10)  # 父进程执行一次，子进程不会执行


if __name__ == '__main__':
    main()