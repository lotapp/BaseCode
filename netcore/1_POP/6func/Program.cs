using System;
using System.Collections.Generic;

namespace _6func
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Base
            // # 定义一个空函数：
            Method();
            // # 定义一个无参函数
            GetName();
            // # 定义一个含参函数
            ShowInfos("李四", 22);
            // # 定义一个含默认参数(缺省参数)的函数
            DefaultParam("张三");
            // # 定义有返回值的函数
            int result = DivHaveReturn(1, 2);
            Console.WriteLine($"计算结果为{result}");
            #endregion

            // # 定义含有多个返回值的函数（利用了元组）
            var (sum, dvalue) = DivHaveReturns(1, 2);
            Console.WriteLine($"sum:{sum},D-value:{dvalue}");

            // 传多个参数系列：
            // 引用传递（通过元组、列表实现）：扩展有可变类型和不可变类型作为形参的对比
            var list = new List<int>() { 1, 2, 3, 4, 5 };
            Console.WriteLine(DefaultSomeParams(list));
            Console.WriteLine(list.Count);//这就是引用传递的证明

            // # 定义一个可变参数的函数(参数名字一般都是*args)
            Console.WriteLine(DefaultParams(1, 2, 3, 4, 5));

            // # 定义含关键字参数的函数 直接传Dict
        }

        #region base
        /// <summary>
        /// 定义一个空函数
        /// </summary>
        private static void Method()
        {

        }
        /// <summary>
        /// 定义一个无参函数
        /// </summary>
        // private static void GetName()
        // {
        //     Console.WriteLine("你好");
        // }
        //简写
        private static void GetName() => Console.WriteLine("你好");

        /// <summary>
        /// 定义一个含参数的函数
        /// </summary>
        /// <param name="name">名字</param>
        /// <param name="age">年龄</param>
        // private static void ShowInfos(string name, int age)
        // {
        //     Console.WriteLine($"我叫{name} 我的年龄是{age}");
        // }
        //简写
        private static void ShowInfos(string name, int age) => Console.WriteLine($"我叫{name} 我的年龄是{age}");

        /// <summary>
        /// 定义一个含缺省参数的函数
        /// </summary>
        /// <param name="name">名字</param>
        /// <param name="age">年龄默认23</param>
        // private static void DefaultParam(string name, int age = 23)
        // {
        //     Console.WriteLine($"我叫{name} 我的年龄是{age}");
        // }
        //简写
        private static void DefaultParam(string name, int age = 23) => Console.WriteLine($"我叫{name} 我的年龄是{age}");

        /// <summary>
        /// 定义一个有返回值的函数（计算a+b，返回计算结果）
        /// </summary>
        /// <param name="a">num1</param>
        /// <param name="b">num2</param>
        // private static int DivHaveReturn(int a, int b)
        // {
        //     return a + b;
        // }
        //简写
        private static int DivHaveReturn(int a, int b) => a + b;
        #endregion

        /// <summary>
        /// 定义含有多个返回值的函数（利用了元组）
        /// 计算a+b的和，计算a-b，并返回两个结果
        /// </summary>
        /// <param name="a"></param>
        /// <param name="b"></param>
        /// <returns></returns>
        // private static (int sum,int dValue) DivHaveReturns(int a, int b)
        // {
        //     return ((a+b),(a-b));
        // }
        //简写
        private static (int sum, int dValue) DivHaveReturns(int a, int b) => ((a + b), (a - b));

        #region 传入多个参数系列
        /// <summary>
        /// 利用列表实现,引用传递之类的C#还有ref和out，这边就不说了
        /// </summary>
        /// <param name="nums"></param>
        /// <returns></returns>
        private static int DefaultSomeParams(List<int> numList)
        {
            int sum = 0;
            foreach (var item in numList)
            {
                sum += item;
            }
            numList.Clear();
            return sum;
        }
        /// <summary>
        /// 定义一个可变参数的函数
        /// </summary>
        /// <param name="args"></param>
        /// <returns></returns>
        private static int DefaultParams(params int[] args)
        {
            int sum = 0;
            foreach (var item in args)
            {
                sum += item;
            }
            return sum;
        }
        #endregion
    }
}
