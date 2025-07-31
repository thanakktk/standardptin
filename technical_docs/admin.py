from django.contrib import admin
from .models import TechnicalDocument

@admin.register(TechnicalDocument)
class TechnicalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'filename', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('ข้อมูลเอกสาร', {
            'fields': ('title', 'description', 'file')
        }),
        ('ข้อมูลเวลา', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
