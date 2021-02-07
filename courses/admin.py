from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Modules)

class ModulesAdmin(admin.ModelAdmin):
    list_display=['name','year','mod_code','description','credit']
