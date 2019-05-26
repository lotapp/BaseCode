# https://baike.baidu.com/item/%E5%B9%B2%E6%94%AF%E5%8E%86/9386578
# https://jingyan.baidu.com/article/fec7a1e5e7203b1190b4e7f5.html
# https://jingyan.baidu.com/article/46650658326555f549e5f8ae.html

class Almanac(object):
    """定义一个老黄历类"""

    def __init__(self):
        # 天干映射集合
        self.sky_dict = {
            1: ("甲", "木", "阳"),
            2: ("乙", "木", "阴"),
            3: ("丙", "火", "阳"),
            4: ("丁", "火", "阴"),
            5: ("戊", "土", "阳"),
            6: ("己", "土", "阴"),
            7: ("庚", "金", "阳"),
            8: ("辛", "金", "阴"),
            9: ("壬", "水", "阳"),
            0: ("癸", "水", "阴")
        }
        # 地支映射集合
        # 我画了个中医的对应图：https://github.lesschina.com/life/doctor/now/images/12sc.png
        self.animal_dict = {
            1: ("子", "鼠", "水", "阳"),  # 23~01
            2: ("丑", "牛", "土", "阴"),  # 01~03
            3: ("寅", "虎", "木", "阳"),  # 03~05
            4: ("卯", "兔", "木", "阴"),  # 05~07
            5: ("辰", "龙", "土", "阳"),  # 07~09
            6: ("巳", "蛇", "火", "阴"),  # 09~11
            7: ("午", "马", "火", "阳"),  # 11~13
            8: ("未", "羊", "土", "阴"),  # 13~15
            9: ("申", "猴", "金", "阳"),  # 15~17
            10: ("酉", "鸡", "金", "阴"),  # 17~19
            11: ("戌", "狗", "土", "阳"),  # 19~21
            0: ("亥", "猪", "水", "阴")  # 21~23
        }

    def __get_sky_num(self, year):
        """根据year获取天干对应的编号"""
        # 年份 - 3 再取余 10
        return (year - 3) % 10

    # PS：年数减3，是因为公元4年恰好是甲子年，从公元4年起，就要减去公元4年前的3年（都是从公元4年开始往后算的）
    def __get_animal_num(self, year):
        """根据year获取地支或者生肖对应的编号"""
        # 年份 - 3 再取余 12
        return (year - 3) % 12

    def __get_sky(self, num):
        """根据num获取天干"""
        return self.sky_dict.get(num)

    def __get_animal(self, num):
        """根据num获取地支和生肖"""
        return self.animal_dict.get(num)

    def year_to_sky(self, year):
        """通过年份获取天干"""
        return self.__get_sky(self.__get_sky_num(year))

    def year_to_animal(self, year):
        """通过年份获取生肖或者地支"""
        return self.__get_animal(self.__get_animal_num(year))

    def mon_to_word(self, year, mon):
        """根据年份的天干和阴历月份来获取八字；参数：该年的天干，该月"""
        # 月份对应的第一个八字：（2*天干编号 + 月份）% 10
        one_num = (2 * self.__get_sky_num(year) + mon) % 10
        # 月份对应的第二个八字：(月份 + 2) % 12
        two_num = (mon + 2) % 12
        # 返回某年下月份的八字元组
        return f"{self.__get_sky(one_num)[0]}{self.__get_animal(two_num)[0]}"


def main():
    # 1.范围测试
    almanac = Almanac()
    for n in range(2004, 2030):
        skys = almanac.year_to_sky(n)
        animals = almanac.year_to_animal(n)
        print(
            f"\n{n}年(阴历)：{skys[0]}{animals[0]}年({animals[1]}年)、五行：{skys[2]}之{skys[1]}"
        )
        for m in range(1, 13):
            print(f"{m}月(阴历)：{almanac.mon_to_word(n, m)}月")

    # 2.随机测试
    import random
    for _ in range(10):
        year = random.randint(1980, 2020)
        mon = random.randint(1, 12)
        skys = almanac.year_to_sky(year)
        animals = almanac.year_to_animal(year)
        print(
            f"\n{year}年(阴历)：{skys[0]}{animals[0]}年({animals[1]}年)、五行：{skys[2]}之{skys[1]}"
        )
        # 根据年份的天干和阴历月份来获取八字
        mons = almanac.mon_to_word(year, mon)
        print(f"{mon}月(阴历)：{mons}")


if __name__ == "__main__":
    main()
