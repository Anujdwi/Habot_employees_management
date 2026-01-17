from django.contrib import admin
from .models import Employee

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'role', 'date_joined')
    search_fields = ('name', 'email', 'department', 'role')