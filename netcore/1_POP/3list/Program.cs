using System;
using System.Collections.Generic;
using System.Linq;

// http://www.cnblogs.com/dotnetcrazy/p/9155310.html
namespace _3list
{
    public static class Program
    {
        private static void Main()
        {
            #region List
            //# 定义一个列表
            // # infos_list=["C#","JavaScript"]#[]
            var infos_list = new List<object>() { "C#", "JavaScript" };
            var infos_list2 = new List<object>() { "张三", 21 };
            // // # ###########################################################
            // // # # 遍历 for while
            // // # for item in infos_list:
            // // #     print(item)
            foreach (var item in infos_list)
            {
                System.Console.WriteLine(item);
            }
            for (int i = 0; i < infos_list.Count; i++)
            {
                System.Console.WriteLine(infos_list[i]);
            }
            // # i=0
            // # while i<len(infos_list):
            // #     print(infos_list[i])
            // #     i+=1
            int j=0;
            while(j<infos_list.Count){
               Console.WriteLine(infos_list[j++]);
            }
            // # ###########################################################
            // # # 增加
            // # # 末尾追加
            // # infos_list.append("Java")
            // # print(infos_list)
            DivPrintList(infos_list);

            infos_list.Add("Java");
            DivPrintList(infos_list);
            // # # 指定位置插入
            // # infos_list.insert(0,"Python")
            // # print(infos_list)
            infos_list.Insert(0,"Python");
            DivPrintList(infos_list);
            // # # 添加一个列表
            // # infos_list2=["张三",21]#python里面的列表类似于List<object>            
            // # infos_list.extend(infos_list2)
            // # print(infos_list)
            infos_list.AddRange(infos_list2);
            DivPrintList(infos_list);
            /*C#有insertRange方法 */
            DivPrintList(infos_list2,"List2原来的列表：");
            infos_list2.InsertRange(0,infos_list);
            DivPrintList(infos_list2,"List2变化后列表：");
            // # # help(infos_list.extend)#可以查看etend方法描述
            // # ###########################################################
            // # # 删除
            // # # pop()删除最后一个元素，返回删掉的元素
            // # # pop(index) 删除指定下标元素
            // # print(infos_list.pop())
            // # print(infos_list)
            // # print(infos_list.pop(1))
            // # # print(infos_list.pop(10)) #不存在就报错
            // # print(infos_list)

            // # # remove("")删除指定元素
            // # infos_list.remove("张三")
            // # # infos_list.remove("dnt") #不存在就报错
            // # print(infos_list)

            // # # del xxx[index] 删除指定下标元素
            // # del infos_list[1]
            // # print(infos_list)
            // # # del infos_list[10] #不存在就报错

            // # del infos_list #删除集合（集合再访问就不存在了）

            DivPrintList(infos_list);
            infos_list.RemoveAt(1);
            // infos_list.RemoveAt(10);//不存在则报错
            // infos_list.RemoveRange(0,1); //可以移除多个
            DivPrintList(infos_list);
            infos_list.Remove("我家在东北吗？"); //移除指定item，不存在不会报错
            DivPrintList(infos_list,"清空前：");
            infos_list.Clear();//清空列表
            DivPrintList(infos_list,"清空后：");

            // # ###########################################################
            // # # 修改 xxx[index]=xx
            // # # 注意：一般不推荐在for循环里面修改
            // # print(infos_list2)
            // # infos_list2[1]="PHP" #只有下标修改一种方式
            // # # infos_list2[3]="GO" #不存在则异常
            // # print(infos_list2)
            DivPrintList(infos_list2);
            infos_list2[1] = "PHP";
            // infos_list2[3]="GO"; //不存在则异常
            DivPrintList(infos_list2);
            // # # 想按值修改需要先查下标再修改
            // # infos_list2.index("张三")
            // # infos_list2[0]="GO"
            // # print(infos_list2)
            // # # infos_list2.index("dnt")#不存在则异常
            int index = infos_list2.IndexOf("张三");
            infos_list2[index] = "GO";
            DivPrintList(infos_list2);
            infos_list2.IndexOf("dnt");//不存在返回-1

            // ###########################################################
            // # 查询 in, not in, index, count
            // # # for扩展：https://www.cnblogs.com/dotnetcrazy/p/9102030.html#forelse
            // # names_list=["张三","李四","王二麻子"]
            var names_list=new List<string>(){"张三","李四","王二麻子"};
            // Console.WriteLine(names_list.Find(i=>i=="张三"));
            // Console.WriteLine(names_list.FirstOrDefault(i=>i=="张三"));
            Console.WriteLine(names_list.Exists(i=>i=="张三"));
            System.Console.WriteLine(names_list.Contains("张三"));
            // # #张三在列表中执行操作
            // # if "张三" in names_list:
            // #     names_list.remove("张三")
            // # else:
            // #     print(names_list)

            // # #查看"大舅子"不在列表中执行操作
            // # if "大舅子" not in names_list:
            // #     names_list.append("大舅子")
            // # else:
            // #     print(names_list)

            // # #查询王二麻子的索引
            // # print(names_list.index("王二麻子"))
            // names_list.IndexOf("王二麻子");

            // # print(names_list.count("大舅子")) 
            // # print(names_list.count("逆天")) 
            // Console.WriteLine(names_list.Count);

            // ###########################################################
            // # # 排序(sort, reverse 逆置)
            // # num_list=[1,3,5,88,7]
            var num_list = new List<object>() { 1, 3, 5, 88, 7 };

            // # #倒序
            // # num_list.reverse()
            // # print(num_list)
            num_list.Reverse();
            DivPrintList(num_list);
            // # # 从小到大排序
            // # num_list.sort()
            // # print(num_list)
            num_list.Sort();
            DivPrintList(num_list);

            // # # 从大到小
            // # num_list.sort(reverse=True)
            // # print(num_list)
            num_list.Sort();
            num_list.Reverse();
            DivPrintList(num_list);

            // # ###########################################################

            // # #列表嵌套(列表也是可以嵌套的)
            // # num_list2=[33,44,22]
            // # num_list.append(num_list2)
            // # print(num_list)
            var num_list2 = new List<object>() { 33, 44, 22,new List<object>(){11,55,77} };
            DivPrintList(num_list2);//可以定义多维数组来支持 num_list2[i][j]
            // # for item in num_list:
            // #     print(item)
            // # ###########################################################

            // # # 引入Null==>None
            // # a=[1,2,3,4]
            // # b=[5,6]
            // # a=a.append(b)#a.append(b)没有返回值
            // # print(a)#None
            #endregion

            // Console.Read();
        }

        private static void DivPrintList(List<object> list, string say = "")
        {
            Console.WriteLine($"\n{say}");
            foreach (var item in list)
            {
                System.Console.Write($"{item} ");
            }
        }
    }
}