using System;
using System.Collections.Generic;

namespace TestBreak
{
    class Program
    {
        static void Main(string[] args)
        {
            foreach (var item in GetValue())
            {
                Console.WriteLine(item);
            }
        }

        public static IEnumerable<int> GetValue()
        {
            for (int i = 0; i < 5; i++)
            {
                yield return i;
                if (i == 2)
                {
                    yield break;
                }
            }
        }
    }
}
