from django.db import models
from machine.models import Machine
from django.conf import settings

class CalibrationForce(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
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
    update = models.DateField(blank=True, null=True, verbose_name="วันที่สอบเทียบ")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='force_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='force_certificates')

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบแรง"
        verbose_name_plural = "ข้อมูลสอบเทียบแรง"

class CalibrationPressure(models.Model):
    STATUS_CHOICES = [
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
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
    update = models.DateField(blank=True, null=True, verbose_name="วันที่สอบเทียบ")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='pressure_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='pressure_certificates')

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
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
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
    update = models.DateField(blank=True, null=True, verbose_name="วันที่สอบเทียบ")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_set', verbose_name="สถานะปรับเเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='torque_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='torque_certificates')

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

class DialGaugeCalibration(models.Model):
    """ข้อมูลการสอบเทียบ Dial Gauge"""
    STATUS_CHOICES = [
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    # ข้อมูลพื้นฐาน
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ Dial Gauge")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='dial_gauge_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='dial_gauge_certificates')
    
    # ข้อมูลการสอบเทียบ
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    
    # ข้อมูลมาตรฐาน
    res_uuc = models.DecimalField(max_digits=10, decimal_places=6, verbose_name="ความละเอียด UUC (inch)")
    acc_std = models.DecimalField(max_digits=10, decimal_places=8, verbose_name="ความแม่นยำมาตรฐาน (inch)")
    
    # สถานะและความสำคัญ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    
    # ข้อมูลการคำนวณ
    type_a_sd = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Type A (SD)")
    type_b_res_uuc = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Type B Res.UUC")
    type_b_acc_std = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True, verbose_name="Type B Acc.STD")
    type_b_hysteresis = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Type B Hysteresis")
    uc_68 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Uc 68%")
    k_factor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="K")
    expanded_uncertainty_95 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="95%")
    
    def __str__(self):
        return f"Dial Gauge Calibration - {self.machine.name} ({self.date_calibration})"

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบ Dial Gauge"
        verbose_name_plural = "ข้อมูลสอบเทียบ Dial Gauge"

class DialGaugeReading(models.Model):
    """ข้อมูลการอ่านค่า Dial Gauge"""
    calibration = models.ForeignKey(DialGaugeCalibration, on_delete=models.CASCADE, related_name='readings', verbose_name="การสอบเทียบ")
    
    # ค่าที่ตั้งไว้
    uuc_set = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="UUC.Set (Inch)")
    
    # การอ่านค่ามาตรฐาน
    std_read_up1 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="STD.Read Up1 (Inch)")
    std_read_down1 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="STD.Read Down1 (Inch)")
    std_read_up2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="STD.Read Up2 (Inch)")
    std_read_down2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="STD.Read Down2 (Inch)")
    
    # ค่าเฉลี่ย
    average_up = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Average Up")
    average_down = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Average Down")
    
    # ค่าผิดพลาด
    error = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Error")
    
    # ความไม่แน่นอน
    uncertainty = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Uncer. ± (inch)")
    
    # ค่าฮิสเทอรีซิส
    hysteresis = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Hysteresis")
    
    # ค่าคำนวณอื่นๆ
    value_root2 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="ค่ารูท2")
    value_root3 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="ค่ารูท3")
    value_2root3 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="ค่า2รูท3")

    def __str__(self):
        return f"Reading {self.uuc_set} - {self.calibration}"

    class Meta:
        verbose_name = "ข้อมูลการอ่านค่า Dial Gauge"
        verbose_name_plural = "ข้อมูลการอ่านค่า Dial Gauge"

class BalanceCalibration(models.Model):
    """ข้อมูลการสอบเทียบ Balance"""
    STATUS_CHOICES = [
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    # ข้อมูลพื้นฐาน
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ Balance")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='balance_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='balance_certificates')
    
    # ข้อมูลการสอบเทียบ
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    
    # ข้อมูลมาตรฐาน
    unit = models.CharField(max_length=20, default="mg", verbose_name="หน่วย")
    
    # สถานะและความสำคัญ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    
    # ข้อมูลการคำนวณ
    drift = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Drift")
    res_push = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="RES.ดัน")
    res_tip = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="RES.ปลาย")
    air_buoyancy = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Air Biyou")
    uncertainty_68 = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Uncer 68%")
    uncertainty_95_k = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="95%*K")
    final_uncertainty = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Final Uncer")
    
    def __str__(self):
        return f"Balance Calibration - {self.machine.name} ({self.date_calibration})"

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบ Balance"
        verbose_name_plural = "ข้อมูลสอบเทียบ Balance"

class BalanceReading(models.Model):
    """ข้อมูลการอ่านค่า Balance"""
    calibration = models.ForeignKey(BalanceCalibration, on_delete=models.CASCADE, related_name='readings', verbose_name="การสอบเทียบ")
    
    # ค่าที่ตั้งไว้
    uuc_set = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="UUC.set")
    
    # การอ่านค่ามาตรฐาน (10 ครั้ง)
    std_read_1 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 1")
    std_read_2 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 2")
    std_read_3 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 3")
    std_read_4 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 4")
    std_read_5 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 5")
    std_read_6 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 6")
    std_read_7 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 7")
    std_read_8 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 8")
    std_read_9 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 9")
    std_read_10 = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="STD.Read 10")
    
    # ค่าคำนวณ
    average = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="Avg")
    standard_deviation = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="SD")
    uncertainty = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Uncer")

    def __str__(self):
        return f"Balance Reading {self.uuc_set} - {self.calibration}"

    class Meta:
        verbose_name = "ข้อมูลการอ่านค่า Balance"
        verbose_name_plural = "ข้อมูลการอ่านค่า Balance"

class MicrowaveCalibration(models.Model):
    """ข้อมูลการสอบเทียบ Microwave"""
    STATUS_CHOICES = [
        ('pending', 'รอสอบเทียบ'),
        ('in_progress', 'กำลังสอบเทียบ'),
        ('passed', 'ผ่านการสอบเทียบ'),
        ('cert_issued', 'ออกใบรับรอง'),
        ('failed', 'ไม่ผ่านการสอบเทียบ'),
        ('closed', 'ปิดงาน'),
    ]
    
    PRIORITY_CHOICES = [
        ('normal', 'ปกติ'),
        ('urgent', 'ด่วน'),
        ('very_urgent', 'ด่วนมาก'),
    ]
    
    # ข้อมูลพื้นฐาน
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ Microwave")
    std_id = models.ForeignKey('std.Standard', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='microwave_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='microwave_certificates')
    
    # ข้อมูลการสอบเทียบ
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
    
    # สถานะและความสำคัญ
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    
    def __str__(self):
        return f"Microwave Calibration - {self.machine.name} ({self.date_calibration})"

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบ Microwave"
        verbose_name_plural = "ข้อมูลสอบเทียบ Microwave"

class MicrowaveReading(models.Model):
    """ข้อมูลการอ่านค่า Microwave"""
    TEST_TYPE_CHOICES = [
        ('output_level_ant', 'OUTPUT LEVEL @ ANT PORT CALIBRATION'),
        ('output_level_rf', 'OUTPUT LEVEL @ RF I/O PORT CALIBRATION'),
        ('dme_reply_pulse', 'DME REPLY PULSE CHARACTERISTICS CALIBRATION'),
        ('dme_reply_delay', 'DME REPLY DELAY RANGE CALIBRATION'),
        ('dme_reply_position', 'DME REPLY POSITION AND AMPLITUDE CALIBRATION'),
        ('dme_reply_efficiency', 'DME REPLY REPLY EFFICIENCY CALIBRATION'),
        ('dme_squitter', 'DME SQUITTER CALIBRATION'),
        ('dme_interrogation_timing', 'DME MEASUREMENT - INTERROGATION PULSE TIMING CALIBRATION'),
        ('dme_interrogation_prf', 'DME MEASUREMENT-INTERROGATION PRF CALIBRATION'),
        ('dme_interrogation_freq', 'DME MEASUREMENT-INTERROGATION FREQUENCY CALIBRATION'),
        ('xpdr_pulse_atcrbs', 'XPDR PULSE CHARACTERISTICS-ATCRBS CALIBRATION'),
        ('xpdr_pulse_mode_s', 'XPDR PULSE CHARACTERISTICS-MODE S CALIBRATION'),
        ('xpdr_interrogation_prf', 'XPDR INTERROGATION PRF CALIBRATION'),
        ('xpdr_sls_level', 'XPDR SLS LEVEL CALIBRATION'),
    ]
    
    calibration = models.ForeignKey(MicrowaveCalibration, on_delete=models.CASCADE, related_name='readings', verbose_name="การสอบเทียบ")
    
    # ประเภทการทดสอบ
    test_type = models.CharField(max_length=50, choices=TEST_TYPE_CHOICES, verbose_name="ประเภทการทดสอบ")
    
    # ข้อมูลการทดสอบ
    function_test = models.CharField(max_length=200, blank=True, null=True, verbose_name="Function Test")
    nominal_value = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nominal Value")
    rf_level = models.CharField(max_length=100, blank=True, null=True, verbose_name="RF Level")
    frequency = models.CharField(max_length=100, blank=True, null=True, verbose_name="Frequency")
    
    # ค่าที่วัดได้
    measured_value = models.CharField(max_length=100, blank=True, null=True, verbose_name="Measured Value")
    measured_value_numeric = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True, verbose_name="Measured Value (Numeric)")
    
    # หน่วย
    unit = models.CharField(max_length=20, blank=True, null=True, verbose_name="Unit")
    
    # ความไม่แน่นอน
    uncertainty = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="Uncertainty (±)")
    
    # ขีดจำกัดความคลาดเคลื่อน
    tolerance_limit_min = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True, verbose_name="Tolerance Limit Min")
    tolerance_limit_max = models.DecimalField(max_digits=15, decimal_places=6, blank=True, null=True, verbose_name="Tolerance Limit Max")
    
    # ผลการทดสอบ
    test_result = models.CharField(max_length=20, choices=[('pass', 'ผ่าน'), ('fail', 'ไม่ผ่าน')], blank=True, null=True, verbose_name="ผลการทดสอบ")
    
    # หมายเหตุ
    notes = models.TextField(blank=True, null=True, verbose_name="หมายเหตุ")

    def __str__(self):
        return f"Microwave Reading - {self.get_test_type_display()} ({self.calibration})"

    class Meta:
        verbose_name = "ข้อมูลการอ่านค่า Microwave"
        verbose_name_plural = "ข้อมูลการอ่านค่า Microwave"
