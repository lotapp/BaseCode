# # 官方的解释说，“用if... elif... elif... else序列很容易来实现 switch / case 语句”。而且可以使用函数字典映射和类的调度方法。
# def numbers_to_strings(argument):
#     switcher = {
#         0: "zero",
#         1: "one",
#         2: "two",
#     }
#     return switcher.get(argument, "nothing")

#     # 这段代码类似于：
# function(argument){
#     switch(argument) {
#         case 0:
#             return "zero";
#         case 1:
#             return "one";
#         case 2:
#             return "two";
#         default:
#             return "nothing";
#     };
# };

# 在 Python 中字典映射也可以包含函数或者 lambda 表达式：
# def zero():
#     return "zero"

# def one():
#     return "one"

# def numbers_to_functions_to_strings(argument):
#     switcher = {
#         0: zero,
#         1: one,
#         2: lambda: "two",
#     }
#     func = switcher.get(argument, lambda: "nothing")
#     return func()

#     # 类的调度方法:如果在一个类中，不确定要使用哪种方法，可以用一个调度方法在运行的时候来确定。
#     class Switcher(object):
#     def numbers_to_methods_to_strings(self, argument):
#         method_name = 'number_' + str(argument)
#         method = getattr(self, method_name, lambda: "nothing")
#         return method()

#     def number_0(self):
#         return "zero"

#     def number_1(self):
#         return "one"

#     def number_2(self):
#         return "two"