using System;
using System.Collections.Generic;

namespace IteratorDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // 枚举器遍历
            var tmp = FibonaByIEnumerator(30);
            while (tmp.MoveNext())
            {
                Console.WriteLine(tmp.Current);
            }
            // 可枚举类型遍历
            foreach (var item in FibonaByIEnumerable(30))
            {
                Console.WriteLine(item);
            }
        }

        /// <summary>
        /// 返回一个枚举器
        /// </summary>
        public static IEnumerator<int> FibonaByIEnumerator(int n)
        {
            int a = 0;
            int b = 1;
            for (int i = 0; i < n; i++)
            {
                yield return b;
                (a, b) = (b, a + b);
            }
        }

        /// <summary>
        /// 返回一个可枚举类型
        /// </summary>
        public static IEnumerable<int> FibonaByIEnumerable(int n)
        {
            int a = 0;
            int b = 1;
            for (int i = 0; i < n; i++)
            {
                yield return b;
                (a, b) = (b, a + b);
            }
        }
    }
}
