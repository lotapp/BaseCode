class MetaClass(type):
    # 在__init__之前执行（__new__：创建对象并返回【单例模式会用到】）
    def __new__(cls, class_name, parent_class_tuple, class_attr_dict):
        print(class_name, parent_class_tuple, class_attr_dict, sep="\n")

        return type(class_name, parent_class_tuple, class_attr_dict)
        # 也可以这么做：type.__new__(cls,x,x,x)
        # return super().__new__(cls, class_name, parent_class_tuple, class_attr_dict)


class People(object):
    location = "地球"


class China(object):
    skin = "黄皮肤"


class Student(People, China, metaclass=MetaClass):
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def show(self):
        print(self.name, self.age, self.school)


def main():
    xiaoming = Student("小明", 25, "中科院")
    xiaoming.show()


if __name__ == "__main__":
    main()
