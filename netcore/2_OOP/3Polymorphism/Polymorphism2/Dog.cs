using System;

namespace Polymorphism2
{
    public class Dog : Animal
    {
        /// <summary>
        /// 子类必须实现抽象类中的抽象方法
        /// </summary>
        public override void Call()
        {
            Console.WriteLine("汪汪叫~~~");
        }
    }
}