from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "organize", "position", "phone", "email", "created_at", "updated_at")
    search_fields = ("name", "position", "phone", "email")
