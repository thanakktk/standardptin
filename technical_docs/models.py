from django.db import models
from django.utils import timezone

class TechnicalDocument(models.Model):
    title = models.CharField(max_length=200, verbose_name="ชื่อเอกสาร")
    description = models.TextField(blank=True, null=True, verbose_name="คำอธิบาย")
    file = models.FileField(upload_to='technical_docs/', verbose_name="ไฟล์เอกสาร")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")

    class Meta:
        verbose_name = "เอกสารเทคนิค"
        verbose_name_plural = "เอกสารเทคนิค"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def filename(self):
        return self.file.name.split('/')[-1]
