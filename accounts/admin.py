from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserRole
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
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_role', 'groups', 'user_permissions')
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
        ('สิทธิ์การใช้งาน', {
            'fields': ('user_role',)
        }),
    )
    
    readonly_fields = ('last_login', 'date_joined', 'created_at', 'updated_at')

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('name',)
    
    fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('name', 'description')
        }),
        ('สิทธิ์เครื่องมือ', {
            'fields': ('can_view_machine', 'can_add_machine', 'can_edit_machine', 'can_delete_machine', 'can_send_notification')
        }),
        ('สิทธิ์สอบเทียบ', {
            'fields': ('can_view_calibration', 'can_add_calibration', 'can_edit_calibration', 'can_delete_calibration')
        }),
        ('สิทธิ์หน่วยงาน', {
            'fields': ('can_view_organization', 'can_manage_organization')
        }),
        ('สิทธิ์ผู้ใช้', {
            'fields': ('can_view_users', 'can_manage_users')
        }),
        ('สิทธิ์เครื่องมือสอบเทียบ', {
            'fields': ('can_view_equipment', 'can_manage_equipment')
        }),
        ('สิทธิ์เอกสารเทคนิค', {
            'fields': ('can_view_technical_docs', 'can_manage_technical_docs')
        }),
        ('สิทธิ์รายงาน', {
            'fields': ('can_view_reports', 'can_export_reports', 'can_edit_reports', 'can_download_certificates')
        }),
        ('สิทธิ์เพิ่มเติม', {
            'fields': ('can_change_priority', 'can_close_work')
        }),
        ('สิทธิ์ระบบ', {
            'fields': ('can_access_admin',)
        }),
    )

admin.site.unregister(Group)
