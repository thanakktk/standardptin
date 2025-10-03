# การอัปเดตฟังก์ชัน Export ของ Torque

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **Torque Export**
- ✅ **Range** - ดึงจากช่วงการวัดหน้าเครื่องมือ (`machine.range`)
- ✅ **Description** - ดึงชื่อเครื่องมือประเภทมา (`machine.name`)
- ✅ **Manufacturer** - ดึงผู้ผลิตมา (`machine.manufacture`)
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
  - `{{STANDARD_DESCRIPTION}}` - Description Name (ชื่อเครื่องมือ)
  - `{{STANDARD_MAKER_MODEL}}` - Maker / Model (รุ่น)
  - `{{STANDARD_SERIAL}}` - Serial Number (หมายเลขเครื่อง)

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **อัปเดต Range, Description, และ Manufacturer**
```python
# ข้อมูลเครื่องมือ
'{{MODEL}}': getattr(cal.uuc_id, 'model', '-'),
'{{MANUFACTURER}}': getattr(cal.uuc_id, 'manufacture', '-'),  # ดึงผู้ผลิตมา
'{{DESCRIPTION}}': getattr(cal.uuc_id, 'name', '-'),  # ดึงชื่อเครื่องมือประเภทมา
'{{SERIAL_NUMBER}}': getattr(cal.uuc_id, 'serial_number', '-'),
'{{ASSET_NUMBER}}': getattr(cal.uuc_id, 'asset_number', '-'),
'{{RANGE}}': getattr(cal.uuc_id, 'range', '-'),  # ดึงจากช่วงการวัดหน้าเครื่องมือ
```

#### 2. **อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบ**
```python
# ข้อมูลมาตรฐาน
'{{STANDARD_DESCRIPTION}}': std.name or '-',  # Description Name
'{{STANDARD_MAKER_MODEL}}': getattr(std, 'model', '-'),  # Maker / Model
'{{STANDARD_SERIAL}}': std.serial_number or '-',  # Serial Number
```

#### 3. **อัปเดตข้อมูลมาตรฐานชุดที่ 2**
```python
# ข้อมูลมาตรฐานชุดที่ 2
'{{STANDARD_DESCRIPTION_2}}': eq2.name or '-',  # Description Name
'{{STANDARD_MAKER_MODEL_2}}': getattr(eq2, 'model', '-'),  # Maker / Model
'{{STANDARD_SERIAL_2}}': eq2.serial_number or '-',  # Serial Number
```

### 📋 รูปแบบข้อมูลที่ส่งออก

#### ข้อมูลเครื่องมือ
```
Model: {{MODEL}}
Manufacturer: {{MANUFACTURER}}  # ดึงผู้ผลิตมา
Description: {{DESCRIPTION}}  # ดึงชื่อเครื่องมือประเภทมา
Serial Number: {{SERIAL_NUMBER}}
Asset Number: {{ASSET_NUMBER}}
Range: {{RANGE}}  # ดึงจากช่วงการวัดหน้าเครื่องมือ
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
- `machine.name` - ชื่อเครื่องมือประเภท
- `machine.model` - รุ่นเครื่องมือ
- `machine.serial_number` - หมายเลขซีเรียล
- `machine.manufacture` - ผู้ผลิต

#### ข้อมูลเครื่องมือที่ใช้สอบเทียบ (CalibrationEquipment)
- `equipment.name` - ชื่อเครื่องมือ (Description Name)
- `equipment.model` - รุ่นเครื่องมือ (Maker / Model)
- `equipment.serial_number` - หมายเลขเครื่อง (Serial Number)
- `equipment.asset_number` - หมายเลขทรัพย์สิน
- `equipment.certificate_number` - หมายเลขใบรับรอง
- `equipment.due_date` - วันที่ครบกำหนด

#### ข้อมูลการสอบเทียบ
- `cal.update` - วันที่สอบเทียบ
- `cal.next_due` - วันที่ครบกำหนด
- `cal.certificate_number` - หมายเลขใบรับรอง

### 🔍 การทดสอบ

#### 1. **ตรวจสอบข้อมูลที่ส่งออก**
- ดูใน console log ว่าข้อมูล Range, Description, Manufacturer ถูกส่งไปถูกต้องหรือไม่
- ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
- ตรวจสอบข้อมูลเครื่องมือที่ใช้สอบเทียบว่าดึงจาก calibration equipment หรือไม่

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Torque ใหม่
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
- ข้อมูล Description จะดึงจาก `machine.name` (ชื่อเครื่องมือประเภท)
- ข้อมูล Manufacturer จะดึงจาก `machine.manufacture` (ผู้ผลิต)
- ข้อมูลเครื่องมือที่ใช้สอบเทียบจะดึงจาก calibration equipment
- ข้อมูล Description Name จะดึงจาก `equipment.name`
- ข้อมูล Maker / Model จะดึงจาก `equipment.model`
- ข้อมูล Serial Number จะดึงจาก `equipment.serial_number`
- ข้อมูลวันที่จะแสดงในรูปแบบ dd/mm/yyyy

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออกใบรับรอง
2. **ตรวจสอบ Template** - ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
3. **ปรับแต่งเพิ่มเติม** - เพิ่มฟีเจอร์ตามความต้องการ

### 🔧 ฟังก์ชันที่อัปเดต

- `export_torque_certificate_docx()` - ฟังก์ชันหลักสำหรับส่งออกใบรับรอง Torque
- เพิ่มข้อมูล Range จากเครื่องมือ (ใช้ฟิลด์ที่ถูกต้อง)
- อัปเดตข้อมูล Description ให้ดึงจากชื่อเครื่องมือประเภท
- อัปเดตข้อมูล Manufacturer ให้ดึงจากผู้ผลิต
- อัปเดตข้อมูลเครื่องมือที่ใช้สอบเทียบให้ดึงจาก calibration equipment
- เพิ่มข้อมูลเพิ่มเติมสำหรับการแสดงผล
- เพิ่ม Debug Information สำหรับการตรวจสอบ

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือ

จากหน้าแก้ไขเครื่องมือ:
- **ฟิลด์ Range**: `machine.range` - ช่วงการวัด
- **ฟิลด์ Description**: `machine.name` - ชื่อเครื่องมือประเภท
- **ฟิลด์ Manufacturer**: `machine.manufacture` - ผู้ผลิต
- **ฟิลด์ Model**: `machine.model` - รุ่นเครื่องมือ
- **ฟิลด์ Serial**: `machine.serial_number` - หมายเลขซีเรียล

### 📊 ข้อมูลที่ดึงจากหน้าเครื่องมือที่ใช้สอบเทียบ

จากหน้าเครื่องมือที่ใช้สอบเทียบ:
- **Description Name**: `equipment.name` - ชื่อเครื่องมือ
- **Maker / Model**: `equipment.model` - รุ่น
- **Serial Number**: `equipment.serial_number` - หมายเลขเครื่อง

### 🔄 การเปลี่ยนแปลงที่สำคัญ

1. **Range Field**: เปลี่ยนจาก `cal.measurement_range` เป็น `cal.uuc_id.range`
2. **Description Field**: เปลี่ยนจาก `cal.uuc_id.description` เป็น `cal.uuc_id.name`
3. **Manufacturer Field**: เปลี่ยนจาก `cal.uuc_id.manufacturer` เป็น `cal.uuc_id.manufacture`
4. **Standard Equipment**: อัปเดตให้ดึงข้อมูลจาก calibration equipment อย่างถูกต้อง
5. **Maker/Model Field**: เปลี่ยนจาก `equipment.maker_model` เป็น `equipment.model`

### ✅ สถานะการอัปเดต

- ✅ **Range** - ดึงจากช่วงการวัดหน้าเครื่องมือ
- ✅ **Description** - ดึงชื่อเครื่องมือประเภทมา
- ✅ **Manufacturer** - ดึงผู้ผลิตมา
- ✅ **ข้อมูลเครื่องมือที่ใช้สอบเทียบ** - ดึงจาก calibration equipment
- ✅ **ตารางเครื่องมือที่ใช้สอบเทียบ** - อัปเดตให้ดึงข้อมูลถูกต้อง

### 🎯 ผลลัพธ์ที่คาดหวัง

หลังจากอัปเดตแล้ว ผู้ใช้จะสามารถ:
1. **ส่งออกใบรับรอง Torque** และข้อมูล Range จะดึงจากช่วงการวัดหน้าเครื่องมือ
2. **ดูข้อมูล Description** ที่ดึงจากชื่อเครื่องมือประเภท
3. **ดูข้อมูล Manufacturer** ที่ดึงจากผู้ผลิต
4. **ดูข้อมูลเครื่องมือที่ใช้สอบเทียบ** ที่ดึงจาก calibration equipment อย่างถูกต้อง
5. **ตรวจสอบข้อมูล** ว่าทุกฟิลด์แสดงครบถ้วนตามที่ต้องการ

### 🔗 URL ที่เกี่ยวข้อง

- **Export Function**: `export_torque_certificate_docx()`
- **Model**: `CalibrationTorque`
- **Template**: `cert_templates/Torque_template.docx`
- **Equipment Model**: `CalibrationEquipment`
