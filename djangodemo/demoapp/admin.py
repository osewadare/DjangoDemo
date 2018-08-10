from django.contrib import admin
from .models import Student

#Inherits Admin Class from ModelAdmin
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name']

#Registers Admin Class
admin.site.register(Student, StudentAdmin)