from django.contrib import admin

# Register your models here.
# from users.models import UserInfo Django1.x

from .models import UserInfo  # Django2.x


# 自定义模型管理页面
class UserInfoAdmin(admin.ModelAdmin):
    # 自定义管理页面的列表显示字段（和类属性相对应）
    list_display = ["id", "name", "create_time", "update_time", "datastatus"]


# 注册模型类和模型管理类（自动生成后台管理页面）
admin.site.register(UserInfo, UserInfoAdmin)
