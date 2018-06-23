using System;

namespace Polymorphism3
{
    public class Cat : IRun
    {
        public void Runing()
        {
            Console.WriteLine("飞快的跑着上树");
        }
    }
}