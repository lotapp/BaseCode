namespace Decorators
{
    /// <summary>
    /// 默认登录组件（账号+密码）
    /// 其他方法省略
    /// </summary>
    public class WeChatLoginDecorator : BaseDecorator
    {
        public WeChatLoginDecorator(BaseComponent obj) : base(obj)
        {
        }
        /// <summary>
        /// 添加微信第三方登录
        /// </summary>
        /// <returns></returns>
        public string WeChatLogin()
        {
            return "add WeChatLogin";
        }
    }
}