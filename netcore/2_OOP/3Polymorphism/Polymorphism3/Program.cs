using System;

namespace Polymorphism3
{
    class Program
    {
        static void Main(string[] args)
        {
            IRun[] objs = { new Student(), new Cat() };
            foreach (var item in objs)
            {
                item.Runing();
            }
        }
    }
}
