using System;

namespace Polymorphism3
{
    public class Student : IRun
    {
        public void Runing()
        {
            Console.WriteLine("飞快的跑着去上课");
        }
    }
}