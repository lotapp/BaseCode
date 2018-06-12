using System;
using System.Collections.Generic;
using System.Linq;

// http://www.cnblogs.com/dotnetcrazy/p/9114691.html
namespace _2str
{
    public static class Program
    {
        private static void Main()
        {
            #region String
            //# # 字符串遍历、下标、切片
            //# user_str="七大姑曰：工作了吗？八大姨问：买房了吗？异性说：结婚了吗？"
            var user_str = "七大姑曰：工作了吗？八大姨问：买房了吗？异性说：结婚了吗？";

            //# #遍历
            //# for item in user_str:
            //#     print(item,end=" ")
            foreach (var item in user_str)
            {
                Console.Write(item);
            }

            //# #长度：len(user_str)
            //# print(len(user_str))
            Console.WriteLine(user_str.Length);

            //# #第一个元素：user_str[0]
            //# print(user_str[0])
            Console.WriteLine(user_str[0]);

            //# #最后一个元素：user_str[-1]
            //# print(user_str[-1])
            //# print(user_str[len(user_str)-1])#其他编程语言写法
            Console.WriteLine(user_str[user_str.Length - 1]);
            //
            //# #倒数第二个元素：user_str[-2]
            //# print(user_str[-2])
            Console.WriteLine(user_str[user_str.Length - 2]);

            //# # -------------------------------------------------------------
            //
            //# 切片:[start_index:end_index:step] （end_index取不到）
            //# eg:str[1:4] 取str[1]、str[2]、str[3]
            //# eg:str[2:] 取下标为2开始到最后的元素
            //# eg:str[2:-1] 取下标为2～到倒数第二个元素（end_index取不到）
            //# eg:str[1:6:2] 隔着取～str[1]、str[3]、str[5]（案例会详细说）
            //# eg:str[::-1] 逆向输出（案例会详细说，）
            //
            var it_str = "我爱编程，编程爱它，它是程序，程序是谁？";
            //
            //#eg:取“编程爱它” it_str[5:9]
            //            print(it_str[5:9])
            //            print(it_str[5:-11]) #end_index用-xx也一样
            //            print(it_str[-15:-11])#start_index用-xx也可以

            //Substring(int startIndex, int length)
            Console.WriteLine(it_str.Substring(5, 4));//第二个参数是长度

            //
            //#eg:取“编程爱它，它是程序，程序是谁？” it_str[5:]
            //            print(it_str[5:])#不写默认取到最后一个
            Console.WriteLine(it_str.Substring(5));//不写默认取到最后一个

            //#eg:一个隔一个跳着取（"我编，程它它程，序谁"） it_str[0::2]
            //            print(it_str[0::2])#step=△index（eg:0,1,2,3。这里的step=> 2-0 => 间隔1）

            //这个我第一反应是用linq ^_^
            for (int i = 0; i < it_str.Length; i += 2)//对比看就清除Python的step为什么是2了，i+=2==》2
            {
                Console.Write(it_str[i]);
            }

            Console.WriteLine("\n倒序：");
            //#eg:倒序输出 it_str[::-1]
            //# end_index不写默认是取到最后一个，是正取（从左往右）还是逆取（从右往左），就看step是正是负
            //            print(it_str[::-1])
            //            print(it_str[-1::-1])#等价于上一个
            for (int i = it_str.Length - 1; i >= 0; i--)
            {
                Console.Write(it_str[i]);
            }
            //其实可以用Linq：Console.WriteLine(new string(it_str.ToCharArray().Reverse().ToArray()));
            #endregion

            #region StringMethod
            var test_str = "ABCDabcdefacddbdf";

            //# # 查找:find,rfind,index,rindex
            //# # xxx.find(str, start, end)
            //# print(test_str.find("cd"))#从左往右
            Console.WriteLine(test_str.IndexOf('a'));//4
            Console.WriteLine(test_str.IndexOf("cd"));//6

            //# print(test_str.rfind("cd"))#从右往左
            Console.WriteLine(test_str.LastIndexOf("cd"));//11

            //# print(test_str.find("dnt"))#find和rfind找不到就返回-1
            Console.WriteLine(test_str.IndexOf("dnt"));//-1
            //# # index和rindex用法和find一样，只是找不到会报错（以后用find系即可）
            //# print(test_str.index("dnt"))

            //# # -------------------------------------------------------------
            //# # 计数:count
            //# # xxx.count(str, start, end)
            // print(test_str.count("d"))#4
            // print(test_str.count("cd"))#2
            // 第一反应，字典、正则、linq，后来想怎么用基础知识解决，于是有了这个~(原字符串长度-替换后的长度)/字符串长度

            System.Console.WriteLine(test_str.Length - test_str.Replace("d", "").Length);//统计单个字符就简单了
            System.Console.WriteLine((test_str.Length - test_str.Replace("cd", "").Length) / "cd".Length);
            System.Console.WriteLine(test_str);//不用担心原字符串改变（python和C#都是有字符串不可变性的）

            //# # -------------------------------------------------------------
            //
            //# # 替换:replace
            //# # xxx.replace(str1, str2, count_num)
            //# print(test_str)
            //# print(test_str.replace("b","B"))#并没有改变原字符串，只是生成了一个新的字符串
            //# print(test_str)
            System.Console.WriteLine(test_str.Replace("b", "B"));
            //# # replace可以指定替换几次
            //# print(test_str.replace("b","B",1))#ABCDaBcdefacddbdf
            // 替换指定次数的功能有点业余，就不说了

            //# # -------------------------------------------------------------

            //# 分割:split（按指定字符分割）,splitlines(按行分割),partition(以str分割成三部分,str前，str和str后),rpartition
            //# test_list=test_str.split("a")#a有两个，按照a分割，那么会分成三段，返回类型是列表（List），并且返回结果中没有a
            //# print(test_list)
            var test_array = test_str.Split('a');//返回数组（如果要返回列表==》test_str.Split('a').ToList();）
            var test_input = "hi my name is dnt";
            //# print(test_input.split(" ")) #返回列表格式（后面会说）['hi', 'my', 'name', 'is', 'dnt']
            test_input.Split(" ");
            //# print(test_input.split(" ",3))#在第三个空格处切片，后面的不管了
            //# # 按行分割，返回类型为List
            var test_line_str = "abc\nbca\ncab\n";
            //# print(test_line_str.splitlines())#['abc', 'bca', 'cab']
            test_line_str.Split("\n", StringSplitOptions.RemoveEmptyEntries);
            //# print(test_line_str.split("\n"))#看出区别了吧：['abc', 'bca', 'cab', '']
            //
            //# # # 没看出来就再来个案例
            //# test_line_str2="abc\nbca\ncab\nLLL"
            //# print(test_line_str2.splitlines())#['abc', 'bca', 'cab', 'LLL']
            //# print(test_line_str2.split("\n"))#再提示一下，最后不是\n就和上面一样效果
            //
            //# # 扩展：
            //# print("hi my name is dnt\t\n  m\n\t\n".split())#split()，默认按空字符切割(空格、\t、\n等等，不用担心返回'')
            //
            //# #partition,返回是元祖类型（后面会说的）,方式和find一样，找到第一个匹配的就罢工了
            //# print(test_str.partition("cd"))#('ABCDab', 'cd', 'efacddbdf')
            //# print(test_str.rpartition("cd"))#('ABCDabcdefa', 'cd', 'dbdf')
            //# print(test_str.partition("感觉自己萌萌哒"))#没找到：('ABCDabcdefacddbdf', '', '')
            //
            //# # -------------------------------------------------------------
            //# 连接：join
            //# separat.join(xxx)
            //# 错误用法：xxx.join("-")
            //# print("-".join(test_list))
            System.Console.WriteLine(string.Join("-", test_array));//test_array是数组 ABCD-bcdef-cddbdf
                                                                   // # # -------------------------------------------------------------

            //# # 头尾判断:startswith（以。。。开头）,endswith（以。。。结尾）
            //# # test_str.startswith（以。。。开头）
            var start_end_str = "http://www.baidu.net";
            //# print(start_end_str.startswith("https://") or start_end_str.startswith("http://"))
            System.Console.WriteLine(start_end_str.StartsWith("https://") || start_end_str.StartsWith("http://"));
            //# print(start_end_str.endswith(".com"))
            System.Console.WriteLine(start_end_str.EndsWith(".com"));
            //# # -------------------------------------------------------------
            //
            //# # 大小写系:lower(字符串转换为小写),upper(字符串转换为大写),title(单词首字母大写),capitalize(第一个字符大写，其他变小写)
            //# print(test_str)
            //# print(test_str.upper())#ABCDABCDEFACDDBDF
            System.Console.WriteLine(test_str.ToUpper());
            //# print(test_str.lower())#abcdabcdefacddbdf
            System.Console.WriteLine(test_str.ToLower());
            //# print(test_str.capitalize())#第一个字符大写，其他变小写
            //
            //# # -------------------------------------------------------------
            //
            //# # 格式系列：lstrip（去除左边空格）,rstrip（去除右边空格）,strip（去除两边空格）,ljust,rjust,center
            var strip_str = " I Have a Dream ";
            //# print(strip_str.strip()+"|")#我加 | 是为了看清后面空格，没有别的用处
            System.Console.WriteLine(strip_str.Trim() + "|");
            //# print(strip_str.lstrip()+"|")
            System.Console.WriteLine(strip_str.TrimStart() + "|");
            //# print(strip_str.rstrip()+"|")
            System.Console.WriteLine(strip_str.TrimEnd() + "|");

            // # #这个就是格式化输出，就不讲了
            // # print(test_str.ljust(50))
            // # print(test_str.rjust(50))
            // # print(test_str.center(50))
            // # # -------------------------------------------------------------

            //# 验证系列:isalpha（是否是纯字母）,isalnum（是否是数字|字母）,isdigit（是否是纯数字）,isspace（是否是纯空格）
            //
            //# test_str2="Abcd123"
            //# test_str3="123456"
            var test_str4 = "  \t";
            var test_str5 = "  \t \n "; //#isspace() ==>true
            // string.IsNullOrEmpty 和 string.IsNullOrWhiteSpace 是系统自带的，其他的你需要自己封装一个扩展类
            System.Console.WriteLine(string.IsNullOrEmpty(test_str4)); //false
            System.Console.WriteLine(string.IsNullOrWhiteSpace(test_str4));//true
            System.Console.WriteLine(string.IsNullOrEmpty(test_str5));//false
            System.Console.WriteLine(string.IsNullOrWhiteSpace(test_str5));//true
            #endregion

            // Console.Read();
        }
    }
}