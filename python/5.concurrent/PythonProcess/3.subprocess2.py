import time
import subprocess


def main():
    process = subprocess.Popen(
        ["ipython3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    try:
        # 对pstree进行交互
        out, err = process.communicate(input=b'print("hello")', timeout=3)
        print("Out:%s\nErr:%s" % (out.decode(), err.decode()))
    except TimeoutError:
        # 如果超时到期，则子进程不会被终止，需要自己处理一下
        process.kill()
        out, err = process.communicate()
        print("Out:%s\nErr:%s" % (out.decode(), err.decode()))
    # time.sleep(10)


if __name__ == '__main__':
    main()
