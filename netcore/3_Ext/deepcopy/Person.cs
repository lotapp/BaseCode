using System;

namespace deepcopy
{
    public partial class Person : ICloneable
    {
        public string Name { get; set; }
        public int Age { get; set; }

        //实现ICloneable的Clone方法
        public object Clone()
        {
            return base.MemberwiseClone();
        }

        public override string ToString()
        {
            return $"Name:{Name},Age:{Age}";
        }
    }
}