# Python会用一个叫做PyEval_EvalFramEx(C函数)去执行py函数
# 首先会创建一个栈帧
# Python里面一切都是对象，栈帧对象，上下文中运行字节码对象

def test():
    pass

def main():
    pass


if __name__ == "__main__":
    main()
    
    print("将Python字节代码反汇编：")
    import dis
    dis.dis(main)