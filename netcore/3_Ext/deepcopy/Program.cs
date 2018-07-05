using System;
using System.Collections.Generic;
using System.Linq;

namespace deepcopy
{
    public class Student
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public override string ToString()
        {
            return $"Name:{Name},Age:{Age}";
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            #region 赋值
            // 和 Python一样，直接赋值即可
            var list1 = new List<int>() { 1, 2, 2 };
            var list2 = list1;
            list1.Add(3);
            foreach (var item in list1)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
            foreach (var item in list2)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine("\n================");
            #endregion

            #region 简单类型深拷贝
            // https://docs.microsoft.com/zh-cn/dotnet/api/system.collections.generic.list-1.copyto?view=netcore-2.1
            var list3 = new List<int>() { 1, 2, 2 };
            var list4 = new List<int>();
            list4.AddRange(list3);

            // 验证一下
            list3.Add(3);
            foreach (var item in list3)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
            foreach (var item in list4)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine("\n================");

            // var listA = new List<int>() { 1, 2, 2 };

            // var array = new int[listA.Count];
            // listA.CopyTo(array);// CopyTo(T[])

            // List<int> listB = array.ToList();

            // // 验证一下
            // listA.Add(3);
            // foreach (var item in listA)
            // {
            //     Console.Write(item + " ");
            // }
            // Console.WriteLine();
            // foreach (var item in listB)
            // {
            //     Console.Write(item + " ");
            // }
            // Console.WriteLine("\n================");
            #endregion

            #region 复杂类型浅拷贝
            var list5 = new List<Student>(){
                new Student { Name = "小张", Age = 22 },
                new Student { Name = "小明", Age = 23 }
                };
            var p = new Student() { Name = "小潘", Age = 23 };
            list5.Add(p);

            var list6 = new List<Student>();
            list6.AddRange(list5);

            // 浅拷贝测试
            list5.Add(new Student() { Name = "小胖", Age = 24 });
            p.Age = 24;

            foreach (var item in list5)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("=============");
            foreach (var item in list6)
            {
                Console.WriteLine(item);
            }
            #endregion
        }
    }
}
