using System;

namespace Closure
{
    class Program
    {
        static void Main(string[] args)
        {
            // var f1 = SlowSum(1, 2, 3, 4, 5);
            // Console.WriteLine(f1);
            // Console.WriteLine(f1());
            var func = QuadraticFunc(1, 0, 1);

            Console.WriteLine(func(0));
            Console.WriteLine(func(1));
            Console.WriteLine(func(2));
            Console.WriteLine(func(3));
            Console.WriteLine(func(4));
            Console.WriteLine(func(5));
        }

        public static Func<int> SlowSum(params int[] args)
        {
            return () =>
            {
                int sum = 0;
                foreach (var item in args)
                {
                    sum += item;
                }
                return sum;
            };
        }
        // 以上面的 y=ax²+bx+c 为例，C#实现：
        // public delegate TResult Func<in T, out TResult>(T arg);
        public static Func<double, double> QuadraticFunc(double a, double b, double c)
        {
            return x => a * x * x + b * x + c;
        }
    }
}
