using System;

namespace Decorators
{
    class Program
    {
        static void Main(string[] args)
        {
            #region 默认调用方式
            var obj = new LoginComponent();
            var str = obj.Login();
            Console.WriteLine(str);
            #endregion

            #region 登录模块V2
            // 实例化登录装饰器
            var loginDecorator = new WeChatLoginDecorator(new LoginComponent());
            // 原有的登录方法
            var str1 = loginDecorator.Login();
            // 现在新增的登录方法
            var str2 = loginDecorator.WeChatLogin();
            Console.WriteLine($"{str1}\n{str2}");
            #endregion

            #region 登录模块V3
            // 实例化登录装饰器
            var loginDecoratorV3 = new LoginDecoratorV3(new LoginComponent());
            // 原有的登录方法
            var v1 = loginDecoratorV3.Login();
            // 第二个版本迭代中的微信登录
            var v2 = loginDecoratorV3.WeChatLogin();
            // 新增的QQ和新浪登录
            var qqLogin = loginDecoratorV3.QQLogin();
            var sinaLogin = loginDecoratorV3.SinaLogin();
            Console.WriteLine($"{v1}\n{v2}\n{qqLogin}\n{sinaLogin}");
            #endregion

        }
    }
}
