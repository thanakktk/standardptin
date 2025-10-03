# การอัปเดตฟังก์ชัน Export ของ Microwave

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **Range - ดึงจากช่วงการวัดหน้าเครื่องมือ**
- ✅ `{{RANGE}}` - ดึงจาก `machine.measurement_range` ก่อน แล้วค่อยใช้ `cal.dc_uuc_range` เป็น fallback
- ✅ ใช้ `getattr(machine, 'measurement_range', '-')` เพื่อดึงข้อมูลจากเครื่องมือ

#### 2. **ประเภท Microwave**
- ✅ `{{TYPE}}` - กำหนดเป็น 'Microwave'
- ✅ `{{CATEGORY}}` - ดึงจาก `machine.category` หรือใช้ 'Microwave' เป็น fallback
- ✅ `{{EQUIPMENT_TYPE}}` - ดึงจาก `machine.equipment_type` หรือใช้ 'Microwave' เป็น fallback

#### 3. **ข้อมูลเพิ่มเติม**
- ✅ `{{MANUFACTURER}}` - ดึงจาก `machine.manufacturer`
- ✅ `{{MODEL_PART_NUMBER}}` - รวม model และ part_number
- ✅ `{{CERTIFICATE_NO}}` - หมายเลขใบรับรอง

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **อัปเดต Range**
```python
'{{RANGE}}': getattr(machine, 'measurement_range', '-') or cal.dc_uuc_range or '-',  # ดึงจากช่วงการวัดหน้าเครื่องมือ
```

#### 2. **เพิ่มข้อมูลประเภท Microwave**
```python
'{{TYPE}}': 'Microwave',  # ประเภท Microwave
'{{CATEGORY}}': getattr(machine, 'category', '-') or 'Microwave',  # หมวดหมู่
'{{EQUIPMENT_TYPE}}': getattr(machine, 'equipment_type', '-') or 'Microwave',  # ประเภทเครื่องมือ
```

#### 3. **เพิ่มข้อมูลเพิ่มเติม**
```python
'{{MANUFACTURER}}': getattr(machine, 'manufacturer', '-') or '-',
'{{MODEL_PART_NUMBER}}': f"{machine.model or '-'} / {getattr(machine, 'part_number', '-')}" if getattr(machine, 'part_number', None) else machine.model or '-',
'{{CERTIFICATE_NO}}': cal.certificate_number or '-',
```

#### 4. **เพิ่ม Debug Information**
```python
# Debug: แสดงข้อมูลที่ส่งไป template
print("DEBUG: === MICROWAVE REPLACEMENTS SENT TO TEMPLATE ===")
for key, value in replacements.items():
    if 'RANGE' in key or 'TYPE' in key or 'CATEGORY' in key or 'EQUIPMENT_TYPE' in key or 'MODEL' in key or 'MANUFACTURER' in key:
        print(f"DEBUG: {key}: {value}")
print("DEBUG: === END MICROWAVE REPLACEMENTS ===")

# Debug: แสดงข้อมูลเครื่องมือ
print(f"DEBUG: Machine Range: {getattr(machine, 'measurement_range', 'NOT_FOUND')}")
print(f"DEBUG: Machine Type: {getattr(machine, 'type', 'NOT_FOUND')}")
print(f"DEBUG: Machine Category: {getattr(machine, 'category', 'NOT_FOUND')}")
print(f"DEBUG: Machine Equipment Type: {getattr(machine, 'equipment_type', 'NOT_FOUND')}")
print(f"DEBUG: Machine Manufacturer: {getattr(machine, 'manufacturer', 'NOT_FOUND')}")
```

### 📋 รูปแบบข้อมูลที่ส่งออก

#### 1. **ข้อมูลเครื่องมือ**
```
Model / Part Number : {{MODEL_PART_NUMBER}}
Date of Calibration : {{DATE_OF_CALIBRATION}}
Description : {{DESCRIPTION}}
Due Date : {{DUE_DATE}}
Serial Number : {{SERIAL_NUMBER}}
Range : {{RANGE}}  # ดึงจากช่วงการวัดหน้าเครื่องมือ
Manufacturer : {{MANUFACTURER}}
Certificate No. : {{CERTIFICATE_NO}}
Type : {{TYPE}}  # ประเภท Microwave
Category : {{CATEGORY}}  # หมวดหมู่
Equipment Type : {{EQUIPMENT_TYPE}}  # ประเภทเครื่องมือ
```

#### 2. **ข้อมูลตาราง DC Voltage (5 แถว)**
```
{{DC_UUC_RANGE}}     {{DC_UUC_SETTING}}     {{DC_MEASURED_VALUE}}     {{DC_UNCERTAINTY}}     {{DC_TOLERANCE_LIMIT}}
{{DC_UUC_RANGE_2}}   {{DC_UUC_SETTING_2}}   {{DC_MEASURED_VALUE_2}}   {{DC_UNCERTAINTY_2}}   {{DC_TOLERANCE_LIMIT_2}}
{{DC_UUC_RANGE_3}}   {{DC_UUC_SETTING_3}}   {{DC_MEASURED_VALUE_3}}   {{DC_UNCERTAINTY_3}}   {{DC_TOLERANCE_LIMIT_3}}
{{DC_UUC_RANGE_4}}   {{DC_UUC_SETTING_4}}   {{DC_MEASURED_VALUE_4}}   {{DC_UNCERTAINTY_4}}   {{DC_TOLERANCE_LIMIT_4}}
{{DC_UUC_RANGE_5}}   {{DC_UUC_SETTING_5}}   {{DC_MEASURED_VALUE_5}}   {{DC_UNCERTAINTY_5}}   {{DC_TOLERANCE_LIMIT_5}}
```

### 🎯 ฟิลด์ที่ใช้ใน Model

#### 1. **ข้อมูลเครื่องมือ (Machine)**
- `machine.measurement_range` - ช่วงการวัดหน้าเครื่องมือ
- `machine.model` - รุ่นเครื่องมือ
- `machine.part_number` - หมายเลขชิ้นส่วน
- `machine.manufacturer` - ผู้ผลิต
- `machine.category` - หมวดหมู่
- `machine.equipment_type` - ประเภทเครื่องมือ

#### 2. **ข้อมูลการสอบเทียบ (MicrowaveCalibration)**
- `cal.dc_uuc_range` - ช่วงการวัด (fallback)
- `cal.certificate_number` - หมายเลขใบรับรอง
- `cal.date_calibration` - วันที่สอบเทียบ
- `cal.next_due` - วันที่ครบกำหนด

#### 3. **ข้อมูลตาราง DC Voltage**
- `cal.dc_uuc_range` ถึง `cal.dc_uuc_range_5` - ช่วงการวัด
- `cal.dc_uuc_setting` ถึง `cal.dc_uuc_setting_5` - ค่าตั้งต้น
- `cal.dc_measured_value` ถึง `cal.dc_measured_value_5` - ค่าที่วัดได้
- `cal.dc_uncertainty` ถึง `cal.dc_uncertainty_5` - ค่าความไม่แน่นอน
- `cal.dc_tolerance_limit` ถึง `cal.dc_tolerance_limit_5` - ขีดจำกัดความคลาดเคลื่อน

### 🔍 การทดสอบ

#### 1. **ตรวจสอบข้อมูลที่ส่งออก**
- ดูใน console log ว่าข้อมูล Range ถูกส่งไปถูกต้องหรือไม่
- ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Microwave ใหม่
- กรอกข้อมูลครบถ้วน
- ทดสอบการส่งออกใบรับรอง

#### 3. **ตรวจสอบผลลัพธ์**
- เปิดไฟล์ Word ที่ส่งออก
- ตรวจสอบว่าข้อมูลแสดงครบถ้วนตามที่ต้องการ
- ตรวจสอบรูปแบบตาราง

### 📝 หมายเหตุ

- ระบบจะแสดงข้อมูล '-' หากไม่มีข้อมูล
- ข้อมูล Range จะดึงจาก `machine.measurement_range` ก่อน แล้วค่อยใช้ `cal.dc_uuc_range` เป็น fallback
- ข้อมูลประเภทจะแสดงเป็น 'Microwave' ตามที่กำหนด
- ข้อมูลวันที่จะแสดงในรูปแบบ dd/mm/yyyy

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออก
2. **ตรวจสอบ Template** - ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
3. **ปรับแต่งเพิ่มเติม** - เพิ่มฟีเจอร์ตามความต้องการ

### 🔧 ฟังก์ชันที่อัปเดต

- `export_microwave_certificate_docx()` - ฟังก์ชันหลักสำหรับส่งออกใบรับรอง Microwave
- เพิ่มข้อมูล Range จากเครื่องมือ
- เพิ่มข้อมูลประเภท Microwave
- เพิ่มข้อมูลเพิ่มเติมสำหรับการแสดงผล
- เพิ่ม Debug Information สำหรับการตรวจสอบ
