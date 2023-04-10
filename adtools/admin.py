from django.contrib import admin

from .models import News, FCMDevice

admin.site.register(News)
admin.site.register(FCMDevice)