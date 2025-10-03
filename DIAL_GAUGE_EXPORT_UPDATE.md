# การอัปเดตฟังก์ชัน Export ของ Dial Gauge

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **ย้ายฟิลด์ "หมายเลขใบรับรอง" ไปอยู่แถวที่ 2**
- ✅ **Template** - ย้ายฟิลด์ certificate_number ไปอยู่แถวที่ 2 (หลังจาก calibrator และ certificate_issuer)

#### 2. **อัปเดต Export Dial Gauge**
- ✅ **Range** - ดึงจากช่วงการวัดหน้าเครื่องมือ (`machine.range`)
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
  - `{{STANDARD_DESCRIPTION}}` - Description Name (ชื่อเครื่องมือ)
  - `{{STANDARD_MAKER_MODEL}}` - Maker / Model (รุ่น)
  - `{{STANDARD_SERIAL}}` - Serial Number (หมายเลขเครื่อง)

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **ย้ายฟิลด์ Certificate Number ไปอยู่แถวที่ 2**
```html
<!-- แถวที่ 1: Calibrator, Certificate Issuer, Certificate Number -->
<div class="row mb-3">
    <div class="col-md-4">
        <label for="{{ form.calibrator.id_for_label }}" class="form-label">
            <i class="fas fa-user me-1"></i>{{ form.calibrator.label }}
        </label>
        {{ form.calibrator }}
    </div>
    <div class="col-md-4">
        <label for="{{ form.certificate_issuer.id_for_label }}" class="form-label">
            <i class="fas fa-certificate me-1"></i>{{ form.certificate_issuer.label }}
        </label>
        {{ form.certificate_issuer }}
    </div>
    <div class="col-md-4">
        <label for="{{ form.certificate_number.id_for_label }}" class="form-label">
            <i class="fas fa-hashtag me-1"></i>{{ form.certificate_number.label }}
        </label>
        {{ form.certificate_number }}
    </div>
</div>
```

#### 2. **อัปเดต Export Dial Gauge - Range**
```python
# ข้อมูลเครื่องมือ
"{{RANGE}}": fmt(m.range),  # ดึงจากช่วงการวัดหน้าเครื่องมือ
```

#### 3. **อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ**
```python
# ข้อมูลมาตรฐาน
"{{STANDARD_DESCRIPTION}}": fmt(std.name if std else None),  # Description Name
"{{STANDARD_MAKER_MODEL}}": fmt(getattr(std, 'model', None) if std else None),  # Maker / Model
"{{STANDARD_SERIAL}}": fmt(std.serial_number if std else None),  # Serial Number
```

#### 4. **อัปเดตตารางเครื่องมือที่ใช้สอบเทียบ**
```python
eq_rows.append({
    "no": str(i),
    "name": fmt(eq.equipment.name),  # Description Name
    "model": fmt(eq.equipment.model),  # Maker / Model
    "asset": fmt(getattr(eq.equipment, 'asset_number', None) or getattr(eq.equipment, 'serial_number', '-')),
    "cert": fmt(getattr(eq.equipment, 'certificate_number', None) or getattr(eq.equipment, 'certificate', '-')),
    "due": fmt_date(getattr(eq.equipment, 'due_date', None)),
})
```

### 📋 รูปแบบข้อมูลที่แสดงในฟอร์ม

#### แถวที่ 1: ข้อมูลการสอบเทียบ
```
ช่วงการวัด | วันที่อัปเดต | วันที่ครบกำหนด
```

#### แถวที่ 2: ข้อมูลผู้รับผิดชอบ
```
ผู้สอบเทียบ | ผู้ออกใบรับรอง | หมายเลขใบรับรอง
```

#### แถวที่ 3: เครื่องมือที่ใช้สอบเทียบ
```
เครื่องมือที่ใช้สอบเทียบ
```

### 📋 รูปแบบข้อมูลที่ส่งออก

#### ข้อมูลเครื่องมือ
```
Model: {{MODEL}}
Manufacturer: {{MANUFACTURER}}
Description: {{DESCRIPTION}}
Serial Number: {{SERIAL_NUMBER}}
Range: {{RANGE}}  # ดึงจากช่วงการวัดหน้าเครื่องมือ
Graduation: {{GRADUATION}}
Option: {{OPTION}}
Customer Asset ID: {{CUSTOMER_ASSET_ID}}
```

#### ข้อมูลเครื่องมือที่ใช้สอบเทียบ (Standard Used)
```
Description Name: {{STANDARD_DESCRIPTION}}  # ชื่อเครื่องมือ
Maker / Model: {{STANDARD_MAKER_MODEL}}  # รุ่น
Serial Number: {{STANDARD_SERIAL}}  # หมายเลขเครื่อง

Description Name: {{STANDARD_DESCRIPTION_2}}  # ชื่อเครื่องมือ (เครื่องมือตัวที่ 2)
Maker / Model: {{STANDARD_MAKER_MODEL_2}}  # รุ่น (เครื่องมือตัวที่ 2)
Serial Number: {{STANDARD_SERIAL_2}}  # หมายเลขเครื่อง (เครื่องมือตัวที่ 2)
```

### 🎯 ฟิลด์ที่ใช้ใน Model

#### ข้อมูลเครื่องมือ (Machine)
- `machine.range` - ช่วงการวัดหน้าเครื่องมือ
- `machine.model` - รุ่นเครื่องมือ
- `machine.serial_number` - หมายเลขซีเรียล
- `machine.manufacture` - ผู้ผลิต
- `machine.name` - ชื่อเครื่องมือ

#### ข้อมูลเครื่องมือที่ใช้สอบเทียบ (CalibrationEquipment)
- `equipment.name` - ชื่อเครื่องมือ (Description Name)
- `equipment.model` - รุ่นเครื่องมือ (Maker / Model)
- `equipment.serial_number` - หมายเลขเครื่อง (Serial Number)
- `equipment.asset_number` - หมายเลขทรัพย์สิน
- `equipment.certificate_number` - หมายเลขใบรับรอง
- `equipment.due_date` - วันที่ครบกำหนด

#### ข้อมูลการสอบเทียบ
- `cal.date_calibration` - วันที่สอบเทียบ
- `cal.next_due` - วันที่ครบกำหนด
- `cal.certificate_number` - หมายเลขใบรับรอง

### 🔍 การทดสอบ

#### 1. **ตรวจสอบการย้ายฟิลด์**
- เข้าหน้าแก้ไขการสอบเทียบ Dial Gauge
- ตรวจสอบว่าฟิลด์ "หมายเลขใบรับรอง" อยู่แถวที่ 2
- ตรวจสอบว่าฟิลด์แสดงในตำแหน่งที่ถูกต้อง

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Dial Gauge ใหม่
- กรอกข้อมูลครบถ้วน
- ทดสอบการส่งออกใบรับรอง

#### 3. **ตรวจสอบผลลัพธ์**
- เปิดไฟล์ Word ที่ส่งออก
- ตรวจสอบว่าข้อมูล Range ดึงจากช่วงการวัดหน้าเครื่องมือ
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบ

### 📝 หมายเหตุ

- ฟิลด์ "หมายเลขใบรับรอง" ถูกย้ายไปอยู่แถวที่ 2 (หลังจาก calibrator และ certificate_issuer)
- ข้อมูล Range จะดึงจาก `machine.range` (ฟิลด์ที่ถูกต้องใน Machine model)
- ข้อมูลเครื่องมือที่ใช้สอบเทียบจะดึงจาก calibration equipment
- ข้อมูล Description Name จะดึงจาก `equipment.name`
- ข้อมูล Maker / Model จะดึงจาก `equipment.model`
- ข้อมูล Serial Number จะดึงจาก `equipment.serial_number`
- ข้อมูลวันที่จะแสดงในรูปแบบ dd-mm-yyyy

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการย้ายฟิลด์** - เข้าหน้าแก้ไขการสอบเทียบ Dial Gauge และตรวจสอบตำแหน่งฟิลด์
2. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออกใบรับรอง
3. **ตรวจสอบผลลัพธ์** - เปิดไฟล์ Word ที่ส่งออกและตรวจสอบข้อมูล

### 🔧 ฟังก์ชันที่อัปเดต

- `dial_gauge_form.html` template - ย้ายฟิลด์ certificate_number ไปอยู่แถวที่ 2
- `export_dial_gauge_certificate_docx()` - อัปเดตการดึงข้อมูล Range และเครื่องมือที่ใช้สอบเทียบ
- เพิ่มข้อมูล Range จากเครื่องมือ (ใช้ฟิลด์ที่ถูกต้อง)
- อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบให้ดึงจาก calibration equipment
- เพิ่มข้อมูลเพิ่มเติมสำหรับการแสดงผล
- เพิ่ม Debug Information สำหรับการตรวจสอบ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือ

จากหน้าแก้ไขเครื่องมือ:
- **ฟิลด์ Range**: `machine.range` - ช่วงการวัด
- **ฟิลด์ Model**: `machine.model` - รุ่นเครื่องมือ
- **ฟิลด์ Serial**: `machine.serial_number` - หมายเลขซีเรียล
- **ฟิลด์ Manufacturer**: `machine.manufacture` - ผู้ผลิต
- **ฟิลด์ Name**: `machine.name` - ชื่อเครื่องมือ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือที่ใช้สอบเทียบ

จากหน้าเครื่องมือที่ใช้สอบเทียบ:
- **Description Name**: `equipment.name` - ชื่อเครื่องมือ
- **Maker / Model**: `equipment.model` - รุ่น
- **Serial Number**: `equipment.serial_number` - หมายเลขเครื่อง

### 🔄 การเปลี่ยนแปลงที่สำคัญ

1. **Template**: ย้ายฟิลด์ certificate_number ไปอยู่แถวที่ 2
2. **Export Range**: เปลี่ยนจาก `cal.measurement_range` เป็น `machine.range`
3. **Export Equipment**: อัปเดตให้ดึงข้อมูลจาก calibration equipment อย่างถูกต้อง
4. **Export Maker/Model**: เปลี่ยนจาก `equipment.description` เป็น `equipment.model`

### ✅ สถานะการอัปเดต

- ✅ **Template** - ย้ายฟิลด์ certificate_number ไปอยู่แถวที่ 2
- ✅ **Export Range** - ดึงจากช่วงการวัดหน้าเครื่องมือ
- ✅ **Export Equipment** - อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ
- ✅ **Export Maker/Model** - อัปเดตให้ดึงจาก equipment.model
- ✅ **Export Description** - อัปเดตให้ดึงจาก equipment.name
- ✅ **Export Serial** - อัปเดตให้ดึงจาก equipment.serial_number

### 🎯 ผลลัพธ์ที่คาดหวัง

หลังจากอัปเดตแล้ว ผู้ใช้จะสามารถ:
1. **เห็นฟิลด์ "หมายเลขใบรับรอง" อยู่แถวที่ 2** ในหน้าแก้ไขการสอบเทียบ Dial Gauge
2. **ส่งออกใบรับรอง** และข้อมูล Range จะดึงจากช่วงการวัดหน้าเครื่องมือ
3. **ดูข้อมูลเครื่องมือที่ใช้สอบเทียบ** ที่ดึงจาก calibration equipment อย่างถูกต้อง
4. **ตรวจสอบข้อมูล** ว่าทุกฟิลด์แสดงครบถ้วนตามที่ต้องการ

### 🔗 URL ที่เกี่ยวข้อง

- **หน้าแก้ไข**: `http://127.0.0.1:8000/calibrate/dial-gauge/2/edit/`
- **Template**: `calibrate/templates/calibrate/dial_gauge_form.html`
- **Export Function**: `export_dial_gauge_certificate_docx()`
- **Model**: `DialGaugeCalibration`
