using System;

namespace _2Inheritance
{
    public class Dog : IRun, IEat
    {
        public void Run()
        {
            System.Console.WriteLine("狗狗跑");
        }

        public void Eat()
        {
            System.Console.WriteLine("狗狗吃");
        }
    }
}