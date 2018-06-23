using System;

namespace Polymorphism2
{
    public class Cat : Feline
    {
        /// <summary>
        /// 子类必须实现父类抽象方法，如果不实现，那么该类也必须是抽象类
        /// </summary>
        public override void Call()
        {
            Console.WriteLine("喵喵叫~~~");
        }
    }
}