from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # ข้อมูลพื้นฐาน
    username = models.CharField(max_length=150, unique=True, verbose_name="ชื่อผู้ใช้")
    email = models.EmailField(verbose_name="อีเมล")
    
    # คำนำหน้า
    prefix = models.CharField(max_length=20, blank=True, null=True, verbose_name="คำนำหน้า")
    
    # ชื่อภาษาไทย
    first_name_th = models.CharField(max_length=100, blank=True, null=True, verbose_name="ชื่อ (ไทย)")
    last_name_th = models.CharField(max_length=100, blank=True, null=True, verbose_name="นามสกุล (ไทย)")
    
    # ชื่อภาษาอังกฤษ
    first_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name="ชื่อ (อังกฤษ)")
    last_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name="นามสกุล (อังกฤษ)")
    
    # เบอร์โทรศัพท์
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="เบอร์โทรศัพท์")
    phone_extension = models.CharField(max_length=5, blank=True, null=True, verbose_name="เบอร์โทรศัพท์ 5 หลัก")
    
    # หน่วยงาน
    organize = models.ForeignKey('organize.Organize', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="หน่วยงาน")
    
    # ข้อมูลอื่นๆ
    level = models.CharField(max_length=50, blank=True, null=True, verbose_name="ระดับ")
    
    # ข้อมูลเวลา
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "ผู้ใช้งาน"
        verbose_name_plural = "ผู้ใช้งาน"
        ordering = ['username']

    def get_full_name_th(self):
        """ดึงชื่อเต็มภาษาไทย"""
        if self.first_name_th and self.last_name_th:
            return f"{self.first_name_th} {self.last_name_th}"
        return self.username

    def get_full_name_en(self):
        """ดึงชื่อเต็มภาษาอังกฤษ"""
        if self.first_name_en and self.last_name_en:
            return f"{self.first_name_en} {self.last_name_en}"
        return self.username

    def get_display_name(self):
        """ดึงชื่อที่แสดง (ไทยก่อน, อังกฤษถ้าไม่มีไทย)"""
        if self.first_name_th and self.last_name_th:
            return self.get_full_name_th()
        elif self.first_name_en and self.last_name_en:
            return self.get_full_name_en()
        return self.username
