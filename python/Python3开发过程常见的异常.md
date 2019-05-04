持续更新中...

- [常见异常解决方案](#%E5%B8%B8%E8%A7%81%E5%BC%82%E5%B8%B8%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
    - [1.Base](#1base)
        - [1.1.IndentationError: unexpected indent](#11indentationerror-unexpected-indent)
        - [1.2.TypeError: __str__ returned non-string (type NoneType)](#12typeerror-str-returned-non-string-type-nonetype)
        - [1.3.TypeError: 'list' object is not callable](#13typeerror-list-object-is-not-callable)
        - [1.4.xxx() missing 1 required positional argument: 'self'](#14xxx-missing-1-required-positional-argument-self)
        - [1.5.'module' object is not callable](#15module-object-is-not-callable)
            - [eg：TypeError: 'module' object is not callable](#egtypeerror-module-object-is-not-callable)
        - [1.6.AttributeError: `__enter__`](#16attributeerror-enter)
        - [1.7.'gbk' codec can't decode byte 0xff in position 3451: illegal multibyte sequence](#17gbk-codec-cant-decode-byte-0xff-in-position-3451-illegal-multibyte-sequence)
        - [1.8.RuntimeError: Queue objects should only be shared between processes through inheritance](#18runtimeerror-queue-objects-should-only-be-shared-between-processes-through-inheritance)
        - [1.9.OSError: [Errno 98] Address already in use](#19oserror-errno-98-address-already-in-use)
        - [1.10.Win下端口占用问题：OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试](#110win%E4%B8%8B%E7%AB%AF%E5%8F%A3%E5%8D%A0%E7%94%A8%E9%97%AE%E9%A2%98oserror-winerror-10013-%E4%BB%A5%E4%B8%80%E7%A7%8D%E8%AE%BF%E9%97%AE%E6%9D%83%E9%99%90%E4%B8%8D%E5%85%81%E8%AE%B8%E7%9A%84%E6%96%B9%E5%BC%8F%E5%81%9A%E4%BA%86%E4%B8%80%E4%B8%AA%E8%AE%BF%E9%97%AE%E5%A5%97%E6%8E%A5%E5%AD%97%E7%9A%84%E5%B0%9D%E8%AF%95)
        - [1.11.Win下Python包不能安装的说明](#111win%E4%B8%8Bpython%E5%8C%85%E4%B8%8D%E8%83%BD%E5%AE%89%E8%A3%85%E7%9A%84%E8%AF%B4%E6%98%8E)
                - [网站](#%E7%BD%91%E7%AB%99)
                - [PYPI](#pypi)
    - [2.Web](#2web)
        - [2.1.Django](#21django)
            - [1.django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.](#1djangocoreexceptionsimproperlyconfigured-mysqlclient-1313-or-newer-is-required-you-have-093)
    - [3.Spider](#3spider)
        - [3.1.通用](#31%E9%80%9A%E7%94%A8)
            - ['gbk' codec can't encode character '\xa0' in position 34: illegal multibyte sequence](#gbk-codec-cant-encode-character-xa0-in-position-34-illegal-multibyte-sequence)
    - [Python常见异常汇总](#python%E5%B8%B8%E8%A7%81%E5%BC%82%E5%B8%B8%E6%B1%87%E6%80%BB)

# 常见异常解决方案

## 1.Base

Python3.7环境相关：<a href="https://www.cnblogs.com/dotnetcrazy/p/9095793.html" target="_blank">https://www.cnblogs.com/dotnetcrazy/p/9095793.html</a>

### 1.1.IndentationError: unexpected indent

===>检查一下缩进，可以借用yapf或者pycodestyle来帮忙<br/>
可以参考这篇文章的末尾：<a href="https://www.cnblogs.com/dotnetcrazy/p/9095793.html" target="_blank">https://www.cnblogs.com/dotnetcrazy/p/9095793.html</a>

---

### 1.2.TypeError: __str__ returned non-string (type NoneType) 

==> def __str__(self) 里面没有return返回值
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180617092021709-18324149.png)

---

### 1.3.TypeError: 'list' object is not callable

==>'list'对象不可调用，一般都是用户自定变量和list重名了
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180626145839253-1425076230.png)

原因：
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180626145846171-830470148.png)

---

### 1.4.xxx() missing 1 required positional argument: 'self'

==>装饰`实例方法`的时候容易出现莫名其妙的错误，所以一般加上get方法，来个案例：

```py
import types
from functools import wraps

class Log(object):
    def __init__(self, func):
        wraps(func)(self)  # @wraps(func) 访问不到，所以用这种方式
        self.__func = func

    def __call__(self, *args, **kvs):
        print("%s log_info..." % self.__func.__name__)
        return self.__func(*args, **kvs)

    # 装饰实例方法的时候容易出现莫名其妙的错误，所以一般加上get方法
    # eg：show() missing 1 required positional argument: 'self'
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

class LoginComponent(object):
    def __init__(self, name):
        self.__name = name

    @Log
    def show(self):
        """实例方法"""
        print("欢迎你：%s" % self.__name)

    @classmethod
    @Log  # 写在下面（"从下往上装，从上往下拆"）
    def login_in(cls):
        """类方法"""
        print("登录ing")

    @staticmethod
    @Log
    def show_news():
        """静态方法"""
        print("今天的新闻是...")

def main():
    LoginComponent.login_in()
    LoginComponent.show_news()
    login = LoginComponent("小明")
    login.show()

if __name__ == '__main__':
    main()
```

---

### 1.5.'module' object is not callable

#### eg：TypeError: 'module' object is not callable

原因：命令不规范，或者你导入的模块当做类来使用了

比如今天写demo的时候，随手创建了个文件名：`mmap.py`
```py
import mmap

fd = os.open("mmap_file", os.O_RDWR)  # 读+写
m = mmap.mmap(fd, 0)  # 创建映射
```
导入的模块也是mmap，那问题就来了～所以，就算随手测试也是要命名规范的-_-#

---

### 1.6.AttributeError: `__enter__`

一般都是上下文管理器`with xxx as x:`的问题，看看是否不能托管的进行了托管，或者自定义上下文管理器`__enter__ `方法有问题

---

### 1.7.'gbk' codec can't decode byte 0xff in position 3451: illegal multibyte sequence

一般都是编码问题，Linux一切正常，win下面出现了糟心事

解决：

指定编码：头文件包含`# _*_ coding:utf-8 _*_`  and 指定编码格式 `encoding="utf-8"`

还出现错误就忽略吧：`errors='ignore'` eg：`with open("bai.csv","r",errors='ignore') as f:`

---

### 1.8.RuntimeError: Queue objects should only be shared between processes through inheritance

队列对象只能通过继承进程之间共享，因为用到了Pool，`multiprocessing.Queue()`会有点问题，换为`multiprocessing.Manager().Queue()`即可

<https://www.cnblogs.com/dotnetcrazy/p/9426279.html#扩展补充>

---

### 1.9.OSError: [Errno 98] Address already in use

具体可以查看此文章：<https://www.cnblogs.com/dotnetcrazy/p/10003762.html>

### 1.10.Win下端口占用问题：OSError: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试

<https://www.cnblogs.com/dotnetcrazy/p/10093178.html>

### 1.11.Win下Python包不能安装的说明

##### 网站

**Win下Py包安装出错就去这个网站下对应包**：https://www.lfd.uci.edu/~gohlke/pythonlibs/

然后 pip install xxx

![](https://img2018.cnblogs.com/blog/1127869/201901/1127869-20190107125659374-320516812.png)

##### PYPI

去PyPI搜索包，然后左侧菜单栏有下载链接

![](https://img2018.cnblogs.com/blog/1127869/201904/1127869-20190427170259406-1405211917.png)

之后pip install xxx 即可

---

## 2.Web

### 2.1.Django

#### 1.django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

解决：<https://www.cnblogs.com/dotnetcrazy/p/10779304.html>

![](https://img2018.cnblogs.com/blog/1127869/201904/1127869-20190427165605929-2070907393.png)

## 3.Spider

### 3.1.通用

#### 'gbk' codec can't encode character '\xa0' in position 34: illegal multibyte sequence

<https://www.cnblogs.com/dotnetcrazy/p/10803209.html>



## Python常见异常汇总

有些异常官方没有写进去，我补了一些常用的异常：`https://docs.python.org/3/library/exceptions.html`

**`BaseException`**
- `SystemExit`：`sys.exit()`引发的异常（目的：让Python解释器退出）
- `KeyboardInterrupt`：用户Ctrl+C终止程序引发的异常
- **`GeneratorExit`**：生成器或者协程关闭的时候产生的异常（**特别注意**）
- **`Exception`**：所有内置异常（非系统退出）或者用户定义异常的基类
    - **`asyncio.Error`**
        - **`asyncio.CancelledError`**
        - **`asyncio.TimeoutError`**：和`Exception.OSError.TimeoutError`区分开
        - `asyncio.InvalidStateError`：`Task/Future`内部状态无效引发
    - `asyncio.LimitOverrunError`：超出缓冲区引发的异常
    - `StopIteration`：`next()、send()`引发的异常：
        - `https://www.cnblogs.com/dotnetcrazy/p/9278573.html#6.Python迭代器`
    - `StopAsyncIteration`：`__anext__()`引发的异常
    - ArithmeticError
        - FloatingPointError
        - OverflowError
        - ZeroDivisionError
    - `AssertionError`：当断言`assert`语句失败时引发
    - `AttributeError`：当属性引用或赋值失败时引发
    - BufferError
    - `EOFError`
        - `asyncio.IncompleteReadError`：读取操作未完成引发的错误
    - ImportError
        - ModuleNotFoundError
    - LookupError
        - IndexError
        - KeyError
    - MemoryError
    - NameError
        - UnboundLocalError
    - **`OSError`**：当系统函数返回与系统相关的错误时引发
        - BlockingIOError
        - ChildProcessError
        - ConnectionError
           - BrokenPipeError
           - ConnectionAbortedError
           - ConnectionRefusedError
           - ConnectionResetError
        - FileExistsError
        - FileNotFoundError
        - InterruptedError
        - IsADirectoryError
        - NotADirectoryError
        - PermissionError
        - ProcessLookupError
        - **`TimeoutError`**：系统函数执行超时时触发
    - `ReferenceError`：引用错误（对象被资源回收或者删除了）
    - **`RuntimeError`**：出错了，但是检测不到错误类别时触发
        - `NotImplementedError`：为实现报错（比如调用了某个不存在的子类方法）
        - `RecursionError`：递归程度太深引发的异常
        - `asyncio.SendfileNotAvailableError`：系统调用不适用于给定的套接字或文件类型
    - **`SyntaxError`**：语法错误时引发（**粘贴代码经常遇到**）
        - `IndentationError`：缩进有问题
        - `TabError`：当缩进包含不一致的制表符和空格使用时引发
    - SystemError
    - TypeError：类型错误
    - ValueError
        - UnicodeError
        - UnicodeDecodeError
        - UnicodeEncodeError
        - UnicodeTranslateError
    - Warning
    - DeprecationWarning
    - PendingDeprecationWarning
    - RuntimeWarning
    - SyntaxWarning
    - UserWarning
    - FutureWarning
    - ImportWarning
    - UnicodeWarning
    - BytesWarning
    - ResourceWarning