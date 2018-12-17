#include <stdio.h>

// 模拟一个耗cpu的操作
int fib(int n)
{
    if (n < 3)
        return 1;
    return fib(n - 1) + fib(n - 2);
}

int main(void)
{
    printf("fib(30)=%d == 832040\n", fib(30));
    return 0;
}