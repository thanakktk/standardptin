from django.db import models
from machine.models import Machine

class Certificate(models.Model):
    cert_no = models.CharField(max_length=50, unique=True, verbose_name="เลขที่ใบรับรอง")
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือ")
    issue_date = models.DateField(verbose_name="วันที่ออกใบรับรอง")
    expire_date = models.DateField(blank=True, null=True, verbose_name="วันหมดอายุ")
    file = models.FileField(upload_to='certificates/', blank=True, null=True, verbose_name="ไฟล์ใบรับรอง")
    remark = models.TextField(blank=True, null=True, verbose_name="หมายเหตุ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไขล่าสุด")

    def __str__(self):
        return self.cert_no

    class Meta:
        verbose_name = "ใบรับรองการสอบเทียบ"
        verbose_name_plural = "ใบรับรองการสอบเทียบ"
