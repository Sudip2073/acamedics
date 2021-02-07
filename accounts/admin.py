from django.contrib import admin
from .models import *
@admin.register(Student)



class Studentadmin(admin.ModelAdmin):
    list_display=['name','sid','age','year','enrollement','description','profile_pic']



