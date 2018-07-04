# 导入matplotlib的pyplot模块
import matplotlib.pyplot as plt


def main():

    x_list = list(range(1, 11))
    y_list = [y * 2 + 1 for y in x_list]

    print(x_list)
    print(y_list)

    # 画图
    plt.plot(x_list, y_list)
    # 设置X，Y的坐标区间（可以不设置，用默认显示方式）
    plt.axis([0, 10, 0, 25])
    # 显示图片
    plt.show()


if __name__ == '__main__':
    main()