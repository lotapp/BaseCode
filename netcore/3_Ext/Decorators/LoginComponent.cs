namespace Decorators
{
    /// <summary>
    /// 默认登录组件（账号+密码）
    /// 其他方法省略
    /// 友情提醒一下，抽象类里面可以定义非抽象方法
    /// </summary>
    public class LoginComponent : BaseComponent
    {
        public override string Login()
        {
            return "默认账号密码登录";
        }
    }
}