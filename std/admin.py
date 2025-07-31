from django.contrib import admin
from .models import Standard

@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name",) 