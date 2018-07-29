import os
import time
import signal



signal.signal(signal.SIGALRM, signal.SIG_IGN)
signal.pause()  # 设置一个进程到休眠状态直到接收一个信号
# signal.signal(signal.SIGKILL, signal.SIG_IGN)  # Kill 9 pid 只能抵挡一次


# 等待信号，有信号发生时则调用信号处理程序
while (1):
    # 添加要阻塞的信号

    time.sleep(1)
# 读取当前进程未决信号集
# pendset = signal.sigpending()
# print(pendset)  # 默认没有屏蔽
# for item in pendset:
#     print(item)

# signal.alarm(1) # 设置定时器

# i = 0
# while True:
#     print("%d" % i)
#     i += 1
# # signal.pthread_kill(os.getpgid(),)  # 杀死线程

# 发送信号：os.kill(pid, sig)
# os.kill(os.getppid(), signal.SIGKILL)  # 相当于kill 9 pid（sigkill）
# os.abort()  # 给自己发异常终止信号
# # raise
# # 【不受进程影响，每个进程只能有一个定时器，再设置只是重置】
# signal.alarm(3)  # 设置终止时间（3s），然后终止进程（sigalrm）
# signal.setitimer()  # 设置定时器
