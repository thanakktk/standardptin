from django.db import models

class Standard(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อมาตรฐาน")
    description = models.TextField(blank=True, null=True, verbose_name="รายละเอียด")
    asset_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="หมายเลขทรัพย์สิน")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรองมาตรฐาน")
    due_date = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดมาตรฐาน")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไขล่าสุด")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "มาตรฐาน"
        verbose_name_plural = "มาตรฐาน" 