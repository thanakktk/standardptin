# การเพิ่มฟิลด์ Certificate Number ใน Dial Gauge

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **Dial Gauge Calibration Form**
- ✅ **เพิ่มฟิลด์ Certificate Number** - ให้ผู้ใช้สามารถกรอกหมายเลขใบรับรองได้
- ✅ **อัปเดตฟอร์ม** - เพิ่มฟิลด์ certificate_number ใน DialGaugeCalibrationForm
- ✅ **อัปเดต Template** - เพิ่มฟิลด์ certificate_number ในหน้าแก้ไข
- ✅ **สร้าง Migration** - สร้าง migration สำหรับฟิลด์ใหม่

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **อัปเดตโมเดล DialGaugeCalibration**
```python
# ข้อมูลการสอบเทียบ
date_calibration = models.DateField(verbose_name="วันที่สอบเทียบ")
update = models.DateField(blank=True, null=True, verbose_name="วันที่อัปเดต")
next_due = models.DateField(blank=True, null=True, verbose_name="วันที่ครบกำหนดสอบเทียบถัดไป")
certificate_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="หมายเลขใบรับรอง")
```

#### 2. **อัปเดตฟอร์ม DialGaugeCalibrationForm**
```python
fields = ['measurement_range', 'update', 'next_due', 'status', 'std_id', 'calibrator', 'certificate_issuer', 'certificate_number',
          'uuc_set', 'actual', 'error', 'uncertainty', 'tolerance_limit',
          'set_2', 'actual_2', 'error_2', 'tolerance_limit_2',
          'set_3', 'actual_3', 'error_3', 'tolerance_limit_3',
          'set_4', 'actual_4', 'error_4', 'tolerance_limit_4',
          'set_5', 'actual_5', 'error_5', 'tolerance_limit_5']
```

#### 3. **เพิ่ม Widget สำหรับฟิลด์ Certificate Number**
```python
'certificate_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'เช่น DG-2024-001'}),
```

#### 4. **อัปเดต Template dial_gauge_form.html**
```html
<div class="row mb-3">
    <div class="col-md-4">
        <label for="{{ form.certificate_number.id_for_label }}" class="form-label">
            <i class="fas fa-hashtag me-1"></i>{{ form.certificate_number.label }}
        </label>
        {{ form.certificate_number }}
        {% if form.certificate_number.errors %}
            <div class="text-danger small">{{ form.certificate_number.errors.0 }}</div>
        {% endif %}
    </div>
</div>
```

### 📋 รูปแบบข้อมูลที่แสดงในฟอร์ม

#### ฟิลด์ Certificate Number
```
หมายเลขใบรับรอง: [DG-2024-001]  # ฟิลด์ใหม่ที่เพิ่มเข้ามา
```

### 🎯 ฟิลด์ที่ใช้ใน Model

#### ข้อมูลการสอบเทียบ Dial Gauge
- `certificate_number` - หมายเลขใบรับรอง (ฟิลด์ใหม่)
- `date_calibration` - วันที่สอบเทียบ
- `update` - วันที่อัปเดต
- `next_due` - วันที่ครบกำหนดสอบเทียบถัดไป
- `status` - สถานะสอบเทียบ
- `calibrator` - ผู้สอบเทียบ
- `certificate_issuer` - ผู้ออกใบรับรอง

### 🔍 การทดสอบ

#### 1. **ตรวจสอบฟิลด์ใหม่**
- เข้าหน้าแก้ไขการสอบเทียบ Dial Gauge
- ตรวจสอบว่าฟิลด์ Certificate Number แสดงขึ้นมา
- ทดสอบกรอกข้อมูลและบันทึก

#### 2. **ทดสอบการบันทึก**
- กรอกหมายเลขใบรับรอง
- บันทึกข้อมูล
- ตรวจสอบว่าข้อมูลถูกบันทึกในฐานข้อมูล

#### 3. **ตรวจสอบการแสดงผล**
- ดูรายการการสอบเทียบ Dial Gauge
- ตรวจสอบว่าหมายเลขใบรับรองแสดงขึ้นมา
- ทดสอบการส่งออกใบรับรอง

### 📝 หมายเหตุ

- ฟิลด์ `certificate_number` เป็นฟิลด์ที่สามารถเว้นว่างได้ (blank=True, null=True)
- ฟิลด์นี้จะแสดงในหน้าแก้ไขการสอบเทียบ Dial Gauge
- ฟิลด์นี้จะถูกใช้ในการส่งออกใบรับรอง
- ฟิลด์นี้จะแสดงในรายการการสอบเทียบ

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบฟิลด์ใหม่** - เข้าหน้าแก้ไขการสอบเทียบ Dial Gauge และทดสอบฟิลด์ใหม่
2. **ตรวจสอบการบันทึก** - ทดสอบการบันทึกข้อมูลและตรวจสอบว่าข้อมูลถูกบันทึก
3. **ทดสอบการส่งออก** - ทดสอบการส่งออกใบรับรองและตรวจสอบว่าหมายเลขใบรับรองแสดงขึ้นมา

### 🔧 ฟังก์ชันที่อัปเดต

- `DialGaugeCalibration` model - เพิ่มฟิลด์ certificate_number
- `DialGaugeCalibrationForm` - เพิ่มฟิลด์ certificate_number ในฟอร์ม
- `dial_gauge_form.html` template - เพิ่มฟิลด์ certificate_number ในหน้าแก้ไข
- Migration `0045_dialgaugecalibration_certificate_number` - เพิ่มฟิลด์ในฐานข้อมูล

### 📊 ข้อมูลที่เพิ่มเข้ามา

#### ฟิลด์ Certificate Number
- **ชื่อฟิลด์**: `certificate_number`
- **ประเภท**: `CharField`
- **ความยาว**: `max_length=100`
- **การตั้งค่า**: `blank=True, null=True`
- **คำอธิบาย**: "หมายเลขใบรับรอง"
- **Placeholder**: "เช่น DG-2024-001"

### 🔄 การเปลี่ยนแปลงที่สำคัญ

1. **โมเดล**: เพิ่มฟิลด์ `certificate_number` ใน `DialGaugeCalibration`
2. **ฟอร์ม**: เพิ่มฟิลด์ `certificate_number` ใน `DialGaugeCalibrationForm`
3. **Template**: เพิ่มฟิลด์ `certificate_number` ในหน้าแก้ไข
4. **Migration**: สร้าง migration เพื่อเพิ่มฟิลด์ในฐานข้อมูล

### ✅ สถานะการอัปเดต

- ✅ **โมเดล** - เพิ่มฟิลด์ certificate_number
- ✅ **ฟอร์ม** - อัปเดต DialGaugeCalibrationForm
- ✅ **Template** - อัปเดต dial_gauge_form.html
- ✅ **Migration** - สร้างและรัน migration
- ✅ **ฐานข้อมูล** - อัปเดตโครงสร้างฐานข้อมูล

### 🎯 ผลลัพธ์ที่คาดหวัง

หลังจากอัปเดตแล้ว ผู้ใช้จะสามารถ:
1. **กรอกหมายเลขใบรับรอง** ในหน้าแก้ไขการสอบเทียบ Dial Gauge
2. **บันทึกข้อมูล** และหมายเลขใบรับรองจะถูกบันทึกในฐานข้อมูล
3. **ดูหมายเลขใบรับรอง** ในรายการการสอบเทียบ
4. **ส่งออกใบรับรอง** และหมายเลขใบรับรองจะแสดงในเอกสาร

### 🔗 URL ที่เกี่ยวข้อง

- **หน้าแก้ไข**: `http://127.0.0.1:8000/calibrate/dial-gauge/2/edit/`
- **ฟอร์ม**: `DialGaugeCalibrationForm`
- **Template**: `calibrate/templates/calibrate/dial_gauge_form.html`
- **Model**: `DialGaugeCalibration`
