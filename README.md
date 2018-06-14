# BaseCode
编程入门（NetCore、Python、Go、C++等）

---
# 说下Markdown语法
逆天推荐使用VSCode编写
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180614105020550-1158788761.png)

装这个插件写作更方便：
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180614105155394-2020058665.png)

<a name="divtop"></a>
内含：锚点使用，使用HTML，新页面跳转，目录生成

## 启用方式：
![](https://images2018.cnblogs.com/blog/1127869/201806/1127869-20180613213802314-1149663484.png)
## H1~H3(#的个数)[博客园只支持H1~3]
```
# H1
## H2
### H3
```
# H1
## H2
### H3

## 斜体(一个\*斜体)，加粗(两个\*粗体)，删除线（两个\~）
```
**加粗内容** 其他内容 *斜体内容* ~~删除内容~~
```
**加粗内容** 其他内容 *斜体内容* ~~删除内容~~

## 引用(> or >>)、代码块(\```开头结尾)、分隔符(\---)、换行(空一行 或者 br标签 )、转义( \\ )
引用：
```
>引用 | 块注释
>从前有座山，山里有座庙
>>里面再来个引用
```
>引用 | 块注释
>从前有座山，山里有座庙
>>里面再来个引用

代码块：
以\```(反引号)开头
以\```(～下面的符合)结尾

如果要语法高亮就在\```后面加小写语言名,eg:html,css,javascript,python,cs(csharp)等等
```python
print("以 ```python开头，```结尾")
```
```cs
var infos_list = new List<object>() { "C#", "JavaScript" };
```
```csharp
var infos_list = new List<object>() { "C#", "JavaScript" };
```

分隔符：
```
---
```
---

换行：
```
<br/>
<br/>
<br/>
```
<br/>
<br/>
<br/>

转义字符
```
\<br/>
```
\<br/>

## HTML代码
直接写HTML就可以解析：
```html
<div>
    <code>
        print("mmd")
    </code>
</div>
```
<div>
    <code>
        print("mmd")
    </code>
</div>

## 超链接、图片、锚点跳转
超链接：
```
页面内打开：[超链接文字](url)
写法1：
汇总系列：[链接](https://www.cnblogs.com/dunitian/p/4822808.html#ai)

写法2：
汇总系列：<https://www.cnblogs.com/dunitian/p/4822808.html#ai>
```

汇总系列：[https://www.cnblogs.com/dunitian/p/4822808.html#ai](https://www.cnblogs.com/dunitian/p/4822808.html#ai)

汇总系列：<https://www.cnblogs.com/dunitian/p/4822808.html#ai>
---
```
新页面打开：[超链接文字](url){:target="_blank"} （有些编辑器不支持，Python Markdown可以使用）
不支持就用：<a href="xxx" target="_blank">xxx</a>

写法1：
汇总系列：[链接](https://www.cnblogs.com/dunitian/p/4822808.html#ai){:target="_blank"}

写法2：
汇总系列：<https://www.cnblogs.com/dunitian/p/4822808.html#ai>{:target="_blank"}

写法3：
汇总系列：<a href="https://www.cnblogs.com/dunitian/p/4822808.html#ai" target="_blank">链接</a>
```
汇总系列：[https://www.cnblogs.com/dunitian/p/4822808.html#ai](https://www.cnblogs.com/dunitian/p/4822808.html#ai){:target="_blank"}

汇总系列：<https://www.cnblogs.com/dunitian/p/4822808.html#ai>{:target="_blank"}

汇总系列：<a href="https://www.cnblogs.com/dunitian/p/4822808.html#ai" target="_blank">https://www.cnblogs.com/dunitian/p/4822808.html#ai</a>

---
图片：(感叹号别忘记了)
```
![alt标题](url地址)
![博客园logo](https://www.cnblogs.com/images/logo_small.gif)
```
![博客园logo](https://www.cnblogs.com/images/logo_small.gif)

锚点：（不能实现的就用html实现即可）
```
我在正文开头定义了一个：<a name="divtop"></a>
我们跳转过去：[跳转指定位置](#divtop)
```
[跳转指定位置](#divtop)

## 列表(无序\- 有序 1.2.3. 注意空格)
```
- 无序列表1
    - 无序列表1.1
    - 无序列表1.2
        - 1.2.1
- 无序列表2
    1. 有序列表1
    2. 有序列表2
    3. 有序列表3
        1. 3.1
        2. 3.2
            1. 3.2.1
            2. 3.2.2
- 无序列表3
```
- 无序列表1
    - 无序列表1.1
    - 无序列表1.2
        - 1.2.1
- 无序列表2
    1. 有序列表1
    2. 有序列表2
    3. 有序列表3
        1. 3.1
        2. 3.2
            - 3.2.1
            - 3.2.2
- 无序列表3

## 目录生成就用js实现了，MarkDown的方式太累
博客园上传js文件，然后引用即可
```javascript
$(function () {
    // 生成目录索引列表
    var mainContent = $('#cnblogs_post_body');
    var h2_list = $('#cnblogs_post_body h2');//如果你的章节标题不是h2,只需要将这里的h2换掉即可

    if (mainContent.length < 1)
        return;

    if (h2_list.length > 0) {
        var content = '<a name="_labelTop"></a>';
        content += '<div id="navCategory">';
        content += '<p style="font-size:18px"><b>目录</b></p>';
        content += '<ul>';
        for (var i = 0; i < h2_list.length; i++) {
            var go_to_top = '<div style="text-align: right"><a href="#_labelTop">回到顶部</a><a name="_label' + i + '"></a></div>';
            $(h2_list[i]).before(go_to_top);

            var h3_list = $(h2_list[i]).nextAll("h3");
            var li3_content = '';
            for (var j = 0; j < h3_list.length; j++) {
                var tmp = $(h3_list[j]).prevAll('h2').first();
                if (!tmp.is(h2_list[i]))
                    break;
                var li3_anchor = '<a name="_label' + i + '_' + j + '"></a>';
                $(h3_list[j]).before(li3_anchor);
                li3_content += '<li><a href="#_label' + i + '_' + j + '">' + $(h3_list[j]).text() + '</a></li>';
            }

            var li2_content = '';
            if (li3_content.length > 0)
                li2_content = '<li><a href="#_label' + i + '">' + $(h2_list[i]).text() + '</a><ul>' + li3_content + '</ul></li>';
            else
                li2_content = '<li><a href="#_label' + i + '">' + $(h2_list[i]).text() + '</a></li>';
            content += li2_content;
        }
        content += '</ul>';
        content += '</div><p>&nbsp;</p>';
        content += '<p style="font-size:18px"><b>正文</b></p>';
        if ($('#cnblogs_post_body').length != 0) {
            $($('#cnblogs_post_body')[0]).prepend(content);
        }
    }
    var allinfo = '<p><strong>汇总系列：<a href="https://www.cnblogs.com/dotnetcrazy/p/9160514.html" target="_blank">https://www.cnblogs.com/dotnetcrazy/p/9160514.html</a></strong></p>';
    $(mainContent[0]).prepend(allinfo);
});
```

## 更多语法请参考
<https://www.cnblogs.com/dotnetcrazy/p/9180295.html>
