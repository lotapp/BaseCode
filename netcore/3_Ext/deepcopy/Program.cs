using System;
using System.Linq;
using System.Collections.Generic;

namespace deepcopy
{
    public partial class Student
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
            var list4 = new List<int>(list3);

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

            #region 引用类型浅拷贝
            var list5 = new List<Student>(){
                new Student { Name = "小张", Age = 22 },
                new Student { Name = "小明", Age = 23 }
                };
            var p = new Student() { Name = "小潘", Age = 23 };
            list5.Add(p);

            // 浅拷贝一份
            var list6 = new List<Student>(list5);

            // 浅拷贝测试
            // 我们修改一下list5，list6没有跟着改变，说明第一层的地址的确不一样
            list5.Add(new Student() { Name = "小胖", Age = 24 });
            // 当我们修改小潘同学的年龄时，大家都变了，说明真的只是浅拷贝
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
            Console.WriteLine("\n=============");
            #endregion

            #region 引用类型浅拷贝CopyTo
            var list7 = new List<Student>(){
                new Student { Name = "小张", Age = 22 },
                new Student { Name = "小明", Age = 23 }
            };
            var p1 = new Student() { Name = "小潘", Age = 23 };
            list7.Add(p1);

            var array = new Student[list7.Count];
            list7.CopyTo(array);
            var list8 = array.ToList();
            // 浅拷贝测试
            // 我们修改一下list7，list8没有跟着改变，说明第一层的地址的确不一样
            list7.Add(new Student() { Name = "小胖", Age = 24 });
            // 当我们修改小潘同学的年龄时，大家都变了，说明真的只是浅拷贝
            p1.Age = 24;

            foreach (var item in list7)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("=============");
            foreach (var item in list8)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("\n############");
            #endregion

            #region 引用类型深拷贝-简单方式实现
            var oldList = new List<Person>(){
                new Person(){Name="小明",Age=23},
                new Person(){Name="小张",Age=22},
            };
            var xiaoPan = new Person() { Name = "小潘", Age = 23 };
            oldList.Add(xiaoPan);

            var newList = oldList.DeepCopy();

            //测试
            oldList.Add(new Person() { Name = "小胖", Age = 23 });
            xiaoPan.Age = 24;

            foreach (var item in oldList)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("========");
            foreach (var item in newList)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("\n###########");
            #endregion

            #region 引用类型深拷贝-序列化实现
            var oldTestList = new List<Teacher>(){
                new Teacher(){Name="小明",Age=23},
                new Teacher(){Name="小张",Age=22},
            };
            var s = new Teacher() { Name = "小潘", Age = 23 };
            oldTestList.Add(s);

            var newTestList = oldTestList.DeepCopy2();

            //测试
            oldTestList.Add(new Teacher() { Name = "小胖", Age = 23 });
            s.Age = 24;

            foreach (var item in oldTestList)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("========");
            foreach (var item in newTestList)
            {
                Console.WriteLine(item);
            }
            #endregion
        }
    }
}
