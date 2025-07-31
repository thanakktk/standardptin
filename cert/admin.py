from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("cert_no", "machine", "issue_date", "expire_date", "file", "remark", "created_at", "updated_at")
    search_fields = ("cert_no", "machine__name")
