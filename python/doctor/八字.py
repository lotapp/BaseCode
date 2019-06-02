from datetime import datetime


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
        self.__sun_year_days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # 选阳历1900年1月31号为基准日期（对应农历1900年1月1日）
        self.base_datetime = datetime(1900, 1, 31)

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

    def __is_leap_year(self, year):
        """查询是否是闰年（1：闰年，2月是29天；0：不是闰年，2月28天）"""
        # 阳历的2月正常都是28天，但闰年的阳历2月是29天
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 1  # 闰年，2月是29天
        else:
            return 0  # 不是闰年，2月28天
    
    # def get_sun_mon_day_count(self, year, mon):
    #     """获取阳历月份的天数（不需要就删掉）"""
    #     if mon == 2:  # 闰2月是29天（比平时多一天）
    #         return self.__sun_year_days_list[mon] + self.__is_leap_year(year)
    #     else:
    #         return self.__sun_year_days_list[mon]

    def get_sun_year_day_count(self, year):
        """获取该年的阳历有多少天"""
        return sum(self.__sun_year_days_list) + self.__is_leap_year(year)

    def __parse_leap_mon_data(self, year):
        """解析农历数据"""
        # 1.把10进制的数据转换成16进制的字符串
        # year - self.min_year的目的就是为了获取对应年份的下标
        moon_year_data = hex(self.moon_year_list[year - self.min_year])
         
        # 2.最后一位是闰几月（0代表没有闰月）
        # 尾部：代表这一年闰月是闰几月（没有闰月则为0）
        if moon_year_data[-1] != "0":
            self.leap_moon = int(moon_year_data[-1], 16)  # 16进制转10进制
        else:
            self.leap_moon = 0  # 其实没有闰月后，闰月的天数就不需要计算了
        
        # 3.设置闰月的天数
        # 十六进制开头的0会被省略了
        if len(moon_year_data) == 6:
            self.leap_moon_day = 29  # 开头是0（29天）
        else:
            self.leap_moon_day = 30  # 开头是1（30天）
    
    def get_moon_mon_day_count(self, year, mon):
        """获取阴历月份的天数"""
        return 30 if self.moon_year_list[year - self.min_year] & (0x10000 >> mon) else 29
    
    def __get_moon_year_days_list(self, year):
        """获取该年的阴历月份天数列表（不含闰月）"""
        return [self.get_moon_mon_day_count(year, m) for m in range(1, 13)]
    
    def get_moon_year_day_count(self, year):
        """获取该年的阴历有多少天"""
        self.__parse_leap_mon_data(year)  # 解析农历数据
        # 阴历天数 = 12个月的天数 + 闰月天数
        return sum(self.__get_moon_year_days_list(year)) + self.leap_moon_day

    # def get_moon_year_days_info(self, year):
    #     """获取闰月月份索引（0代表没有闰月）、农历每月天数（包含闰月）、该年的农历总天数
    #     PS：关于0代表没闰月的说明：就算是闰1月也得排1月后面，那么index也是为1
    #     """
    #     self.__parse_leap_mon_data(year)  # 解析农历数据
    #     # 获取这一年每月有多少天
    #     moon_mon_days_list = self.__get_moon_year_days_list(year)
    #     if self.leap_moon == 0:
    #         return self.leap_moon, moon_mon_days_list, sum(moon_mon_days_list)
    #     else:
    #         # 把闰月插入到对应月份之后（eg：闰4月在4月后面）
    #         moon_mon_days_list.insert(self.leap_moon, self.leap_moon_day)
    #         return self.leap_moon, moon_mon_days_list, sum(moon_mon_days_list)

    def sun_day_to_moon_day(self, year, mon, day):
        """阳历转阴历（year参考范围：1900.1.31 ~ 2100.12.31"""
        # 这边是真正暴露给用户的地方，需要验证一下年份的上下限
        if year > self.max_year or year < self.min_year:
            return -1
        # 低于阴历数据的最小年
        if (year == self.min_year and mon == 1 and day < 31):
            return -1
        
        # 需要转换的公历日期 − 公历基准 + 1 = 转换后的农历日期 − 农历基准 + 1 = 相差天数（偏移量）
        # > **PS：对于+1的说明：今天是6.1号，明天是6.2号，2-1=1，但是实际天数确是2天**
        
        # 我们就选农历`1900年1月1日`为基准天 ==> 对应阳历：`1900年1月31日`
        # > PS：为啥选1900年呢？黄帝内经里面说过，上古的人洁身自好一般都能活到120，现在人大多不爱惜自己的身体（主动或被动）所以留个美好愿景吧~

        # 以求阳历`2019年1月1日`对应的农历为例：
        # 1.算出阳历距离基准阳历的天数（偏移量）
        # type：datetime.timedelta
        sun_datetime = datetime(year, mon, day)
        offset_day = (sun_datetime - self.base_datetime).days  # 43434天

        # 需要转换的公历日期 − 公历基准 = 转换后的农历日期 − 农历基准
        # 2.根据间隔天数和农历基准值来计算出农历
        # 2.1.农历日期的年份（农历每一年的天数是不固定的）
        # 用计算出的相差天数依次减去从农历基准开始后的每一年的农历天数，当天数<=0的时候结束循环
        n = 0
        for y in range(1900, year + 1):
            offset_day -= self.get_moon_year_day_count(y)
            n += 1  # 在农历1900年的基础上 + 1年
            if offset_day <= 0:
                break
        moon_year = self.base_datetime.year + n
        # 2.2.历日期的月份

        # 2.3.农历日期的天

        return moon_year

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
    #     # 闰月是几月（0代表没有），该年的农历每个月天数，该年农历总天数
    #     print(almanac.get_moon_year_days_info(year))
    
    # 顺序测试
    # for year in range(2000, 2022):
    #     # print(year, "是否是闰年", almanac.is_leap_year(year))
    #     # 闰月是几月（0代表没有），该年的农历每个月天数，该年农历总天数
    #     print(f"阳历：{year}年，对应阴历月份信息：{almanac.get_moon_year_days_info(year)}")

    print(almanac.sun_day_to_moon_day(2019, 1, 1))


if __name__ == "__main__":
    main()