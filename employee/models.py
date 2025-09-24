from django.db import models
from organize.models import Organize

class Employee(models.Model):
    organize = models.ForeignKey(Organize, on_delete=models.CASCADE, verbose_name="หน่วยงาน")
    name = models.CharField(max_length=100, verbose_name="ชื่อพนักงาน")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="ตำแหน่ง")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="เบอร์โทรศัพท์")
    email = models.EmailField(blank=True, null=True, verbose_name="อีเมล")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไขล่าสุด")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ผู้ใช้งาน"
        verbose_name_plural = "ผู้ใช้งาน"
