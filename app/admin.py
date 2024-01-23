from django.contrib import admin

# Register your models here.

from app.models import *

class Custom(admin.ModelAdmin):
    list_display = ['username','address','profile_pic']

admin.site.register(Profile,Custom)