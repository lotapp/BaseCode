
using System.Collections;

namespace Enumerator
{
    /// <summary>
    /// 使MyArray能够For循环遍历
    /// </summary>
    public partial class MyArray: IEnumerable
    {
        /// <summary>
        /// 枚举器方法
        /// </summary>
        /// <returns></returns>
        public IEnumerator GetEnumerator()
        {
            return new MyEnumerator(this.array, this.count);
        }
    }
}