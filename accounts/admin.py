from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import Group

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'get_display_name', 'organize', 'phone', 'is_active', 'date_joined')
    list_filter = ('is_active', 'is_staff', 'organize', 'date_joined')
    search_fields = ('username', 'email', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en')
    ordering = ('username',)
    
    fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('username', 'email', 'password')
        }),
        ('ข้อมูลส่วนตัว', {
            'fields': ('prefix', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en')
        }),
        ('ข้อมูลติดต่อ', {
            'fields': ('phone', 'phone_extension', 'organize')
        }),
        ('สิทธิ์การใช้งาน', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('ข้อมูลเวลา', {
            'fields': ('last_login', 'date_joined', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    add_fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        ('ข้อมูลส่วนตัว', {
            'fields': ('prefix', 'first_name_th', 'last_name_th', 'first_name_en', 'last_name_en')
        }),
        ('ข้อมูลติดต่อ', {
            'fields': ('phone', 'phone_extension', 'organize')
        }),
    )
    
    readonly_fields = ('last_login', 'date_joined', 'created_at', 'updated_at')

admin.site.unregister(Group)
