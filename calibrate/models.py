from django.db import models
from machine.models import Machine

class CalibrationForce(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอปรับเทียบ'),
        ('in_progress', 'กำลังปรับเทียบ'),
        ('passed', 'ผ่านการปรับเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    cal_force_id = models.AutoField(primary_key=True, verbose_name="รหัสการสอบเทียบแรง")
    apply_com = models.CharField(max_length=10, blank=True, null=True, verbose_name="แรงกด (Compression)")
    apply_ten = models.CharField(max_length=10, blank=True, null=True, verbose_name="แรงดึง (Tension)")
    compress = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่ากด (Compression)")
    tension = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าดึง (Tension)")
    fullscale = models.FloatField(blank=True, null=True, verbose_name="ค่าช่วงการวัดสูงสุด (Full Scale)")
    error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (Error)")
    uncer = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน (Uncertainty)")
    tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น")
    tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่ calibration")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะปรับเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบแรง"
        verbose_name_plural = "ข้อมูลสอบเทียบแรง"

class CalibrationPressure(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอปรับเทียบ'),
        ('in_progress', 'กำลังปรับเทียบ'),
        ('passed', 'ผ่านการปรับเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    cal_pressure_id = models.AutoField(primary_key=True, verbose_name="รหัสการสอบเทียบความดัน")
    set = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น")
    m1 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1")
    m2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2")
    m3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3")
    m4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4")
    avg = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย")
    error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (Error)")
    uncer = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน (Uncertainty)")
    tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น")
    tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่ calibration")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะปรับเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบความดัน"
        verbose_name_plural = "ข้อมูลสอบเทียบความดัน"
    
    def calculate_average(self):
        """คำนวณค่าเฉลี่ยจาก m1, m2, m3, m4"""
        values = []
        for field in ['m1', 'm2', 'm3', 'm4']:
            value = getattr(self, field)
            if value:
                # ถ้าเป็น string ให้แปลงเป็น float
                if isinstance(value, str):
                    if value.strip():
                        try:
                            values.append(float(value))
                        except (ValueError, TypeError):
                            continue
                # ถ้าเป็น float หรือ int อยู่แล้ว
                elif isinstance(value, (float, int)) and value != 0:
                    values.append(float(value))
        
        if values:
            return round(sum(values) / len(values), 2)
        return None
    
    def save(self, *args, **kwargs):
        """คำนวณค่าเฉลี่ยก่อนบันทึก"""
        self.avg = self.calculate_average()
        super().save(*args, **kwargs)

class CalibrationTorque(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอปรับเทียบ'),
        ('in_progress', 'กำลังปรับเทียบ'),
        ('passed', 'ผ่านการปรับเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    cal_torque_id = models.AutoField(primary_key=True, verbose_name="รหัสการสอบเทียบแรงบิด")
    cwset = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CW")
    cw0 = models.FloatField(blank=True, null=True, verbose_name="CW 0 องศา")
    cw90 = models.FloatField(blank=True, null=True, verbose_name="CW 90 องศา")
    cw180 = models.FloatField(blank=True, null=True, verbose_name="CW 180 องศา")
    cw270 = models.FloatField(blank=True, null=True, verbose_name="CW 270 องศา")
    cw_reading = models.FloatField(blank=True, null=True, verbose_name="ค่าอ่าน CW")
    cw_avg = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย CW")
    cw_error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CW")
    cw_uncen = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน CW")
    cw_tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CW")
    cw_tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CW")
    ccwset = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CCW")
    ccw0 = models.FloatField(blank=True, null=True, verbose_name="CCW 0 องศา")
    ccw90 = models.FloatField(blank=True, null=True, verbose_name="CCW 90 องศา")
    ccw180 = models.FloatField(blank=True, null=True, verbose_name="CCW 180 องศา")
    ccw270 = models.FloatField(blank=True, null=True, verbose_name="CCW 270 องศา")
    ccw_reading = models.FloatField(blank=True, null=True, verbose_name="ค่าอ่าน CCW")
    ccw_avg = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย CCW")
    ccw_error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CCW")
    ccw_uncen = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน CCW")
    ccw_tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CCW")
    ccw_tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CCW")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่ calibration")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_set', verbose_name="สถานะปรับเเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบแรงบิด"
        verbose_name_plural = "ข้อมูลสอบเทียบแรงบิด"
    
    def calculate_cw_average(self):
        """คำนวณค่าเฉลี่ย CW จาก cw0, cw90, cw180, cw270"""
        values = []
        for field in ['cw0', 'cw90', 'cw180', 'cw270']:
            value = getattr(self, field)
            if value is not None:
                values.append(value)
        
        if values:
            return round(sum(values) / len(values), 2)
        return None
    
    def calculate_ccw_average(self):
        """คำนวณค่าเฉลี่ย CCW จาก ccw0, ccw90, ccw180, ccw270"""
        values = []
        for field in ['ccw0', 'ccw90', 'ccw180', 'ccw270']:
            value = getattr(self, field)
            if value is not None:
                values.append(value)
        
        if values:
            return round(sum(values) / len(values), 2)
        return None
    
    def save(self, *args, **kwargs):
        """คำนวณค่าเฉลี่ยก่อนบันทึก"""
        self.cw_avg = self.calculate_cw_average()
        self.ccw_avg = self.calculate_ccw_average()
        super().save(*args, **kwargs)

class UUC(models.Model):
    name = models.CharField(max_length=100, verbose_name="ชื่อเครื่องที่สอบเทียบ (UUC)")
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ")
    std = models.ForeignKey('std.Standard', on_delete=models.CASCADE, verbose_name="มาตรฐาน")
    # เพิ่ม field อื่นๆ ตามต้องการ

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "เครื่องที่สอบเทียบ (UUC)"
        verbose_name_plural = "เครื่องที่สอบเทียบ (UUC)"

class UUCStdMap(models.Model):
    uuc = models.ForeignKey(UUC, on_delete=models.CASCADE, verbose_name="เครื่องที่สอบเทียบ (UUC)")
    std = models.ForeignKey('std.Standard', on_delete=models.CASCADE, verbose_name="มาตรฐาน")

    def __str__(self):
        return f"{self.uuc} - {self.std}"

    class Meta:
        verbose_name = "การเชื่อมโยง UUC กับมาตรฐาน"
        verbose_name_plural = "การเชื่อมโยง UUC กับมาตรฐาน"
