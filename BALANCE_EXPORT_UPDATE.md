# การอัปเดตฟังก์ชัน Export ของ Balance

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **Balance Export**
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
  - `{{STANDARD_DESCRIPTION}}` - Description Name (ชื่อเครื่องมือ)
  - `{{STANDARD_MAKER_MODEL}}` - Maker / Model (รุ่น)
  - `{{STANDARD_SERIAL}}` - Serial Number (หมายเลขเครื่อง)
  - `{{STANDARD_DESCRIPTION_2}}` - Description Name (เครื่องมือตัวที่ 2)
  - `{{STANDARD_MAKER_MODEL_2}}` - Maker / Model (เครื่องมือตัวที่ 2)
  - `{{STANDARD_SERIAL_2}}` - Serial Number (เครื่องมือตัวที่ 2)

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ**
```python
# ข้อมูลมาตรฐาน
"{{STANDARD_DESCRIPTION}}": fmt(std.name if std else None),  # Description Name
"{{STANDARD_MAKER_MODEL}}": fmt(getattr(std, 'model', None) if std else None),  # Maker / Model
"{{STANDARD_SERIAL}}": fmt(std.serial_number if std else None),  # Serial Number
```

#### 2. **อัปเดตข้อมูลมาตรฐานชุดที่ 2**
```python
# ข้อมูลมาตรฐานชุดที่ 2 (ถ้ามี)
"{{STANDARD_DESCRIPTION_2}}": fmt(std.name if std else None),  # Description Name
"{{STANDARD_MAKER_MODEL_2}}": fmt(getattr(std, 'model', None) if std else None),  # Maker / Model
"{{STANDARD_SERIAL_2}}": fmt(std.serial_number if std else None),  # Serial Number
```

#### 3. **อัปเดตตารางเครื่องมือที่ใช้สอบเทียบ**
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

### 📋 รูปแบบข้อมูลที่ส่งออก

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

#### 1. **ตรวจสอบข้อมูลที่ส่งออก**
- ดูใน console log ว่าข้อมูลเครื่องมือที่ใช้สอบเทียบถูกส่งไปถูกต้องหรือไม่
- ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบว่าดึงจาก calibration equipment หรือไม่

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Balance ใหม่
- กรอกข้อมูลครบถ้วน
- ทดสอบการส่งออกใบรับรอง

#### 3. **ตรวจสอบผลลัพธ์**
- เปิดไฟล์ Word ที่ส่งออก
- ตรวจสอบว่าข้อมูลแสดงครบถ้วนตามที่ต้องการ
- ตรวจสอบรูปแบบตาราง
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบ

### 📝 หมายเหตุ

- ระบบจะแสดงข้อมูล '-' หากไม่มีข้อมูล
- ข้อมูลเครื่องมือที่ใช้สอบเทียบจะดึงจาก calibration equipment
- ข้อมูล Description Name จะดึงจาก `equipment.name`
- ข้อมูล Maker / Model จะดึงจาก `equipment.model`
- ข้อมูล Serial Number จะดึงจาก `equipment.serial_number`
- ข้อมูลวันที่จะแสดงในรูปแบบ dd-mm-yyyy

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออกใบรับรอง
2. **ตรวจสอบ Template** - ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
3. **ปรับแต่งเพิ่มเติม** - เพิ่มฟีเจอร์ตามความต้องการ

### 🔧 ฟังก์ชันที่อัปเดต

- `export_balance_certificate_docx()` - ฟังก์ชันหลักสำหรับส่งออกใบรับรอง Balance
- อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบให้ดึงจาก calibration equipment
- เพิ่มข้อมูลเพิ่มเติมสำหรับการแสดงผล
- เพิ่ม Debug Information สำหรับการตรวจสอบ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือที่ใช้สอบเทียบ

จากหน้าเครื่องมือที่ใช้สอบเทียบ:
- **Description Name**: `equipment.name` - ชื่อเครื่องมือ
- **Maker / Model**: `equipment.model` - รุ่น
- **Serial Number**: `equipment.serial_number` - หมายเลขเครื่อง

### 🔄 การเปลี่ยนแปลงที่สำคัญ

1. **Maker/Model Field**: เปลี่ยนจาก `equipment.description` เป็น `equipment.model`
2. **Standard Equipment**: อัปเดตให้ดึงข้อมูลจาก calibration equipment อย่างถูกต้อง
3. **Equipment Table**: อัปเดตตารางเครื่องมือที่ใช้สอบเทียบให้ดึงข้อมูลถูกต้อง

### ✅ สถานะการอัปเดต

- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
- ✅ **ตารางเครื่องมือที่ใช้สอบเทียบ** - อัปเดตให้ดึงข้อมูลถูกต้อง
- ✅ **Maker/Model Field** - อัปเดตให้ดึงจาก equipment.model
- ✅ **Description Field** - อัปเดตให้ดึงจาก equipment.name
- ✅ **Serial Field** - อัปเดตให้ดึงจาก equipment.serial_number

### 🎯 ผลลัพธ์ที่คาดหวัง

หลังจากอัปเดตแล้ว ผู้ใช้จะสามารถ:
1. **ส่งออกใบรับรอง Balance** และข้อมูลเครื่องมือที่ใช้สอบเทียบจะดึงจาก calibration equipment
2. **ดูข้อมูลเครื่องมือที่ใช้สอบเทียบ** ที่ดึงจาก calibration equipment อย่างถูกต้อง
3. **ตรวจสอบข้อมูล** ว่าทุกฟิลด์แสดงครบถ้วนตามที่ต้องการ
4. **ดูตารางเครื่องมือที่ใช้สอบเทียบ** ที่แสดงข้อมูลครบถ้วน

### 🔗 URL ที่เกี่ยวข้อง

- **Export Function**: `export_balance_certificate_docx()`
- **Model**: `BalanceCalibration`
- **Template**: `cert_templates/Balance_template.docx`
- **Equipment Model**: `CalibrationEquipment`

