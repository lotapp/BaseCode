using System;

namespace deepcopy
{
    [Serializable]
    public partial class Teacher
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public override string ToString()
        {
            return $"Name:{Name},Age:{Age}";
        }
    }
}