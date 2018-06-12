using System;
using System.Collections.Generic;

namespace _5dict
{
    public static class Program
    {
        private static void Main()
        {
            #region Dict
            // infos_dict={"name":"dnt","web":"dkill.net"}
            // # # 遍历
            // # for item in infos_dict.keys():
            // #     print(item)
            // # for item in infos_dict.values():
            // #     print(item)
            // # for item in infos_dict.items():
            // #     print("Key:%s,Value:%s"%(item[0],item[1]))
            // # #每一次相当于取一个元组，那可以用之前讲的例子来简化了：c,d=a #等价于：c=a[0] d=a[1]
            // # for k,v in infos_dict.items():
            // #     print("Key:%s,Value:%s"%(k,v))
            var infos_dict = new Dictionary<string, object>{
                {"name","dnt"},
                {"web","dkill.net"}
            };
            // foreach (var item in infos_dict.Keys)
            // {
            //     System.Console.WriteLine(item);
            // }
            // foreach (var item in infos_dict.Values)
            // {
            //     System.Console.WriteLine(item);
            // }
            // foreach (KeyValuePair<string, object> kv in infos_dict)
            // {
            //     //Console.WriteLine("Key:%s,Value:%s",(kv.Key,kv.Value));
            //     Console.WriteLine($"Key:{kv.Key},Value:{kv.Value}");
            // }

            // // # # 增加 修改 (有就修改，没就添加)
            // // # # 添加
            // // # infos_dict["wechat"]="lll"
            // // # print(infos_dict)
            infos_dict.Add("wechat", "lll");
            infos_dict["wechat1"] = "lll";
            // // # # 修改
            // // # infos_dict["wechat"]="dotnetcrazy"
            // // # print(infos_dict)
            infos_dict["wechat"] = "dotnetcrazy";

            // // # # 删除
            // // # del infos_dict["name"]
            // // # del infos_dict["dog"] #不存在就报错
            // // # print(infos_dict)
            infos_dict.Remove("name");
            infos_dict.Remove("dog");//不存在不报错
            // // # #清空列表内容
            // // # infos_dict.clear()
            // // # print(infos_dict)
            infos_dict.Clear();
            // // # # 删除列表
            // // # del infos_dict

            // # 查询
            // infos_dict["name"]
            // infos_dict["mmd"] #查不到就异常            

            // infos_dict.get("name")
            // infos_dict.get("mmd")#查不到不会异常
            Console.WriteLine(infos_dict["name"]);
            // Console.WriteLine(infos_dict["mmd"]); //#查不到就异常
            // 先看看有没有 ContainsKey(key),看值就 ContainsValue(value)
            if (infos_dict.ContainsKey("mmd")) Console.WriteLine(infos_dict["mmd"]);

            // # 查看帮助
            // help(infos_dict)
            // len(infos_dict) #有几对key,value
            Console.WriteLine(infos_dict.Count);

            #endregion

            // Console.Read();
        }
    }
}