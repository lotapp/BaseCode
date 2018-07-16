namespace Decorators
{
    /// <summary>
    /// 装饰器
    /// </summary>
    public class BaseDecorator : BaseComponent
    {
        protected BaseComponent _component;
        /// <summary>
        /// 构造函数
        /// </summary>
        /// <param name="obj">登录组件对象</param>
        protected BaseDecorator(BaseComponent obj)
        {
            this._component = obj;
        }
        public override string Login()
        {
            string str = string.Empty;
            if (_component != null) str = _component.Login();
            return str;
        }
    }
}