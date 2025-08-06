from django.db import models
from django.utils import timezone
import os
import unicodedata
import uuid

def get_upload_path(instance, filename):
    """สร้าง path สำหรับอัพโหลดไฟล์"""
    # สร้างชื่อไฟล์ที่ไม่ซ้ำกัน
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('technical_docs', filename)

class TechnicalDocument(models.Model):
    title = models.CharField(max_length=200, verbose_name="ชื่อเอกสาร")
    description = models.TextField(blank=True, null=True, verbose_name="คำอธิบาย")
    file = models.FileField(upload_to=get_upload_path, verbose_name="ไฟล์เอกสาร")
    original_filename = models.CharField(max_length=255, blank=True, verbose_name="ชื่อไฟล์ต้นฉบับ")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")

    class Meta:
        verbose_name = "เอกสารเทคนิค"
        verbose_name_plural = "เอกสารเทคนิค"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # บันทึกชื่อไฟล์ต้นฉบับเมื่ออัพโหลด
        if self.file and not self.original_filename:
            self.original_filename = self.file.name.split('/')[-1]
        super().save(*args, **kwargs)

    def filename(self):
        """ดึงชื่อไฟล์จาก path"""
        return os.path.basename(self.file.name)
    
    def safe_filename(self):
        """สร้างชื่อไฟล์ที่ปลอดภัยสำหรับการดาวน์โหลด"""
        # ใช้ชื่อไฟล์ต้นฉบับถ้ามี
        if self.original_filename:
            filename = self.original_filename
        else:
            filename = self.filename()
        
        # แปลงชื่อไฟล์ให้เป็นรูปแบบที่ปลอดภัย
        # ลบอักขระพิเศษและแทนที่ด้วย underscore
        safe_name = unicodedata.normalize('NFKD', filename)
        safe_name = ''.join(c for c in safe_name if c.isalnum() or c in '._-')
        return safe_name
