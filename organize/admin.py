from django.contrib import admin
from .models import Organize

@admin.register(Organize)
class OrganizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_main_unit', 'phone', 'email', 'created_at')
    list_filter = ('is_main_unit', 'parent', 'created_at')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('users',)
    
    fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('name', 'parent', 'is_main_unit')
        }),
        ('ข้อมูลติดต่อ', {
            'fields': ('address', 'phone', 'email')
        }),
        ('ผู้ใช้งาน', {
            'fields': ('users',)
        }),
        ('ข้อมูลเวลา', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        """แสดงเฉพาะหน่วยงานที่ผู้ใช้มีสิทธิ์เข้าถึง"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(users=request.user)
