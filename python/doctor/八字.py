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
        self.earth_dict = {
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
        
        # 农历数据（农历1900-2100的润大小信息表）
        self.moon_year_list = [
            0x04bd8, 0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950, 0x16554, 0x056a0, 0x09ad0, 0x055d2,  # 1900-1909
            0x04ae0, 0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540, 0x0d6a0, 0x0ada2, 0x095b0, 0x14977,  # 1910-1919
            0x04970, 0x0a4b0, 0x0b4b5, 0x06a50, 0x06d40, 0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970,  # 1920-1929
            0x06566, 0x0d4a0, 0x0ea50, 0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950,  # 1930-1939
            0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, 0x092d0, 0x0d2b2, 0x0a950, 0x0b557,  # 1940-1949
            0x06ca0, 0x0b550, 0x15355, 0x04da0, 0x0a5b0, 0x14573, 0x052b0, 0x0a9a8, 0x0e950, 0x06aa0,  # 1950-1959
            0x0aea6, 0x0ab50, 0x04b60, 0x0aae4, 0x0a570, 0x05260, 0x0f263, 0x0d950, 0x05b57, 0x056a0,  # 1960-1969
            0x096d0, 0x04dd5, 0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250, 0x0d558, 0x0b540, 0x0b6a0, 0x195a6,  # 1970-1979
            0x095b0, 0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46, 0x0ab60, 0x09570,  # 1980-1989
            0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58, 0x05ac0, 0x0ab60, 0x096d5, 0x092e0,  # 1990-1999
            0x0c960, 0x0d954, 0x0d4a0, 0x0da50, 0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5,  # 2000-2009
            0x0a950, 0x0b4a0, 0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, 0x0a5b0, 0x15176, 0x052b0, 0x0a930,  # 2010-2019
            0x07954, 0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260, 0x0ea65, 0x0d530,  # 2020-2029
            0x05aa0, 0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0, 0x1d0b6, 0x0d250, 0x0d520, 0x0dd45,  # 2030-2039
            0x0b5a0, 0x056d0, 0x055b2, 0x049b0, 0x0a577, 0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0,  # 2040-2049
            0x14b63, 0x09370, 0x049f8, 0x04970, 0x064b0, 0x168a6, 0x0ea50, 0x06b20, 0x1a6c4, 0x0aae0,  # 2050-2059
            0x0a2e0, 0x0d2e3, 0x0c960, 0x0d557, 0x0d4a0, 0x0da50, 0x05d55, 0x056a0, 0x0a6d0, 0x055d4,  # 2060-2069
            0x052d0, 0x0a9b8, 0x0a950, 0x0b4a0, 0x0b6a6, 0x0ad50, 0x055a0, 0x0aba4, 0x0a5b0, 0x052b0,  # 2070-2079
            0x0b273, 0x06930, 0x07337, 0x06aa0, 0x0ad50, 0x14b55, 0x04b60, 0x0a570, 0x054e4, 0x0d160,  # 2080-2089
            0x0e968, 0x0d520, 0x0daa0, 0x16aa6, 0x056d0, 0x04ae0, 0x0a9d4, 0x0a2d0, 0x0d150, 0x0f252,  # 2090-2099
            0x0d520]  # 2100
        
        # 范围里面的最小年和最大年（不在这个范围内的数据不准）
        self.min_year, self.max_year = 1900, 2100

        # 阳历正常情况下每个月的天数
        # self.sun_mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __get_sky_num(self, year):
        """根据年份获取天干编号"""
        # 根据year获取天干对应的编号
        return (year - 3) % 10  # 年份 - 3 再取余 10

    def year_to_sky(self, year):
        """通过年份获取天干"""
        num = self.__get_sky_num(year)
        return self.sky_dict.get(num)

    def year_to_earth(self, year):
        """通过年份获取生肖或者地支"""
        # 根据year获取地支或者生肖对应的编号
        num = (year - 3) % 12  # 年份 - 3 再取余 12
        return self.earth_dict.get(num)

    def __mon_to_word(self, year, mon):
        """根据年份的天干和阴历月份来获取八字；参数：该年，该月"""
        # 月份对应的第一个八字：（2*天干编号 + 月份）% 10
        one_num = (2 * self.__get_sky_num(year) + mon) % 10  # 天干编号
        # 月份对应的第二个八字：(月份 + 2) % 12
        two_num = (mon + 2) % 12  # 地支编号
        # 返回某年下月份的八字元组
        return f"{self.sky_dict.get(one_num)[0]}{self.earth_dict.get(two_num)[0]}"

    def print_words(self, year, mon):
        """获取年月的八字+年五行和命格"""
        skys = self.year_to_sky(year)
        earths = self.year_to_earth(year)
        mons = self.__mon_to_word(year, mon)
        return f"{year}年(阴历)：{skys[0]}{earths[0]}年【{earths[1]}年】\n{mon}月：{mons}月\n五行：{skys[2]}之{skys[1]}、命格：{skys[1]}{earths[1]}命"

    def is_leap_year(self, year):
        """根据阳历年份查询是否是闰年"""
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
    def __get_moon_year_data(self, year):
        """获取阴历数据的头、中间、尾"""
        # 把10进制的数据转换成16进制的字符串
        # year - self.min_year的目的就是为了获取对应年份的下标
        moon_year_data = hex(self.moon_year_list[year - self.min_year])

        # 十六进制开头的0被省略了
        if len(moon_year_data) == 6:
            # eg：`0x07954` ==> ten_moon_year_data：`31060` ==> moon_year_data`0x7954`
            moon_year_data = moon_year_data.replace("0x", "0")
        else:
            # eg：`0x15176` ==> ten_moon_year_data：`86390` ==> moon_year_data`0x15176`
            moon_year_data = moon_year_data.replace("0x", "")
        
        # print(f"Hex：0x{moon_year_data}")  # 日志输出

        # 返回数据的 第一个数字 中间部分 最后一个数字
        return moon_year_data[0], moon_year_data[1:-1], moon_year_data[-1]
    
    def parse_moon_year_data(self, year):
        """解析获取的阴历数据"""
        start, body, end = self.__get_moon_year_data(year)
        # 第一位：要么0（29天）要么1（30天）：代表如果是闰年，多出的那个月是大月还是小月
        # PS：其实没有闰月也就不用算闰月的天数了，我这边为了大家思路清楚，就逐一写下
        if start == "0":
            leap_moon_day = 29
        else:
            leap_moon_day = 30

        # 中间部分：农历每个月有多少天（1为30，0为29）
        # int(body, 16) => 16进制转10进制；bin() => 十进制转二进制
        bin_data = bin(int(body, 16))  # eg：[0x]795 => 1941 => 0b11110010101
        # PS：还记得我们说过，这个数据有点小问题吗？如果只有11个月份需要自己在头部补一个0
        if len(bin_data) == 13:
            bin_data = bin_data.replace("0b", "0")  # 顺便把二进制的标识去除
        else:
            bin_data = bin_data.replace("0b", "")
        # 阴历每月有多少天
        year_moon_day_list = []
        # 农历非闰月的1~12月的天数
        for item in bin_data:
            if item == "0":
                year_moon_day_list.append(29)  # 0为29
            else:
                year_moon_day_list.append(30)  # 1为30

        # 尾部：代表这一年闰月是闰几月（没有闰月则为0）
        if end != "0":
            leap_moon = int(end, 16) # 16进制转10进制
        else:
            leap_moon = 0

        # 返回闰月是几月（0代表没有），闰月多少天，对应农历每一月有多少天
        return leap_moon, leap_moon_day, year_moon_day_list

    def get_moon_year_day_list(self, year):
        """获取闰月月份索引（0代表没有闰月）和农历每月天数（包含闰月）"""
        leap_moon, leap_moon_day, year_moon_day_list = self.parse_moon_year_data(year)
        if leap_moon == 0:
            return leap_moon, year_moon_day_list
        else:
            # 把闰月插入到对应月份之后（eg：闰4月在4月后面）
            year_moon_day_list.insert(leap_moon, leap_moon_day)
            return leap_moon, year_moon_day_list

    def sun_day_to_moon_day(self, year, mon, day):
        """阳历转阴历（year参考范围：1900.1.31 ~ 2100.12.31"""
        # 这边是真正暴露给用户的地方，需要验证一下年份的上下限
        if year > 2100 or year < 1900:
            return -1
        # 低于阴历数据的最小年
        if (year == 1900 and mon == 1 and day < 31):
            return -1

def main():
    import random
    # 随机测试
    almanac = Almanac()
    # for _ in range(10):
    #     year = random.randint(1980, 2025)
    #     # mon = random.randint(1, 12)
    #     # print(almanac.print_words(year, mon))
    #     print("-" * 20)
    #     print(year, "是否是闰年", almanac.is_leap_year(year))
    #     # print(almanac.get_moon_year_data(year))
    #     # print(almanac.parse_moon_year_data(year))
    #     print(almanac.get_moon_year_day_list(year))
    for year in range(1900, 2101):
        print(year, "是否是闰年", almanac.is_leap_year(year))
        moon_year_data_list = almanac.get_moon_year_day_list(year)
        # 一年有多少天
        moon_year_day_count = sum(moon_year_data_list[1])
        print(f"该年阴历总共有{moon_year_day_count}天，每月数据：{moon_year_data_list}")
    
if __name__ == "__main__":
    main()
