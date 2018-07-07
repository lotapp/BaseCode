using System;
using System.Collections;
using System.Collections.Generic;

namespace simpleDemo
{
    public partial class MyArray : IEnumerable
    {
        /// <summary>
        /// 枚举器方法
        /// </summary>
        /// <returns></returns>
        public IEnumerator GetEnumerator()
        {
            return MyEnumerator();
        }
        /// <summary>
        /// 通过yield快速实现
        /// </summary>
        /// <returns></returns>
        public IEnumerator<string> MyEnumerator()
        {
            foreach (var item in this.array)
            {
                yield return item;
            }
        }
    }
}