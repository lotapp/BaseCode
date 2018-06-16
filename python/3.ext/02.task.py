#!/usr/bin/env python3

import os
import time

while True:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(600)
    os.system("notify-send 友情提醒 10分钟过去了")

# Ubuntu下的定时提醒