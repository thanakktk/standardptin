from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organize(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อหน่วยงาน")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="หน่วยงานหลัก")
    is_main_unit = models.BooleanField(default=False, verbose_name="เป็นหน่วยงานหลัก")
    address = models.TextField(blank=True, null=True, verbose_name="ที่อยู่")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="เบอร์โทรศัพท์")
    email = models.EmailField(blank=True, null=True, verbose_name="อีเมล")
    users = models.ManyToManyField(User, blank=True, verbose_name="ผู้ใช้งาน", related_name='organizations')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไขล่าสุด")

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} - {self.name}"
        return self.name

    class Meta:
        verbose_name = "หน่วยงาน"
        verbose_name_plural = "หน่วยงาน"
        ordering = ['name']

    def get_sub_units(self):
        """ดึงหน่วยงานย่อยทั้งหมด"""
        return Organize.objects.filter(parent=self)

    def get_all_sub_units(self):
        """ดึงหน่วยงานย่อยทั้งหมดแบบ recursive"""
        sub_units = self.get_sub_units()
        for sub_unit in sub_units:
            sub_units = sub_units.union(sub_unit.get_all_sub_units())
        return sub_units
