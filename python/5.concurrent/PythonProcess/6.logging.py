import logging
from multiprocessing import Process, log_to_stderr


def test():
    print("test")


def start_log():
    # 把日记输出定向到sys.stderr中
    logger = log_to_stderr()
    # 设置日记记录级别
    # 敏感程度：DEBUG、INFO、WARN、ERROR、CRITICAL
    print(logging.WARN == logging.WARNING)  # 这两个是一样的
    level = logging.INFO
    logger.setLevel(level)  # 设置日记级别(一般都是WARN)

    # 自定义输出
    # def log(self, level, msg, *args, **kwargs):
    logger.log(level, "我是通用格式")  # 通用，下面的内部也是调用的这个
    logger.info("info 测试")
    logger.warning("warning 测试")
    logger.error("error 测试")


def main():
    start_log()
    # 做的操作都会被记录下来
    p = Process(target=test)
    p.start()
    p.join()


if __name__ == '__main__':
    main()
