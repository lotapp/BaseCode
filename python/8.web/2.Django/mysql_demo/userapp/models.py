from django.db import models
import uuid


# editable=False

# 快递公司表（一）
# https://www.kuaidi100.com/query?type=&postid=
# https://sp0.baidu.com/9_Q4sjW91Qh3otqbppnN2DJv/pae/channel/data/asyncqury?appid=4001&com=huitongkuaidi&nu=71330102164040
class Express(models.Model):
    # 快递编号
    ecode = models.CharField(max_length=20, blank=True, verbose_name="快递编号")

    # 公司名（创建索引）
    # 顺丰快递、圆通快递、韵达快递、中通快递、申通快递、百世快递、天天快递、邮政EMS、
    # 京东物流、德邦快递、优速快递、安能快递、快捷快递、其他快递
    ename = models.CharField(max_length=10, db_index=True, verbose_name="快递名称")

    # 快递100的快递类型
    etype = models.CharField(max_length=20, default="other", verbose_name="快递100对应的类型")

    # 快递显示顺序（默认都是9，以后可能用到）
    esort = models.SmallIntegerField(default=9, blank=True, verbose_name="快递排序")

    # 创建时间 auto_now_add：当对象第一次被创建时自动设置当前时间
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间 auto_now：每次保存对象时自动设置该字段为当前时间
    updatetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # 数据状态（0：访客/冻结，1：正常，99：删除
    datastatus = models.SmallIntegerField(default=1, verbose_name="数据状态", help_text="默认为1，99代表数据被删除")

    class Meta:
        # 表名默认为app名_小写类名
        # db_table = "express"
        # Express在admin管理页面显示为啥
        verbose_name = "快递公司"  # 单数显示
        verbose_name_plural = verbose_name  # 复数显示


# 买家寄过来的物流信息（多）
class ExpressOrder(models.Model):
    # 物流id（创建索引）
    express_num = models.CharField(max_length=40, db_index=True, verbose_name="物流编号", help_text="您的物流信息")

    # 快递对象（物流信息和快递公司是多对一的关系）PS：数据库中就是一个指向快递公司表的外键
    # models.CASCADE：级联删除（以前的默认值）eg：快递公司删除，则对应的快递订单都删除
    express = models.ForeignKey("Express", on_delete=models.CASCADE)

    # 创建时间 auto_now_add：当对象第一次被创建时自动设置当前时间
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间 auto_now：每次保存对象时自动设置该字段为当前时间
    updatetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # 数据状态（0：访客/冻结，1：正常，99：删除
    datastatus = models.SmallIntegerField(default=1, verbose_name="数据状态", help_text="默认为1，99代表数据被删除")

    class Meta:
        verbose_name = "物流信息"  # 单数显示
        verbose_name_plural = verbose_name  # 复数显示


class FileInfo(models.Model):
    # 文件对应的md5码
    file_md5 = models.CharField(max_length=32, verbose_name="文件MD5", help_text="同一文件MD5相同")

    # file_url =models.FilePathField(path="/files",verbose_name="上传文件")

    # 创建时间 auto_now_add：当对象第一次被创建时自动设置当前时间
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间 auto_now：每次保存对象时自动设置该字段为当前时间
    updatetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # 数据状态（0：访客/冻结，1：正常，99：删除
    datastatus = models.SmallIntegerField(default=1, verbose_name="数据状态", help_text="默认为1，99代表数据被删除")

    class Meta:
        verbose_name = "文件信息"  # 单数显示
        verbose_name_plural = verbose_name  # 复数显示


# 买家订单
class Order(models.Model):
    # 用户订单id（索引）自动生成  editable=False
    order_id = models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name="订单编号",
                                help_text="该编号是系统自动生成")

    # files = models.

    # 创建时间 auto_now_add：当对象第一次被创建时自动设置当前时间
    createtime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 更新时间 auto_now：每次保存对象时自动设置该字段为当前时间
    updatetime = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    # 数据状态（0：访客/冻结，1：正常，99：删除
    datastatus = models.SmallIntegerField(default=1, verbose_name="数据状态", help_text="默认为1，99代表数据被删除")

    class Meta:
        verbose_name = "买家订单"  # 单数显示
        verbose_name_plural = verbose_name  # 复数显示

# from django.db import connection
# print(connection.queries[-1])

# QuerySet的query属性查看转化成的sql语句
# xx.objects.all().query

# 查看日志开启的状态和log文件路径
# show variables like '%general_log%';
