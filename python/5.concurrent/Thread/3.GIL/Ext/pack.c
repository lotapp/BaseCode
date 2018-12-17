#include "Python.h" // 引入Python提供的头文件
#include "dnt.h"    // 引入自己定义的头文件

// 模块名_函数名（调用的时候：dnt.fib(30)）
// 相当于：定义Python对应的函数名
static PyObject *dnt_fib(PyObject *self, PyObject *args)
{
    int num;
    // 把Python类型转换成C类型（用户传过来的参数）
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;

    // 把C返回类型转换成Python类型（PS:python定义变量不加修饰符）
    // result = (PyObject *)Py_BuildValue("i", fib(num));
    return (PyObject *)Py_BuildValue("i", fib(num));
}

// 这个就是一个映射关系（Python函数和C函数对应）
static PyMethodDef dntMethods[] = {
    // {"函数名", 模块名_函数名, METH_VARARGS, "函数描述"},
    // METH_VARARGS：告诉解释器调用约定用于C函数的标志
    {"fib", dnt_fib, METH_VARARGS, "fib函数"}, // dnt.fib.__doc__
    {NULL, NULL, 0, NULL} // 固定格式
};

// 模块定义
static struct PyModuleDef dntModule = {
    PyModuleDef_HEAD_INIT,
    "dnt",
    NULL, // 模块文档
    -1,
    dntMethods // 映射数组
};

// 相当于init方法 PyMODINIT_FUNC
void PyInit_dnt(void)
{
    PyModule_Create(&dntModule);
}

// Python2
// void initdnt(void)
// {
//     Py_InitModule("dnt", dntMethods);
// }