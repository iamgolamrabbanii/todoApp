from django.contrib import admin
from .models import database

class reg(admin.ModelAdmin):
    details = "task_title", "task_description"
admin.site.register(database, reg)