using System;
using System.Linq;

namespace _1base
{
    // https://www.cnblogs.com/dotnetcrazy/p/9102030.html
    public static class Program
    {
        private static void Main()
        {
            #region BaseCode

            var test = "123";//定义一个变量
            Console.WriteLine(test);//输出这个变量

            Console.WriteLine("请输入用户名：");
            var name = Console.ReadLine();

            Console.WriteLine("请输入性别:");
            var gender = Console.ReadLine();

            Console.WriteLine($"Name:{name}，Gender:{gender}"); //推荐用法
            Console.WriteLine("Name:{0}，Gender:{1}", name, gender); //Old 输出

            //类型转换
            Console.WriteLine("输入第一个数字：");
            var num1 = Console.ReadLine();
            Console.WriteLine("输入第二个数字:");
            var num2 = Console.ReadLine();
            Console.WriteLine($"num1+num2={Convert.ToInt32(num1) + Convert.ToInt32(num2)}");

            //Convert.ToInt64(),Convert.ToDouble()，Convert.ToString()
            Console.Write("dnt.dkill.net/now");
            Console.WriteLine("带你走进中医经络");

            var temp = "xxx";
            var tEmp = "===";
            Console.WriteLine(temp + tEmp);
            var num = 9;
            Console.WriteLine("num=9,下面结果是对2的除，取余，取商操作：");
            Console.WriteLine(num / 2.0);
            Console.WriteLine(num % 2.0);
            Console.WriteLine(num / 2);
            //指数
            Console.WriteLine(Math.Pow(2, 3));

            int age = 24;

            if (age >= 23)
                Console.WriteLine("七大姑曰：工作了吗？八大姨问：买房了吗？异性说：结婚了吗？");
            else if (age >= 18)
            {
                Console.WriteLine(age);
                Console.WriteLine("成年了哇");
            }
            else
                Console.WriteLine("好好学习天天向上");

            int index = 1;
            int sum = 0;
            while (index <= 100)
            {
                sum += index;
                index++;
            }
            Console.WriteLine(sum);

            var url = "https://pan.baidu.com/s/1weaF2DGsgDzAcniRzNqfyQ#mmd";
            foreach (var item in url)
            {
                if (item == '#')
                    break;
                Console.Write(item);
            }
            Console.WriteLine("\n end ...");
            
            #endregion
            // Console.Read();
        }
    }
}