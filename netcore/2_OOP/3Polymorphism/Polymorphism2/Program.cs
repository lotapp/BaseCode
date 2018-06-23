using System;

namespace Polymorphism2
{
    class Program
    {
        static void Main(string[] args)
        {
            Animal[] animals = { new Dog(), new Cat() };
            foreach (var item in animals)
            {
                item.Call();
            }
        }
    }
}
