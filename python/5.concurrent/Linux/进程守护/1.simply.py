import os
import time
import signal


def write_log(msg):
    pass


def is_running(p_name):
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
        write_log(ex)
        return False


def is_restart(p_script):
    """重启程序"""
    try:
        if os.system(p_script) == 0:
            return True
        else:
            return False
    except Exception as ex:
        write_log(ex)
        return False


def heartbeat(signalnum, addr):
    """心跳检查"""
    p_name = "test.py"
    p_script = "python3 ./test.py"

    if not is_running(p_name):
        print("程序(%s)已挂，准备重启" % p_name)
        if not is_restart(p_script):
            is_restart(p_script)  # 再给一次机会


def main():

    # 信号处理
    signal.signal(signal.SIGALRM, heartbeat)
    # 第一次1s后检查，以后每5s检查一次
    signal.setitimer(signal.ITIMER_REAL, 1, 5)

    while True:
        time.sleep(5)  # 不用担心影响signal（优先级别高）


if __name__ == '__main__':
    main()