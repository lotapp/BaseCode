def meta_fun(class_name, parent_class_tuple, class_attr_dict):
    print(class_name, parent_class_tuple, class_attr_dict, sep="\n")
    # 这个就是默认做的事情，我这边只是演示一下，指定了metaclass就会使用自定义的方法或者类
    return type(class_name, parent_class_tuple, class_attr_dict)


class People(object):
    location = "地球"


class China(object):
    skin = "黄皮肤"


class Student(People, China, metaclass=meta_fun):
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
