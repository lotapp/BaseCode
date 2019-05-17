# PySnooper
import functools
import pysnooper


# 分析整个代码
@pysnooper.snoop()
def sum(args):
    return functools.reduce(lambda x, y: x + y, args)

def avg(args):
    # return sum(args) / len(args)
    sum_num = sum(args)
    # 分析片段代码
    with pysnooper.snoop():
        avg_num = sum_num / len(args)
    return avg_num


if __name__ == "__main__":
    print("-" * 30)
    # 求和
    sum_num = sum(list(range(1, 101)))
    print(sum_num)
    print("-" * 30)
    # 平均值
    avg_num = avg(list(range(1, 101)))
    print(avg_num)

# $ pip install pysnooper
# Collecting pysnooper
#   Downloading https://files.pythonhosted.org/packages/73/c3/d097f46b47d7db4097f16df6f292b9d52b978a8c3108aea8d13495c9bc76/PySnooper-0.0.35-py2.py3-none-any.whl
# Installing collected packages: pysnooper
# Successfully installed pysnooper-0.0.35
