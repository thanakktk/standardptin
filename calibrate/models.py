from django.db import models
from machine.models import Machine, CalibrationEquipment
from django.conf import settings


class CalibrationEquipmentUsed(models.Model):
    """เครื่องมือที่ใช้ในการสอบเทียบ (Many-to-Many relationship)"""
    calibration_type = models.CharField(max_length=50, verbose_name="ประเภทการสอบเทียบ")
    calibration_id = models.PositiveIntegerField(verbose_name="รหัสการสอบเทียบ")
    equipment = models.ForeignKey(CalibrationEquipment, on_delete=models.CASCADE, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    
    class Meta:
        verbose_name = "เครื่องมือที่ใช้ในการสอบเทียบ"
        verbose_name_plural = "เครื่องมือที่ใช้ในการสอบเทียบ"
        unique_together = ['calibration_type', 'calibration_id', 'equipment']
    
    def __str__(self):
        return f"{self.calibration_type} - {self.equipment.name}"


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
    
    cal_pressure_id = models.AutoField(primary_key=True, verbose_name="รหัสการสอบเทียบ Pressure")
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    set = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น")
    m1 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1")
    m2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2")
    m3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3")
    m4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4")
    avg = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย")
    actual = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง")
    error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (Error)")
    
    # แถวเพิ่มเติม
    set_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น (แถว 2)")
    m1_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1 (แถว 2)")
    m2_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2 (แถว 2)")
    m3_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3 (แถว 2)")
    m4_2 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4 (แถว 2)")
    avg_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย (แถว 2)")
    actual_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง (แถว 2)")
    error_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (แถว 2)")
    
    set_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น (แถว 3)")
    m1_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1 (แถว 3)")
    m2_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2 (แถว 3)")
    m3_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3 (แถว 3)")
    m4_3 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4 (แถว 3)")
    avg_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย (แถว 3)")
    actual_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง (แถว 3)")
    error_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (แถว 3)")
    
    set_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น (แถว 4)")
    m1_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1 (แถว 4)")
    m2_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2 (แถว 4)")
    m3_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3 (แถว 4)")
    m4_4 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4 (แถว 4)")
    avg_4 = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย (แถว 4)")
    actual_4 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง (แถว 4)")
    error_4 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (แถว 4)")
    
    set_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น (แถว 5)")
    m1_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1 (แถว 5)")
    m2_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2 (แถว 5)")
    m3_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3 (แถว 5)")
    m4_5 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4 (แถว 5)")
    avg_5 = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย (แถว 5)")
    actual_5 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง (แถว 5)")
    error_5 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (แถว 5)")
    
    set_6 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าตั้งต้น (แถว 6)")
    m1_6 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 1 (แถว 6)")
    m2_6 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 2 (แถว 6)")
    m3_6 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 3 (แถว 6)")
    m4_6 = models.CharField(max_length=10, blank=True, null=True, verbose_name="ค่าที่ 4 (แถว 6)")
    avg_6 = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย (แถว 6)")
    actual_6 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง (แถว 6)")
    error_6 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน (แถว 6)")
    uncer = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน (Uncertainty)")
    tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น")
    tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด")
    tolerance_start_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น (แถว 2)")
    tolerance_end_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด (แถว 2)")
    tolerance_start_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น (แถว 3)")
    tolerance_end_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด (แถว 3)")
    tolerance_start_4 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น (แถว 4)")
    tolerance_end_4 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด (แถว 4)")
    tolerance_start_5 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น (แถว 5)")
    tolerance_end_5 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด (แถว 5)")
    tolerance_start_6 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น (แถว 6)")
    tolerance_end_6 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด (แถว 6)")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่สอบเทียบ")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='pressure_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='pressure_certificates')
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบ Pressure"
        verbose_name_plural = "ข้อมูลสอบเทียบ Pressure"
    
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
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='pressure',
            calibration_id=self.cal_pressure_id
        )
    
    def check_tolerance_limits(self):
        """ตรวจสอบเงื่อนไขการคำนวณตาม Tolerance Limit
        
        เงื่อนไข: ค่าของช่อง UUC Set และ ค่าของช่อง Actual 
        ต้องอยู่ในระหว่าง ค่าของช่อง Tolerance Limit ทั้งคู่ ถึงจะผ่านการสอบเทียบ
        หากค่าของ UUC Set และ ค่าของช่อง Actual ต่ำกว่า หรือ มากกว่า 
        ค่าของช่อง Tolerance Limit ให้ ไม่ผ่านการสอบเทียบ
        """
        results = []
        
        # ตรวจสอบแถวที่ 1
        if self.set and self.actual and self.tolerance_start and self.tolerance_end:
            try:
                set_val = float(self.set)
                actual_val = float(self.actual)
                tolerance_start = float(self.tolerance_start)
                tolerance_end = float(self.tolerance_end)
                
                # ตรวจสอบ UUC Set อยู่ในช่วง Tolerance Limit
                set_in_range = tolerance_start <= set_val <= tolerance_end
                # ตรวจสอบ Actual อยู่ในช่วง Tolerance Limit  
                actual_in_range = tolerance_start <= actual_val <= tolerance_end
                
                # ผ่านการสอบเทียบเมื่อทั้ง UUC Set และ Actual อยู่ในช่วง Tolerance Limit
                passed = set_in_range and actual_in_range
                
                results.append({
                    'row': 1,
                    'set': set_val,
                    'actual': actual_val,
                    'tolerance_start': tolerance_start,
                    'tolerance_end': tolerance_end,
                    'set_in_range': set_in_range,
                    'actual_in_range': actual_in_range,
                    'passed': passed
                })
            except (ValueError, TypeError):
                results.append({
                    'row': 1,
                    'error': 'Invalid data format'
                })
        
        # ตรวจสอบแถวที่ 2-6
        for i in range(2, 7):
            set_field = getattr(self, f'set_{i}', None)
            actual_field = getattr(self, f'actual_{i}', None)
            tolerance_start_field = getattr(self, f'tolerance_start_{i}', None)
            tolerance_end_field = getattr(self, f'tolerance_end_{i}', None)
            
            if set_field and actual_field and tolerance_start_field and tolerance_end_field:
                try:
                    set_val = float(set_field)
                    actual_val = float(actual_field)
                    tolerance_start = float(tolerance_start_field)
                    tolerance_end = float(tolerance_end_field)
                    
                    # ตรวจสอบ UUC Set อยู่ในช่วง Tolerance Limit
                    set_in_range = tolerance_start <= set_val <= tolerance_end
                    # ตรวจสอบ Actual อยู่ในช่วง Tolerance Limit
                    actual_in_range = tolerance_start <= actual_val <= tolerance_end
                    
                    # ผ่านการสอบเทียบเมื่อทั้ง UUC Set และ Actual อยู่ในช่วง Tolerance Limit
                    passed = set_in_range and actual_in_range
                    
                    results.append({
                        'row': i,
                        'set': set_val,
                        'actual': actual_val,
                        'tolerance_start': tolerance_start,
                        'tolerance_end': tolerance_end,
                        'set_in_range': set_in_range,
                        'actual_in_range': actual_in_range,
                        'passed': passed
                    })
                except (ValueError, TypeError):
                    results.append({
                        'row': i,
                        'error': 'Invalid data format'
                    })
        
        return results
    
    def get_calibration_result(self):
        """คำนวณผลการสอบเทียบโดยรวม"""
        results = self.check_tolerance_limits()
        
        if not results:
            return 'no_data'
        
        # ตรวจสอบว่ามี error หรือไม่
        if any('error' in result for result in results):
            return 'error'
        
        # ตรวจสอบว่าทุกแถวผ่านหรือไม่
        all_passed = all(result.get('passed', False) for result in results)
        
        if all_passed:
            return 'passed'
        else:
            return 'failed'
    
    def auto_update_status(self):
        """อัพเดต status อัตโนมัติตามผลการสอบเทียบ"""
        result = self.get_calibration_result()
        
        if result == 'passed':
            self.status = 'passed'
        elif result == 'failed':
            self.status = 'failed'
        elif result == 'error':
            self.status = 'in_progress'  # ยังไม่สามารถประเมินได้
        
        return result

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
    
    cal_torque_id = models.AutoField(primary_key=True, verbose_name="รหัสการสอบเทียบ Torque")
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    cwset = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CW")
    cw0 = models.FloatField(blank=True, null=True, verbose_name="CW 0 องศา")
    cw90 = models.FloatField(blank=True, null=True, verbose_name="CW 90 องศา")
    cw180 = models.FloatField(blank=True, null=True, verbose_name="CW 180 องศา")
    cw270 = models.FloatField(blank=True, null=True, verbose_name="CW 270 องศา")
    cw_reading = models.FloatField(blank=True, null=True, verbose_name="ค่าอ่าน CW")
    cw_avg = models.FloatField(blank=True, null=True, verbose_name="ค่าเฉลี่ย CW")
    cw_actual = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CW")
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
    ccw_actual = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CCW")
    ccw_error = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CCW")
    ccw_uncen = models.FloatField(blank=True, null=True, verbose_name="ค่าความไม่แน่นอน CCW")
    ccw_tolerance_start = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CCW")
    ccw_tolerance_end = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CCW")
    
    # ฟิลด์สำหรับแถวที่ 2
    cwset_2 = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CW 2")
    cw_actual_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CW 2")
    cw_error_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CW 2")
    cw_tolerance_start_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CW 2")
    cw_tolerance_end_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CW 2")
    ccwset_2 = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CCW 2")
    ccw_actual_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CCW 2")
    ccw_error_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CCW 2")
    ccw_tolerance_start_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CCW 2")
    ccw_tolerance_end_2 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CCW 2")
    
    # ฟิลด์สำหรับแถวที่ 3
    cwset_3 = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CW 3")
    cw_actual_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CW 3")
    cw_error_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CW 3")
    cw_tolerance_start_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CW 3")
    cw_tolerance_end_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CW 3")
    ccwset_3 = models.FloatField(blank=True, null=True, verbose_name="ตั้งค่า CCW 3")
    ccw_actual_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าจริง CCW 3")
    ccw_error_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อน CCW 3")
    ccw_tolerance_start_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนเริ่มต้น CCW 3")
    ccw_tolerance_end_3 = models.FloatField(blank=True, null=True, verbose_name="ค่าความคลาดเคลื่อนสิ้นสุด CCW 3")
    
    update = models.DateField(blank=True, null=True, verbose_name="วันที่สอบเทียบ")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะปรับเเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    uuc_id = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name="เครื่องมือที่สอบเทียบ")
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='torque_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='torque_certificates')
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")

    class Meta:
        verbose_name = "ข้อมูลสอบเทียบ Torque"
        verbose_name_plural = "ข้อมูลสอบเทียบ Torque"
    
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
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='torque',
            calibration_id=self.cal_torque_id
        )
    
    def check_tolerance_limits(self):
        """ตรวจสอบเงื่อนไขการคำนวณตาม Tolerance Limit"""
        results = []
        
        # ตรวจสอบแถวที่ 1 (CW)
        if self.cwset and self.cw_avg and self.cw_tolerance_start and self.cw_tolerance_end:
            try:
                set_val = float(self.cwset)
                actual_val = float(self.cw_avg)
                tolerance_start = float(self.cw_tolerance_start)
                tolerance_end = float(self.cw_tolerance_end)
                
                # ตรวจสอบ UUC Set
                set_in_range = tolerance_start <= set_val <= tolerance_end
                # ตรวจสอบ Actual
                actual_in_range = tolerance_start <= actual_val <= tolerance_end
                
                results.append({
                    'row': 1,
                    'direction': 'CW',
                    'set': set_val,
                    'actual': actual_val,
                    'tolerance_start': tolerance_start,
                    'tolerance_end': tolerance_end,
                    'set_in_range': set_in_range,
                    'actual_in_range': actual_in_range,
                    'passed': set_in_range and actual_in_range
                })
            except (ValueError, TypeError):
                results.append({
                    'row': 1,
                    'direction': 'CW',
                    'error': 'Invalid data format'
                })
        
        # ตรวจสอบแถวที่ 1 (CCW)
        if self.ccwset and self.ccw_avg and self.ccw_tolerance_start and self.ccw_tolerance_end:
            try:
                set_val = float(self.ccwset)
                actual_val = float(self.ccw_avg)
                tolerance_start = float(self.ccw_tolerance_start)
                tolerance_end = float(self.ccw_tolerance_end)
                
                # ตรวจสอบ UUC Set
                set_in_range = tolerance_start <= set_val <= tolerance_end
                # ตรวจสอบ Actual
                actual_in_range = tolerance_start <= actual_val <= tolerance_end
                
                results.append({
                    'row': 1,
                    'direction': 'CCW',
                    'set': set_val,
                    'actual': actual_val,
                    'tolerance_start': tolerance_start,
                    'tolerance_end': tolerance_end,
                    'set_in_range': set_in_range,
                    'actual_in_range': actual_in_range,
                    'passed': set_in_range and actual_in_range
                })
            except (ValueError, TypeError):
                results.append({
                    'row': 1,
                    'direction': 'CCW',
                    'error': 'Invalid data format'
                })
        
        return results
    
    def get_calibration_result(self):
        """คำนวณผลการสอบเทียบโดยรวม"""
        results = self.check_tolerance_limits()
        
        if not results:
            return 'no_data'
        
        # ตรวจสอบว่ามี error หรือไม่
        if any('error' in result for result in results):
            return 'error'
        
        # ตรวจสอบว่าทุกแถวผ่านหรือไม่
        all_passed = all(result.get('passed', False) for result in results)
        
        if all_passed:
            return 'passed'
        else:
            return 'failed'
    
    def auto_update_status(self):
        """อัพเดต status อัตโนมัติตามผลการสอบเทียบ"""
        result = self.get_calibration_result()
        
        if result == 'passed':
            self.status = 'passed'
        elif result == 'failed':
            self.status = 'failed'
        elif result == 'error':
            self.status = 'in_progress'  # ยังไม่สามารถประเมินได้
        
        return result

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
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='dial_gauge_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='dial_gauge_certificates')
    
    # ข้อมูลการสอบเทียบ
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
    
    # ข้อมูลมาตรฐาน
    res_uuc = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, verbose_name="ความละเอียด UUC (inch)")
    acc_std = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True, verbose_name="ความแม่นยำมาตรฐาน (inch)")
    
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
    
    # Dial Gauge Calibration fields - Row 1
    uuc_set = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC.Set( inch )")
    actual = models.CharField(max_length=50, blank=True, null=True, verbose_name="Actual( inch )")
    error = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error( inch )")
    uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g)")
    tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit")
    
    # Dial Gauge Calibration fields - Row 2
    set_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC.Set( inch ) - Row 2")
    actual_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Actual( inch ) - Row 2")
    error_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error( inch ) - Row 2")
    tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit - Row 2")
    
    # Dial Gauge Calibration fields - Row 3
    set_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC.Set( inch ) - Row 3")
    actual_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Actual( inch ) - Row 3")
    error_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error( inch ) - Row 3")
    tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit - Row 3")
    
    # Dial Gauge Calibration fields - Row 4
    set_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC.Set( inch ) - Row 4")
    actual_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Actual( inch ) - Row 4")
    error_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error( inch ) - Row 4")
    tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit - Row 4")
    
    # Dial Gauge Calibration fields - Row 5
    set_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC.Set( inch ) - Row 5")
    actual_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Actual( inch ) - Row 5")
    error_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error( inch ) - Row 5")
    tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit - Row 5")
    
    def __str__(self):
        return f"Dial Gauge Calibration - {self.machine.name} ({self.date_calibration})"
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='dial_gauge',
            calibration_id=self.pk
        )

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
    uuc_id = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่สอบเทียบ", related_name='balance_uuc_calibrations')
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='balance_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='balance_certificates')
    
    # ข้อมูลการสอบเทียบ
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    received_date = models.DateField(blank=True, null=True, verbose_name="วันที่รับเครื่องมือ")
    issue_date = models.DateField(blank=True, null=True, verbose_name="วันที่ออกใบรับรอง")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
    procedure_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขขั้นตอนการสอบเทียบ")
    
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
    
    # Linear (Min-Max) fields - Row 1
    linear_nominal_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nominal Value (g)")
    linear_conventional_mass = models.CharField(max_length=50, blank=True, null=True, verbose_name="Conventional Mass (g)")
    linear_displayed_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Displayed Value (g)")
    linear_error = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error (g)")
    linear_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g)")
    
    # Linear (Min-Max) fields - Row 2
    linear_nominal_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nominal Value (g) - Row 2")
    linear_conventional_mass_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Conventional Mass (g) - Row 2")
    linear_displayed_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Displayed Value (g) - Row 2")
    linear_error_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error (g) - Row 2")
    linear_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g) - Row 2")
    
    # Linear (Min-Max) fields - Row 3
    linear_nominal_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nominal Value (g) - Row 3")
    linear_conventional_mass_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Conventional Mass (g) - Row 3")
    linear_displayed_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Displayed Value (g) - Row 3")
    linear_error_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error (g) - Row 3")
    linear_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g) - Row 3")
    
    # Linear (Min-Max) fields - Row 4
    linear_nominal_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nominal Value (g) - Row 4")
    linear_conventional_mass_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Conventional Mass (g) - Row 4")
    linear_displayed_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Displayed Value (g) - Row 4")
    linear_error_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error (g) - Row 4")
    linear_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g) - Row 4")
    
    # Linear (Min-Max) fields - Row 5
    linear_nominal_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Nominal Value (g) - Row 5")
    linear_conventional_mass_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Conventional Mass (g) - Row 5")
    linear_displayed_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Displayed Value (g) - Row 5")
    linear_error_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Error (g) - Row 5")
    linear_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (g) - Row 5")
    
    def __str__(self):
        return f"Balance Calibration - {self.machine.name} ({self.date_calibration})"
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='balance',
            calibration_id=self.pk
        )
    
    def check_tolerance_limits(self):
        """ตรวจสอบเงื่อนไขการคำนวณตาม Tolerance Limit
        
        เงื่อนไข:
        1. ค่าของช่อง Displayed Value ต้องไม่เกินค่าของช่อง Conventional Mass ± 0.10
        2. ค่า Error ต้องอยู่ในช่วง ± 0.10
        """
        results = []
        tolerance = 0.10  # ค่าความคลาดเคลื่อนที่อนุญาต ± 0.10
        
        # ตรวจสอบแถวที่ 1
        if (self.linear_conventional_mass and 
            self.linear_displayed_value and self.linear_error):
            try:
                conventional_mass = float(self.linear_conventional_mass)
                displayed_value = float(self.linear_displayed_value)
                error = float(self.linear_error)
                
                # ตรวจสอบ Displayed Value กับ Conventional Mass ± 0.10
                conventional_min = conventional_mass - tolerance
                conventional_max = conventional_mass + tolerance
                displayed_in_range = conventional_min <= displayed_value <= conventional_max
                
                # ตรวจสอบ Error อยู่ในช่วง ± 0.10
                error_in_range = -tolerance <= error <= tolerance
                
                # ผ่านการสอบเทียบเมื่อทั้งสองเงื่อนไขเป็นจริง
                passed = displayed_in_range and error_in_range
                
                results.append({
                    'row': 1,
                    'conventional_mass': conventional_mass,
                    'displayed_value': displayed_value,
                    'error': error,
                    'tolerance': tolerance,
                    'conventional_min': conventional_min,
                    'conventional_max': conventional_max,
                    'displayed_in_range': displayed_in_range,
                    'error_in_range': error_in_range,
                    'passed': passed
                })
            except (ValueError, TypeError):
                results.append({
                    'row': 1,
                    'error': 'Invalid data format'
                })
        
        # ตรวจสอบแถวที่ 2-5
        for i in range(2, 6):
            conventional_field = getattr(self, f'linear_conventional_mass_{i}', None)
            displayed_field = getattr(self, f'linear_displayed_value_{i}', None)
            error_field = getattr(self, f'linear_error_{i}', None)
            
            if (conventional_field and displayed_field and error_field):
                try:
                    conventional_mass = float(conventional_field)
                    displayed_value = float(displayed_field)
                    error = float(error_field)
                    
                    # ตรวจสอบ Displayed Value กับ Conventional Mass ± 0.10
                    conventional_min = conventional_mass - tolerance
                    conventional_max = conventional_mass + tolerance
                    displayed_in_range = conventional_min <= displayed_value <= conventional_max
                    
                    # ตรวจสอบ Error อยู่ในช่วง ± 0.10
                    error_in_range = -tolerance <= error <= tolerance
                    
                    # ผ่านการสอบเทียบเมื่อทั้งสองเงื่อนไขเป็นจริง
                    passed = displayed_in_range and error_in_range
                    
                    results.append({
                        'row': i,
                        'conventional_mass': conventional_mass,
                        'displayed_value': displayed_value,
                        'error': error,
                        'tolerance': tolerance,
                        'conventional_min': conventional_min,
                        'conventional_max': conventional_max,
                        'displayed_in_range': displayed_in_range,
                        'error_in_range': error_in_range,
                        'passed': passed
                    })
                except (ValueError, TypeError):
                    results.append({
                        'row': i,
                        'error': 'Invalid data format'
                    })
        
        return results
    
    def get_calibration_result(self):
        """คำนวณผลการสอบเทียบโดยรวม"""
        results = self.check_tolerance_limits()
        
        if not results:
            return 'no_data'
        
        # ตรวจสอบว่ามี error หรือไม่
        if any('error' in result for result in results):
            return 'error'
        
        # ตรวจสอบว่าทุกแถวผ่านหรือไม่
        all_passed = all(result.get('passed', False) for result in results)
        
        if all_passed:
            return 'passed'
        else:
            return 'failed'
    
    def auto_update_status(self):
        """อัพเดต status อัตโนมัติตามผลการสอบเทียบ"""
        result = self.get_calibration_result()
        
        if result == 'passed':
            self.status = 'passed'
        elif result == 'failed':
            self.status = 'failed'
        elif result == 'error':
            self.status = 'in_progress'  # ยังไม่สามารถประเมินได้
        
        return result

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
    
    # ข้อมูลเพิ่มเติมสำหรับใบรับรอง
    conventional_mass = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="Conventional Mass")
    displayed_value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True, verbose_name="Displayed Value")

    def __str__(self):
        return f"Balance Reading {self.uuc_set} - {self.calibration}"

    class Meta:
        verbose_name = "ข้อมูลการอ่านค่า Balance"
        verbose_name_plural = "ข้อมูลการอ่านค่า Balance"

class HighFrequencyCalibration(models.Model):
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
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ High Frequency")
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='high_frequency_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='high_frequency_certificates')
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateTimeField(auto_now=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะการสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    
    # 1. Frequency Accuracy and Display Calibration
    freq_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Time Base)")
    freq_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting")
    freq_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value")
    freq_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±)")
    freq_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit")
    
    # แถวเพิ่มเติมสำหรับ Frequency
    freq_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Time Base) 2")
    freq_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 2")
    freq_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 2")
    freq_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 2")
    freq_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 2")
    
    freq_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Time Base) 3")
    freq_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 3")
    freq_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 3")
    freq_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 3")
    freq_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 3")
    
    freq_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Time Base) 4")
    freq_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 4")
    freq_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 4")
    freq_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 4")
    freq_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 4")
    
    freq_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Time Base) 5")
    freq_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 5")
    freq_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 5")
    freq_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 5")
    freq_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 5")
    
    # 2. Digital Voltmeter Calibration
    volt_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Voltage)")
    volt_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting")
    volt_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value")
    volt_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±)")
    volt_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit")
    
    # แถวเพิ่มเติมสำหรับ Voltage
    volt_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Voltage) 2")
    volt_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 2")
    volt_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 2")
    volt_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 2")
    volt_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 2")
    
    volt_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Voltage) 3")
    volt_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 3")
    volt_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 3")
    volt_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 3")
    volt_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 3")
    
    volt_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Voltage) 4")
    volt_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 4")
    volt_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 4")
    volt_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 4")
    volt_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 4")
    
    volt_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Voltage) 5")
    volt_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting 5")
    volt_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value 5")
    volt_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) 5")
    volt_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit 5")
    
    def __str__(self):
        return f"High Frequency Calibration - {self.machine.name}"
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='high_frequency',
            calibration_id=self.pk
        )
    
    def check_tolerance_limits(self):
        """ตรวจสอบเงื่อนไขการคำนวณตาม Tolerance Limit"""
        results = []
        
        # ตรวจสอบ Frequency Accuracy (แถวที่ 1-5)
        for i in range(1, 6):
            setting_field = getattr(self, f'freq_uuc_setting_{i}' if i > 1 else 'freq_uuc_setting', None)
            measured_field = getattr(self, f'freq_measured_value_{i}' if i > 1 else 'freq_measured_value', None)
            tolerance_field = getattr(self, f'freq_tolerance_limit_{i}' if i > 1 else 'freq_tolerance_limit', None)
            
            if setting_field and measured_field and tolerance_field:
                try:
                    setting_val = float(setting_field)
                    measured_val = float(measured_field)
                    
                    # แปลง Tolerance Limit (รูปแบบ: "min - max" หรือ "min to max")
                    tolerance_str = str(tolerance_field).strip()
                    if ' - ' in tolerance_str:
                        min_tolerance, max_tolerance = tolerance_str.split(' - ')
                    elif ' – ' in tolerance_str:  # รองรับ en dash
                        min_tolerance, max_tolerance = tolerance_str.split(' – ')
                    elif ' to ' in tolerance_str:
                        min_tolerance, max_tolerance = tolerance_str.split(' to ')
                    else:
                        # ถ้าเป็นตัวเลขเดียว ให้ใช้เป็น ±tolerance
                        try:
                            center = float(tolerance_str)
                            min_tolerance = center - abs(center * 0.01)  # ±1%
                            max_tolerance = center + abs(center * 0.01)
                        except:
                            continue
                    
                    min_tolerance = float(min_tolerance.strip())
                    max_tolerance = float(max_tolerance.strip())
                    
                    # ตรวจสอบ UUC Setting
                    setting_in_range = min_tolerance <= setting_val <= max_tolerance
                    # ตรวจสอบ Measured Value
                    measured_in_range = min_tolerance <= measured_val <= max_tolerance
                    
                    results.append({
                        'row': i,
                        'type': 'Frequency',
                        'setting': setting_val,
                        'measured': measured_val,
                        'tolerance_min': min_tolerance,
                        'tolerance_max': max_tolerance,
                        'setting_in_range': setting_in_range,
                        'measured_in_range': measured_in_range,
                        'passed': setting_in_range and measured_in_range
                    })
                except (ValueError, TypeError):
                    results.append({
                        'row': i,
                        'type': 'Frequency',
                        'error': 'Invalid data format'
                    })
        
        # ตรวจสอบ Digital Voltmeter (แถวที่ 1-5)
        for i in range(1, 6):
            setting_field = getattr(self, f'volt_uuc_setting_{i}' if i > 1 else 'volt_uuc_setting', None)
            measured_field = getattr(self, f'volt_measured_value_{i}' if i > 1 else 'volt_measured_value', None)
            tolerance_field = getattr(self, f'volt_tolerance_limit_{i}' if i > 1 else 'volt_tolerance_limit', None)
            
            if setting_field and measured_field and tolerance_field:
                try:
                    setting_val = float(setting_field)
                    measured_val = float(measured_field)
                    
                    # แปลง Tolerance Limit (รูปแบบ: "min - max" หรือ "min to max")
                    tolerance_str = str(tolerance_field).strip()
                    if ' - ' in tolerance_str:
                        min_tolerance, max_tolerance = tolerance_str.split(' - ')
                    elif ' – ' in tolerance_str:  # รองรับ en dash
                        min_tolerance, max_tolerance = tolerance_str.split(' – ')
                    elif ' to ' in tolerance_str:
                        min_tolerance, max_tolerance = tolerance_str.split(' to ')
                    else:
                        # ถ้าเป็นตัวเลขเดียว ให้ใช้เป็น ±tolerance
                        try:
                            center = float(tolerance_str)
                            min_tolerance = center - abs(center * 0.01)  # ±1%
                            max_tolerance = center + abs(center * 0.01)
                        except:
                            continue
                    
                    min_tolerance = float(min_tolerance.strip())
                    max_tolerance = float(max_tolerance.strip())
                    
                    # ตรวจสอบ UUC Setting
                    setting_in_range = min_tolerance <= setting_val <= max_tolerance
                    # ตรวจสอบ Measured Value
                    measured_in_range = min_tolerance <= measured_val <= max_tolerance
                    
                    results.append({
                        'row': i,
                        'type': 'Voltage',
                        'setting': setting_val,
                        'measured': measured_val,
                        'tolerance_min': min_tolerance,
                        'tolerance_max': max_tolerance,
                        'setting_in_range': setting_in_range,
                        'measured_in_range': measured_in_range,
                        'passed': setting_in_range and measured_in_range
                    })
                except (ValueError, TypeError):
                    results.append({
                        'row': i,
                        'type': 'Voltage',
                        'error': 'Invalid data format'
                    })
        
        return results
    
    def get_calibration_result(self):
        """คำนวณผลการสอบเทียบโดยรวม"""
        results = self.check_tolerance_limits()
        
        if not results:
            return 'no_data'
        
        # ตรวจสอบว่ามี error หรือไม่
        if any('error' in result for result in results):
            return 'error'
        
        # ตรวจสอบว่าทุกแถวผ่านหรือไม่
        all_passed = all(result.get('passed', False) for result in results)
        
        if all_passed:
            return 'passed'
        else:
            return 'failed'
    
    def auto_update_status(self):
        """อัพเดต status อัตโนมัติตามผลการสอบเทียบ"""
        result = self.get_calibration_result()
        
        if result == 'passed':
            self.status = 'passed'
        elif result == 'failed':
            self.status = 'failed'
        elif result == 'error':
            self.status = 'in_progress'  # ยังไม่สามารถประเมินได้
        
        return result
    
    class Meta:
        verbose_name = "การสอบเทียบ High Frequency"
        verbose_name_plural = "การสอบเทียบ High Frequency"

class LowFrequencyCalibration(models.Model):
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
    machine = models.ForeignKey('machine.Machine', on_delete=models.CASCADE, verbose_name="เครื่องมือ Low Frequency")
    measurement_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="ช่วงการวัด")
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
    calibrator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้สอบเทียบ", related_name='low_frequency_calibrations')
    certificate_issuer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ผู้ออกใบรับรอง", related_name='low_frequency_certificates')
    date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
    update = models.DateTimeField(auto_now=True, verbose_name="วันที่อัปเดต")
    next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
    certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="สถานะการสอบเทียบ")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal', verbose_name="ระดับความเร่งด่วน")
    
    # 1. DC VOLTAGE
    dc_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC)")
    dc_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC)")
    dc_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC)")
    dc_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC)")
    dc_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC)")
    
    # DC VOLTAGE แถว 2-5
    dc_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 2")
    dc_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 2")
    dc_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 2")
    dc_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 2")
    dc_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 2")
    
    dc_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 3")
    dc_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 3")
    dc_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 3")
    dc_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 3")
    dc_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 3")
    
    dc_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 4")
    dc_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 4")
    dc_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 4")
    dc_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 4")
    dc_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 4")
    
    dc_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 5")
    dc_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 5")
    dc_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 5")
    dc_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 5")
    dc_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 5")
    
    # 2. AC VOLTAGE
    ac_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (AC)")
    ac_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (AC)")
    ac_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (AC)")
    ac_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (AC)")
    ac_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (AC)")
    
    # AC VOLTAGE แถว 2-5
    ac_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (AC) 2")
    ac_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (AC) 2")
    ac_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (AC) 2")
    ac_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (AC) 2")
    ac_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (AC) 2")
    
    ac_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (AC) 3")
    ac_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (AC) 3")
    ac_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (AC) 3")
    ac_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (AC) 3")
    ac_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (AC) 3")
    
    ac_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (AC) 4")
    ac_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (AC) 4")
    ac_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (AC) 4")
    ac_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (AC) 4")
    ac_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (AC) 4")
    
    ac_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (AC) 5")
    ac_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (AC) 5")
    ac_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (AC) 5")
    ac_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (AC) 5")
    ac_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (AC) 5")
    
    # 3. RESISTANCE
    res_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Resistance)")
    res_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (Resistance)")
    res_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (Resistance)")
    res_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (Resistance)")
    res_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (Resistance)")
    
    # RESISTANCE แถว 2-5
    res_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Resistance) 2")
    res_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (Resistance) 2")
    res_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (Resistance) 2")
    res_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (Resistance) 2")
    res_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (Resistance) 2")
    
    res_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Resistance) 3")
    res_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (Resistance) 3")
    res_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (Resistance) 3")
    res_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (Resistance) 3")
    res_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (Resistance) 3")
    
    res_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Resistance) 4")
    res_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (Resistance) 4")
    res_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (Resistance) 4")
    res_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (Resistance) 4")
    res_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (Resistance) 4")
    
    res_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (Resistance) 5")
    res_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (Resistance) 5")
    res_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (Resistance) 5")
    res_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (Resistance) 5")
    res_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (Resistance) 5")
    
    def __str__(self):
        return f"Low Frequency Calibration - {self.machine.name}"
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='low_frequency',
            calibration_id=self.pk
        )
    
    class Meta:
        verbose_name = "การสอบเทียบ Low Frequency"
        verbose_name_plural = "การสอบเทียบ Low Frequency"

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
    std_id = models.ForeignKey('machine.CalibrationEquipment', on_delete=models.CASCADE, blank=True, null=True, verbose_name="เครื่องมือที่ใช้สอบเทียบ")
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
    
    # 1. DC VOLTAGE fields
    dc_uuc_range = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC)")
    dc_uuc_setting = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC)")
    dc_measured_value = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC)")
    dc_uncertainty = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC)")
    dc_tolerance_limit = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC)")
    
    # DC VOLTAGE แถว 2-5
    dc_uuc_range_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 2")
    dc_uuc_setting_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 2")
    dc_measured_value_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 2")
    dc_uncertainty_2 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 2")
    dc_tolerance_limit_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 2")
    
    dc_uuc_range_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 3")
    dc_uuc_setting_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 3")
    dc_measured_value_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 3")
    dc_uncertainty_3 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 3")
    dc_tolerance_limit_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 3")
    
    dc_uuc_range_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 4")
    dc_uuc_setting_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 4")
    dc_measured_value_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 4")
    dc_uncertainty_4 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 4")
    dc_tolerance_limit_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 4")
    
    dc_uuc_range_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Range (DC) 5")
    dc_uuc_setting_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="UUC Setting (DC) 5")
    dc_measured_value_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Measured Value (DC) 5")
    dc_uncertainty_5 = models.CharField(max_length=50, blank=True, null=True, verbose_name="Uncertainty (±) (DC) 5")
    dc_tolerance_limit_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tolerance Limit (DC) 5")
    
    def __str__(self):
        return f"Microwave Calibration - {self.machine.name} ({self.date_calibration})"
    
    @property
    def calibration_equipment_used(self):
        """เครื่องมือที่ใช้ในการสอบเทียบ"""
        from calibrate.models import CalibrationEquipmentUsed
        return CalibrationEquipmentUsed.objects.filter(
            calibration_type='microwave',
            calibration_id=self.pk
        )

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