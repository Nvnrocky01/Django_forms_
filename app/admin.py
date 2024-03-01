from django.contrib import admin

# Register your models here.

from app.models import *

class Custmizewebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url']

admin.site.register(Topic)
admin.site.register(Webpage,Custmizewebpage)
admin.site.register(AcessRecord)
