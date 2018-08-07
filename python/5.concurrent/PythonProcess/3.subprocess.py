import subprocess


def main():
    # os.execlp("ls", "ls", "-al")  # 执行Path环境变量可以搜索到的命令
    result = subprocess.run(["ls", "-al"])
    print(result)


if __name__ == '__main__':
    main()
