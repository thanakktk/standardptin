# การอัปเดตฟังก์ชัน Export ของ Pressure

## สรุปการเปลี่ยนแปลง

### ✅ ข้อมูลที่อัปเดตแล้ว

#### 1. **ข้อมูลตารางผลการสอบเทียบ (6 แถว)**
- ✅ แถวที่ 1: `{{SET}}`, `{{ACTUAL}}`, `{{ERROR}}`, `{{TOLERANCE_START}}`, `{{TOLERANCE_END}}`
- ✅ แถวที่ 2: `{{SET_2}}`, `{{ACTUAL_2}}`, `{{ERROR_2}}`, `{{TOLERANCE_START_2}}`, `{{TOLERANCE_END_2}}`
- ✅ แถวที่ 3: `{{SET_3}}`, `{{ACTUAL_3}}`, `{{ERROR_3}}`, `{{TOLERANCE_START_3}}`, `{{TOLERANCE_END_3}}`
- ✅ แถวที่ 4: `{{SET_4}}`, `{{ACTUAL_4}}`, `{{ERROR_4}}`, `{{TOLERANCE_START_4}}`, `{{TOLERANCE_END_4}}`
- ✅ แถวที่ 5: `{{SET_5}}`, `{{ACTUAL_5}}`, `{{ERROR_5}}`, `{{TOLERANCE_START_5}}`, `{{TOLERANCE_END_5}}`
- ✅ แถวที่ 6: `{{SET_6}}`, `{{ACTUAL_6}}`, `{{ERROR_6}}`, `{{TOLERANCE_START_6}}`, `{{TOLERANCE_END_6}}`

#### 2. **ข้อมูลเพิ่มเติม**
- ✅ `{{MODEL_PART_NUMBER}}` - รุ่น/หมายเลขชิ้นส่วน
- ✅ `{{DATE_OF_CALIBRATION}}` - วันที่สอบเทียบ
- ✅ `{{DESCRIPTION}}` - คำอธิบาย
- ✅ `{{DUE_DATE}}` - วันที่ครบกำหนด
- ✅ `{{SERIAL_NUMBER}}` - หมายเลขซีเรียล
- ✅ `{{RANGE}}` - ช่วงการวัด
- ✅ `{{MANUFACTURER}}` - ผู้ผลิต
- ✅ `{{CERTIFICATE_NO}}` - หมายเลขใบรับรอง

### 🔧 การเปลี่ยนแปลงในโค้ด

#### 1. **อัปเดต replacements dictionary**
```python
# ข้อมูลตารางผลการสอบเทียบ Pressure (6 แถว) - อัปเดตตามรูปแบบที่คุณต้องการ
# แถวที่ 1
'{{SET}}': cal.set or '-',
'{{ACTUAL}}': cal.actual or '-',
'{{ERROR}}': cal.error or '-',
'{{TOLERANCE_START}}': cal.tolerance_start or '-',
'{{TOLERANCE_END}}': cal.tolerance_end or '-',

# แถวที่ 2
'{{SET_2}}': cal.set_2 or '-',
'{{ACTUAL_2}}': cal.actual_2 or '-',
'{{ERROR_2}}': cal.error_2 or '-',
'{{TOLERANCE_START_2}}': cal.tolerance_start_2 or '-',
'{{TOLERANCE_END_2}}': cal.tolerance_end_2 or '-',

# ... และต่อไปเรื่อยๆ จนถึงแถวที่ 6
```

#### 2. **เพิ่มข้อมูลเพิ่มเติม**
```python
# ข้อมูลเพิ่มเติมสำหรับการแสดงผล
'{{MODEL_PART_NUMBER}}': f"{getattr(cal.uuc_id, 'model', '-')} / {getattr(cal.uuc_id, 'part_number', '-')}" if getattr(cal.uuc_id, 'part_number', None) else getattr(cal.uuc_id, 'model', '-'),
'{{DATE_OF_CALIBRATION}}': cal.update.strftime('%d/%m/%Y') if cal.update else '-',
'{{DESCRIPTION}}': getattr(cal.uuc_id, 'description', '-'),
'{{DUE_DATE}}': cal.next_due.strftime('%d/%m/%Y') if cal.next_due else '-',
'{{SERIAL_NUMBER}}': getattr(cal.uuc_id, 'serial_number', '-'),
'{{RANGE}}': getattr(cal, 'measurement_range', '-'),
'{{MANUFACTURER}}': getattr(cal.uuc_id, 'manufacturer', '-'),
'{{CERTIFICATE_NO}}': cal.certificate_number or '-',
```

#### 3. **เพิ่ม Debug Information**
```python
# Debug: แสดงข้อมูล tolerance
print(f"DEBUG: TOLERANCE_START: {getattr(cal, 'tolerance_start', None)}")
print(f"DEBUG: TOLERANCE_END: {getattr(cal, 'tolerance_end', None)}")
print(f"DEBUG: TOLERANCE_START_2: {getattr(cal, 'tolerance_start_2', None)}")
print(f"DEBUG: TOLERANCE_END_2: {getattr(cal, 'tolerance_end_2', None)}")

# Debug: แสดงข้อมูลที่ส่งไป template
print("DEBUG: === REPLACEMENTS SENT TO TEMPLATE ===")
for key, value in replacements.items():
    if 'SET' in key or 'TOLERANCE' in key or 'ACTUAL' in key or 'ERROR' in key:
        print(f"DEBUG: {key}: {value}")
print("DEBUG: === END REPLACEMENTS ===")
```

### 📋 รูปแบบข้อมูลที่ส่งออก

#### 1. **ตารางผลการสอบเทียบ**
```
{{SET}}    50.0    -    {{TOLERANCE_START}} - {{TOLERANCE_END}}
{{SET_2}}  100.0   -    {{TOLERANCE_START_2}} - {{TOLERANCE_END_2}}
{{SET_3}}  149.9   -0.1  {{TOLERANCE_START_3}} - {{TOLERANCE_END_3}}
{{SET_4}}  200.0   -    {{TOLERANCE_START_4}} - {{TOLERANCE_END_4}}
{{SET_5}}  250.0   -    {{TOLERANCE_START_5}} - {{TOLERANCE_END_5}}
{{SET_6}}  300.0   -    {{TOLERANCE_START_6}} - {{TOLERANCE_END_6}}
```

#### 2. **ข้อมูลเครื่องมือ**
```
Model / Part Number : {{MODEL_PART_NUMBER}}
Date of Calibration : {{DATE_OF_CALIBRATION}}
Description : {{DESCRIPTION}}
Due Date : {{DUE_DATE}}
Serial Number : {{SERIAL_NUMBER}}
Range : {{RANGE}}
Manufacturer : {{MANUFACTURER}}
Certificate No. : {{CERTIFICATE_NO}}
```

### 🎯 ฟิลด์ที่ใช้ใน Model

#### 1. **ข้อมูลหลัก**
- `cal.set` - ค่าตั้งต้น
- `cal.actual` - ค่าจริง
- `cal.error` - ค่าความคลาดเคลื่อน
- `cal.tolerance_start` - ค่าความคลาดเคลื่อนเริ่มต้น
- `cal.tolerance_end` - ค่าความคลาดเคลื่อนสิ้นสุด

#### 2. **ข้อมูลแถวเพิ่มเติม**
- `cal.set_2` ถึง `cal.set_6` - ค่าตั้งต้นแถวที่ 2-6
- `cal.actual_2` ถึง `cal.actual_6` - ค่าจริงแถวที่ 2-6
- `cal.error_2` ถึง `cal.error_6` - ค่าความคลาดเคลื่อนแถวที่ 2-6
- `cal.tolerance_start_2` ถึง `cal.tolerance_start_6` - ค่าความคลาดเคลื่อนเริ่มต้นแถวที่ 2-6
- `cal.tolerance_end_2` ถึง `cal.tolerance_end_6` - ค่าความคลาดเคลื่อนสิ้นสุดแถวที่ 2-6

#### 3. **ข้อมูลเครื่องมือ**
- `cal.uuc_id.model` - รุ่นเครื่องมือ
- `cal.uuc_id.part_number` - หมายเลขชิ้นส่วน
- `cal.uuc_id.description` - คำอธิบาย
- `cal.uuc_id.serial_number` - หมายเลขซีเรียล
- `cal.uuc_id.manufacturer` - ผู้ผลิต
- `cal.measurement_range` - ช่วงการวัด
- `cal.certificate_number` - หมายเลขใบรับรอง

### 🔍 การทดสอบ

#### 1. **ตรวจสอบข้อมูลที่ส่งออก**
- ดูใน console log ว่าข้อมูล tolerance ถูกส่งไปถูกต้องหรือไม่
- ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่

#### 2. **ทดสอบการส่งออก**
- สร้างการสอบเทียบ Pressure ใหม่
- กรอกข้อมูลครบถ้วน
- ทดสอบการส่งออกใบรับรอง

#### 3. **ตรวจสอบผลลัพธ์**
- เปิดไฟล์ Word ที่ส่งออก
- ตรวจสอบว่าข้อมูลแสดงครบถ้วนตามที่ต้องการ
- ตรวจสอบรูปแบบตาราง

### 📝 หมายเหตุ

- ระบบจะแสดงข้อมูล '-' หากไม่มีข้อมูล
- ข้อมูล tolerance จะแสดงเป็นรูปแบบ "start - end"
- ข้อมูลวันที่จะแสดงในรูปแบบ dd/mm/yyyy
- ข้อมูล tolerance ที่เป็น None จะแสดงเป็น '-'

### 🚀 ขั้นตอนต่อไป

1. **ทดสอบการส่งออก** - สร้างข้อมูลทดสอบและทดสอบการส่งออก
2. **ตรวจสอบ Template** - ตรวจสอบว่า template รับข้อมูลครบถ้วนหรือไม่
3. **ปรับแต่งเพิ่มเติม** - เพิ่มฟีเจอร์ตามความต้องการ
