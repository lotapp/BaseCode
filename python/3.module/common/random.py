# 简单验证码的例子
import random


def get_code(n):
    """简单验证码"""
    code = ""
    for i in range(n):
        s1 = chr(random.randint(65, 90))  # 字母
        s2 = str(random.randint(0, 9))  # 数字
        code += random.choice([s1, s2])  # 随机返回s1 or s2
    return code


def main():
    print(get_code(4))


if __name__ == '__main__':
    main()
