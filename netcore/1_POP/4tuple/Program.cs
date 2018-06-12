using System;

// http://www.cnblogs.com/dotnetcrazy/p/9155310.html
namespace _4tuple
{
    public static class Program
    {
        private static void Main()
        {
            #region Tuple
            // C#中元组主要是方便程序员,不用自然可以.
            // 元祖系:https://msdn.microsoft.com/zh-cn/library/system.tuple.aspx
            // 值元组:https://msdn.microsoft.com/zh-cn/library/system.valuetuple.aspx
            // 比如:当你返回多个值是否还用ref out 或者返回一个list之类的?
            // 这些都需要先定义,比较麻烦.元祖在一些场景用的比较多 eg:        

            // 初始化
            // var test_tuple = ("萌萌哒", 1, 3, 5, "加息", "加息"); //这种方式就是valueTuple了

            // test_tuple.Item1 = "ddd";//可以修改值

            // test_tuple.GetType();
            // test_tuple.itemxxx //获取值只能通过itemxxx

            var result = GetCityAndTel();  //支持async/await模式
            var city = result.city;
            var tel = result.tel;
            // 拆包方式:
            var (city1, tel1) = GetCityAndTel();
            
            #endregion
            // Console.Read();
        }
        // public static (string city, string tel) GetCityAndTel()
        // {
        //     return ("北京", "110");
        // }
        // 简化写法
        public static (string city, string tel) GetCityAndTel() => ("北京", "110");
    }
}