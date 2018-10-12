using System;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace testGIL
{
    class Program
    {
        static void Main(string[] args)
        {
            var list = new List<int>() { 1, 2, 3, 4, 5 };
            var tasks = list.AsParallel().Select(i => Task.Run(() => Test(i))).ToArray();
            Task.WhenAll(tasks).Wait();
        }
        static void Test(int i)
        {
            System.Console.WriteLine($"启动一个线程～");
            while (true) { }
        }
    }
}