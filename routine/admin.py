from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(routiney)

class Routineadmin(admin.ModelAdmin):
    list_display=['batch','img']