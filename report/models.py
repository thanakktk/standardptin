from django.db import models
from django.conf import settings
from machine.models import Machine
from calibrate.models import CalibrationForce, CalibrationPressure, CalibrationTorque
from organize.models import Organize
from employee.models import Employee
from std.models import Standard
from datetime import datetime, timedelta

class ReportTemplate(models.Model):
    """โมเดลสำหรับเทมเพลตรายงาน"""
    name = models.CharField(max_length=200, verbose_name="ชื่อเทมเพลต")
    description = models.TextField(blank=True, verbose_name="คำอธิบาย")
    template_type = models.CharField(
        max_length=50,
        choices=[
            ('calibration', 'รายงานการปรับเทียบ'),
            ('machine', 'รายงานเครื่องมือ'),
            ('employee', 'รายงานพนักงาน'),
            ('organization', 'รายงานหน่วยงาน'),
            ('summary', 'รายงานสรุป'),
        ],
        verbose_name="ประเภทเทมเพลต"
    )
    is_active = models.BooleanField(default=True, verbose_name="ใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")
    
    class Meta:
        verbose_name = "เทมเพลตรายงาน"
        verbose_name_plural = "เทมเพลตรายงาน"
    
    def __str__(self):
        return self.name

class ReportSchedule(models.Model):
    """โมเดลสำหรับกำหนดการรายงาน"""
    name = models.CharField(max_length=200, verbose_name="ชื่อกำหนดการ")
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE, verbose_name="เทมเพลต")
    frequency = models.CharField(
        max_length=20,
        choices=[
            ('daily', 'รายวัน'),
            ('weekly', 'รายสัปดาห์'),
            ('monthly', 'รายเดือน'),
            ('quarterly', 'ราย 3 เดือน'),
            ('yearly', 'รายปี'),
        ],
        verbose_name="ความถี่"
    )
    recipients = models.TextField(verbose_name="ผู้รับรายงาน (อีเมล)")
    is_active = models.BooleanField(default=True, verbose_name="ใช้งาน")
    last_run = models.DateTimeField(null=True, blank=True, verbose_name="รันครั้งล่าสุด")
    next_run = models.DateTimeField(null=True, blank=True, verbose_name="รันครั้งถัดไป")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    
    class Meta:
        verbose_name = "กำหนดการรายงาน"
        verbose_name_plural = "กำหนดการรายงาน"
    
    def __str__(self):
        return self.name

class ReportLog(models.Model):
    """โมเดลสำหรับบันทึกการสร้างรายงาน"""
    report_type = models.CharField(max_length=50, verbose_name="ประเภทรายงาน")
    generated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="สร้างโดย")
    generated_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    file_path = models.CharField(max_length=500, blank=True, verbose_name="เส้นทางไฟล์")
    file_size = models.IntegerField(default=0, verbose_name="ขนาดไฟล์ (bytes)")
    status = models.CharField(
        max_length=20,
        choices=[
            ('success', 'สำเร็จ'),
            ('failed', 'ล้มเหลว'),
            ('processing', 'กำลังประมวลผล'),
        ],
        default='processing',
        verbose_name="สถานะ"
    )
    error_message = models.TextField(blank=True, verbose_name="ข้อความผิดพลาด")
    
    class Meta:
        verbose_name = "บันทึกรายงาน"
        verbose_name_plural = "บันทึกรายงาน"
        ordering = ['-generated_at']
    
    def __str__(self):
        return f"{self.report_type} - {self.generated_at.strftime('%Y-%m-%d %H:%M')}"

class DashboardWidget(models.Model):
    """โมเดลสำหรับ widget ในแดชบอร์ด"""
    name = models.CharField(max_length=200, verbose_name="ชื่อ widget")
    widget_type = models.CharField(
        max_length=50,
        choices=[
            ('chart', 'กราฟ'),
            ('table', 'ตาราง'),
            ('metric', 'ตัวชี้วัด'),
            ('list', 'รายการ'),
        ],
        verbose_name="ประเภท widget"
    )
    data_source = models.CharField(max_length=100, verbose_name="แหล่งข้อมูล")
    position = models.IntegerField(default=0, verbose_name="ตำแหน่ง")
    is_active = models.BooleanField(default=True, verbose_name="ใช้งาน")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    
    class Meta:
        verbose_name = "Widget แดชบอร์ด"
        verbose_name_plural = "Widget แดชบอร์ด"
        ordering = ['position']
    
    def __str__(self):
        return self.name
