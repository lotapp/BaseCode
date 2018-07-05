using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Runtime.Serialization.Formatters.Binary;

namespace deepcopy
{
    public static partial class ListExt
    {
        // 只要T实现了ICloneable接口就可以了
        public static IEnumerable<T> DeepCopy<T>(this IEnumerable<T> list) where T : ICloneable
        {
            return list.Select(item => (T)item.Clone()).ToList();
        }

        //利用System.Runtime.Serialization序列化与反序列化实现深拷贝
        public static T DeepCopy2<T>(this T obj)
        {
            using (var stream = new MemoryStream())
            {
                var formatter = new BinaryFormatter();
                formatter.Serialize(stream, obj);
                stream.Seek(0, SeekOrigin.Begin);
                return (T)formatter.Deserialize(stream);
            }
        }
    }
}