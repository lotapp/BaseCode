from django.db import models
import time


# 用户信息表
class UserInfo(models.Model):
    # 字符串类型，最大长度为20
    name = models.CharField(max_length=20)
    # 创建时间：日期类型
    create_time = models.DateTimeField()
    # 更新时间
    update_time = models.DateTimeField(default=time.time())
    # 用户状态（0游客 1正常 99删除）
    datastatus = models.SmallIntegerField(default=0)

    # def __str__(self):
    #     """为了后台管理页面的美化"""
    #     return self.name
