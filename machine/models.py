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
    name = models.CharField(max_length=200, verbose_name="ชื่อเครื่องมือวัดใช้ปรับเทียบ")
    model = models.CharField(max_length=100, blank=True, null=True, verbose_name="รุ่น")
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขเครื่อง")
    certificate = models.ForeignKey('cert.Certificate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ใบรับรอง")
    machine_type = models.ForeignKey(MachineType, on_delete=models.CASCADE, verbose_name="ประเภท")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")

    def __str__(self):
        return f"{self.name} - {self.model}"

    class Meta:
        verbose_name = "เครื่องมือที่ใช้สอบเทียบ"
        verbose_name_plural = "เครื่องมือที่ใช้สอบเทียบ"

class Machine(models.Model):
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
    deleted = models.BooleanField(default=False, verbose_name="ลบแล้ว")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "เครื่องมือ"
        verbose_name_plural = "เครื่องมือ"
