# การอัปเดตฟังก์ชัน Export ของ Low Frequency และ Microwave

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **Low Frequency Export**
- ✅ **Range** - ดึงจาก `machine.range` (ช่วงการวัดหน้าเครื่องมือ)
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
  - `{{STANDARD_DESCRIPTION}}` - Description Name (ชื่อเครื่องมือ)
  - `{{STANDARD_MAKER_MODEL}}` - Maker / Model (รุ่น)
  - `{{STANDARD_SERIAL}}` - Serial Number (หมายเลขเครื่อง)

#### 2. **Microwave Export**
- ✅ **Range** - ดึงจาก `machine.range` (ช่วงการวัดหน้าเครื่องมือ)
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
  - `{{STANDARD_DESCRIPTION}}` - Description Name (ชื่อเครื่องมือ)
  - `{{STANDARD_MAKER_MODEL}}` - Maker / Model (รุ่น)
  - `{{STANDARD_SERIAL}}` - Serial Number (หมายเลขเครื่อง)

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **Low Frequency Export - อัปเดต Range**
```python
"{{RANGE}}": fmt(getattr(m, "range", None)),  # ดึงจากช่วงการวัดหน้าเครื่องมือ
```

#### 2. **Low Frequency Export - อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ**
```python
eq_rows.append({
    "no": str(idx),
    "name": fmt(getattr(e, "name", None)),  # Description Name
    "model": fmt(getattr(e, "model", None)),  # Maker / Model
    "asset": fmt(getattr(e, "asset_number", None)),
    "cert": fmt(getattr(e, "certificate_number", None)),
    "due": fmt_date(getattr(e, "due_date", None)),
    "serial": fmt(getattr(e, "serial_number", None)),  # Serial Number
})
```

#### 3. **Low Frequency Export - อัปเดต placeholder สำหรับเครื่องมือ**
```python
# เครื่องมือตัวแรก
replacements["{{STANDARD_DESCRIPTION}}"] = first_eq["name"]  # Description Name
replacements["{{STANDARD_MAKER_MODEL}}"] = first_eq["model"]  # Maker / Model
replacements["{{STANDARD_SERIAL}}"] = first_eq["serial"]  # Serial Number

# เครื่องมือตัวที่สอง
replacements["{{STANDARD_DESCRIPTION_2}}"] = second_eq["name"]  # Description Name
replacements["{{STANDARD_MAKER_MODEL_2}}"] = second_eq["model"]  # Maker / Model
replacements["{{STANDARD_SERIAL_2}}"] = second_eq["serial"]  # Serial Number
```

#### 4. **Microwave Export - อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ**
```python
'{{STANDARD_DESCRIPTION}}': standard_equipment.equipment.name if standard_equipment else '-',  # Description Name
'{{STANDARD_MAKER_MODEL}}': standard_equipment.equipment.model if standard_equipment else '-',  # Maker / Model
'{{STANDARD_SERIAL}}': standard_equipment.equipment.serial_number if standard_equipment else '-',  # Serial Number
```

### 📋 รูปแบบข้อมูลที่ส่งออก

#### 1. **ข้อมูลเครื่องมือ**
```
Model / Part Number : {{MODEL_PART_NUMBER}}
Date of Calibration : {{DATE_OF_CALIBRATION}}
Description : {{DESCRIPTION}}
Due Date : {{DUE_DATE}}
Serial Number : {{SERIAL_NUMBER}}
Range : {{RANGE}}  # ดึงจากช่วงการวัดหน้าเครื่องมือ (machine.range)
Manufacturer : {{MANUFACTURER}}
Certificate No. : {{CERTIFICATE_NO}}
```

#### 2. **ข้อมูลเครื่องมือที่ใช้สอบเทียบ (Standard Used)**
```
Description Name: {{STANDARD_DESCRIPTION}}  # ชื่อเครื่องมือ
Maker / Model: {{STANDARD_MAKER_MODEL}}  # รุ่น
Serial Number: {{STANDARD_SERIAL}}  # หมายเลขเครื่อง

Description Name: {{STANDARD_DESCRIPTION_2}}  # ชื่อเครื่องมือ (เครื่องมือตัวที่ 2)
Maker / Model: {{STANDARD_MAKER_MODEL_2}}  # รุ่น (เครื่องมือตัวที่ 2)
Serial Number: {{STANDARD_SERIAL_2}}  # หมายเลขเครื่อง (เครื่องมือตัวที่ 2)
```

### 🎯 ฟิลด์ที่ใช้ใน Model

#### 1. **ข้อมูลเครื่องมือ (Machine)**
- `machine.range` - ช่วงการวัดหน้าเครื่องมือ
- `machine.model` - รุ่นเครื่องมือ
- `machine.serial_number` - หมายเลขซีเรียล
- `machine.name` - ชื่อเครื่องมือ

#### 2. **ข้อมูลเครื่องมือที่ใช้สอบเทียบ (CalibrationEquipment)**
- `equipment.name` - ชื่อเครื่องมือ (Description Name)
- `equipment.model` - รุ่นเครื่องมือ (Maker / Model)
- `equipment.serial_number` - หมายเลขเครื่อง (Serial Number)
- `equipment.asset_number` - หมายเลขทรัพย์สิน
- `equipment.certificate_number` - หมายเลขใบรับรอง
- `equipment.due_date` - วันที่ครบกำหนด

#### 3. **ข้อมูลการสอบเทียบ**
- `cal.date_calibration` - วันที่สอบเทียบ
- `cal.next_due` - วันที่ครบกำหนด
- `cal.certificate_number` - หมายเลขใบรับรอง

### 🔍 การทดสอบ

#### 1. **ตรวจสอบข้อมูลที่ส่งออก**
- ดูใน console log ว่าข้อมูล Range ถูกส่งไปถูกต้องหรือไม่
- ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบว่าดึงจาก calibration equipment หรือไม่

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Low Frequency และ Microwave ใหม่
- กรอกข้อมูลครบถ้วน
- ทดสอบการส่งออกใบรับรอง

#### 3. **ตรวจสอบผลลัพธ์**
- เปิดไฟล์ Word ที่ส่งออก
- ตรวจสอบว่าข้อมูลแสดงครบถ้วนตามที่ต้องการ
- ตรวจสอบรูปแบบตาราง
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบ

### 📝 หมายเหตุ

- ระบบจะแสดงข้อมูล '-' หากไม่มีข้อมูล
- ข้อมูล Range จะดึงจาก `machine.range` (ฟิลด์ที่ถูกต้องใน Machine model)
- ข้อมูลเครื่องมือที่ใช้สอบเทียบจะดึงจาก calibration equipment
- ข้อมูล Description Name จะดึงจาก `equipment.name`
- ข้อมูล Maker / Model จะดึงจาก `equipment.model`
- ข้อมูล Serial Number จะดึงจาก `equipment.serial_number`
- ข้อมูลวันที่จะแสดงในรูปแบบ dd/mm/yyyy

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออก
2. **ตรวจสอบ Template** - ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
3. **ปรับแต่งเพิ่มเติม** - เพิ่มฟีเจอร์ตามความต้องการ

### 🔧 ฟังก์ชันที่อัปเดต

- `export_low_frequency_certificate_docx()` - ฟังก์ชันหลักสำหรับส่งออกใบรับรอง Low Frequency
- `export_microwave_certificate_docx()` - ฟังก์ชันหลักสำหรับส่งออกใบรับรอง Microwave
- เพิ่มข้อมูล Range จากเครื่องมือ (ใช้ฟิลด์ที่ถูกต้อง)
- อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบให้ดึงจาก calibration equipment
- เพิ่มข้อมูลเพิ่มเติมสำหรับการแสดงผล
- เพิ่ม Debug Information สำหรับการตรวจสอบ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือ

จากหน้าแก้ไขเครื่องมือ `http://127.0.0.1:8000/machine/12/edit/`:
- **ฟิลด์ Range**: `machine.range` - ช่วงการวัด
- **ฟิลด์ Model**: `machine.model` - รุ่นเครื่องมือ
- **ฟิลด์ Serial**: `machine.serial_number` - หมายเลขซีเรียล
- **ฟิลด์ Manufacturer**: `machine.manufacture` - ผู้ผลิต
- **ฟิลด์ Type**: `machine.machine_type` - ประเภทเครื่องมือ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือที่ใช้สอบเทียบ

จากหน้าเครื่องมือที่ใช้สอบเทียบ `http://127.0.0.1:8000/machine/calibration-equipment/`:
- **Description Name**: `equipment.name` - ชื่อเครื่องมือ
- **Maker / Model**: `equipment.model` - รุ่น
- **Serial Number**: `equipment.serial_number` - หมายเลขเครื่อง
