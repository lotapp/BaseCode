using System;

namespace simpleDemo
{
    public partial class MyArray
    {
        /// <summary>
        /// 数组容量
        /// </summary>
        private string[] array = new string[4];
        /// <summary>
        /// 数组元素个数
        /// </summary>
        private int count = 0;
        /// <summary>
        /// 当前数组的长度
        /// </summary>
        public int Length
        {
            get
            {
                return count;
            }
        }

        /// <summary>
        /// 添加元素
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public MyArray Add(string str)
        {
            //要溢出的时候扩容
            if (count == array.Length)
            {
                string[] newArray = new string[2 * array.Length];
                array.CopyTo(newArray, 0);
                array = newArray;//array重新指向
            }
            array[count++] = str;
            return this;
        }

        /// <summary>
        /// 移除某一项
        /// </summary>
        /// <param name="i"></param>
        /// <returns></returns>
        public MyArray RemoveAt(int i)
        {
            for (int j = i; j < count - 1; j++)
            {
                array[j] = array[j + 1];
            }
            array[count - 1] = string.Empty;//add 干掉移除的数组
            count--;//少了一个元素所以--
            return this;
        }

        /// <summary>
        /// 索引器
        /// </summary>
        /// <param name="index"></param>
        /// <returns></returns>
        public string this[int index]
        {
            get
            {
                return array[index];
            }
            set
            {
                array[index] = value;
            }
        }
    }
}