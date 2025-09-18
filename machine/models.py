from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MachineType(models.Model):
    name = models.CharField(max_length=100, verbose_name="ประเภทเครื่องมือ")
    # เพิ่ม field อื่นๆ ตามต้องการ

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ประเภทเครื่องมือ"
        verbose_name_plural = "ประเภทเครื่องมือ"

class MachineUnit(models.Model):
    name = models.CharField(max_length=100, verbose_name="หน่วยนับ")
    # เพิ่ม field อื่นๆ ตามต้องการ

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "หน่วยนับ"
        verbose_name_plural = "หน่วยนับ"

class Manufacture(models.Model):
    name = models.CharField(max_length=100, verbose_name="ผู้ผลิต")
    # เพิ่ม field อื่นๆ ตามต้องการ

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ผู้ผลิต"
        verbose_name_plural = "ผู้ผลิต"

class CalibrationEquipment(models.Model):
    """เครื่องมือที่ใช้สอบเทียบ"""
    name = models.CharField(max_length=200, verbose_name="ชื่อเครื่องมือวัดใช้สอบเทียบ")
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name="รุ่น")
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขเครื่อง")
    certificate = models.CharField(max_length=200, blank=True, null=True, verbose_name="ใบรับรอง")
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE, verbose_name="ประเภท")
    created_at = models.DateTimeField(blank=True, null=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")

    def __str__(self):
        return f"{self.name} - {self.model}"

    def save(self, *args, **kwargs):
        from django.utils import timezone
        from datetime import datetime
        
        # ถ้าไม่มีการกำหนด created_at ให้ใช้เวลาปัจจุบัน
        if not self.created_at:
            self.created_at = timezone.now()
        
        # ตรวจสอบว่า created_at ไม่ใช่วันอนาคต
        if self.created_at and self.created_at > timezone.now():
            raise ValueError("วันที่สร้างไม่สามารถเป็นวันอนาคตได้")
        
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "เครื่องมือที่ใช้สอบเทียบ"
        verbose_name_plural = "เครื่องมือที่ใช้สอบเทียบ"

class Machine(models.Model):
    STATUS_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    organize = models.ForeignKey('organize.Organize', on_delete=models.CASCADE, verbose_name="หน่วยงาน", null=True, blank=True)
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE, verbose_name="ประเภทเครื่องมือ")
    name = models.CharField(max_length=45, verbose_name="ชื่อเครื่องมือ")
    model = models.CharField(max_length=45, blank=True, null=True, verbose_name="รุ่น")
    serial_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="หมายเลขเครื่อง")
    range = models.CharField(max_length=10, blank=True, null=True, verbose_name="ช่วงการวัด")
    res_uuc = models.CharField(max_length=5, blank=True, null=True, verbose_name="ความละเอียด UUC")
    update = models.DateTimeField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    unit = models.ForeignKey(MachineUnit, on_delete=models.CASCADE, verbose_name="หน่วยนับ")
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, verbose_name="ผู้ผลิต")
    calibration_equipment = models.ForeignKey(CalibrationEquipment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='normal', verbose_name="สถานะ")
    deleted = models.BooleanField(default=False, verbose_name="ลบแล้ว")
    option = models.CharField(max_length=100, blank=True, null=True, verbose_name="ตัวเลือกเพิ่มเติม")
    customer_asset_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="รหัสลูกค้า/ทรัพย์สิน")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "เครื่องมือ"
        verbose_name_plural = "เครื่องมือ"
