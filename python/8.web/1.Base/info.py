# # 路由的功能
# # 伪静态实现
# # 正则版路由
# # 增删改查系
# # 日志相关系

# import urllib

# # url编码
# result = urllib.parse.quote("http://www.test.com/wd=逸鹏说道")
# print(result)

# # url解码
# new_result = urllib.parse.unquote(result)
# print(new_result)

# # 把键值对编码为url查询字符串
# result = urllib.parse.urlencode({"wd": "逸鹏说道"})
# print(result)

# # url解码
# new_result = urllib.parse.unquote(result)
# print(new_result)

# # 正文编码
# input_str = "<script>aleter('x xx x');</script>"

# # 正文解码

# # ---

# # logging
import logging

# # 1.控制台输出
# # 默认是 logging.WARNING
# # asctime：时间，文件名：filename，行号：lineno，级别：levelname，消息：message
# logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

# logging.debug("debug logging")
# logging.info("info logging")
# logging.warning("warning logging")
# logging.error("error logging")
# logging.critical("critical logging")

# 2.文件写入
import time
logging.basicConfig(level=logging.INFO,filename=f"{time.strftime('%Y-%m-%d',time.localtime())}.log",filemode="a+",format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

logging.debug("debug logging")
logging.info("info logging")
logging.warning("warning logging")
logging.error("error logging")
logging.critical("critical logging")
