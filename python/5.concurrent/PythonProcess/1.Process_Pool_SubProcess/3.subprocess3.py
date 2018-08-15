import subprocess


def main():
    # ps aux | grep bash
    # 进程1获取结果
    p1 = subprocess.Popen(["ps", "-aux"], stdout=subprocess.PIPE)
    # 得到进程1的结果再进行筛选
    p2 = subprocess.Popen(["grep", "bash"], stdin=p1.stdout, stdout=subprocess.PIPE)
    # 关闭写段（结果已经获取到进程2中了，防止干扰显示）
    p1.stdout.close()
    # 与流程交互：将数据发送到stdin并关闭它。
    msg_tuple = p2.communicate()
    # 输出结果
    print(msg_tuple[0].decode())


if __name__ == '__main__':
    main()