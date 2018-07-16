namespace Decorators
{
    /// <summary>
    /// 默认登录组件（账号+密码）
    /// 其他方法省略
    /// </summary>
    public class LoginDecoratorV3 : WeChatLoginDecorator
    {
        public LoginDecoratorV3(BaseComponent obj) : base(obj)
        {
        }

        /// <summary>
        /// 添加QQ登录
        /// </summary>
        /// <returns></returns>
        public string QQLogin()
        {
            return "add QQLogin";
        }

        /// <summary>
        /// 添加新浪登录
        /// </summary>
        /// <returns></returns>
        public string SinaLogin()
        {
            return "add SinaLogin";
        }
    }
}