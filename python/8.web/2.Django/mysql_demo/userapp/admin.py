from django.contrib import admin
from userapp import models

admin.site.site_header = u"欢迎来到逸鹏说道"
admin.site.site_title = u"逸鹏说道后台"

# Register your models here.
admin.site.register(models.Express)
admin.site.register(models.ExpressOrder)


# 文件上传
class FileInfoAdmin(admin.ModelAdmin):
    list_display = ["file_md5", "createtime", "updatetime", "datastatus"]
    readonly_fields = ["file_md5"]


admin.site.register(models.FileInfo, FileInfoAdmin)


# 买家订单
class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "createtime", "updatetime", "datastatus"]
    readonly_fields = ["order_id", "datastatus"]


admin.site.register(models.Order, OrderAdmin)
