# บทบาทเจ้าหน้าที่แผนกจัดดำเนินงาน (Coordinator Role)

## สรุปการใช้งาน

บทบาทเจ้าหน้าที่แผนกจัดดำเนินงานได้ถูกสร้างขึ้นใหม่ โดยมีสิทธิ์เข้าถึงทุกฟีเจอร์ยกเว้นการเข้าหลังบ้าน:

### 🎯 สิทธิ์การใช้งานสำหรับเจ้าหน้าที่แผนกจัดดำเนินงาน

#### หน้าเครื่องมือ
- ✅ **เห็นทุกอย่าง** - ดู, เพิ่ม, แก้ไข, ลบ, ส่งแจ้งเตือน

#### หน้าปรับเทียบ
- ✅ **เห็นทุกอย่าง** - ดู, เพิ่ม, แก้ไข, ลบ, เปลี่ยนระดับความเร่งด่วน, ปิดงาน

#### หน้าหน่วยงาน
- ✅ **เห็นทุกอย่าง** - ดูและจัดการหน่วยงาน

#### หน้าพนักงาน
- ✅ **เห็นทุกอย่าง** - ดูและจัดการผู้ใช้

#### หน้าเครื่องมือที่ใช้สอบเทียบ
- ✅ **เห็นทุกอย่าง** - ดูและจัดการเครื่องมือสอบเทียบ

#### เอกสารเทคนิค
- ✅ **เห็นทุกอย่าง** - ดูและจัดการเอกสารเทคนิค

#### รายงานผลปรับเทียบ
- ✅ **สามารถกด export word, excel ได้**
- ✅ **สามารถดาวน์โหลดใบรับรองได้**

#### จัดการหลังบ้าน
- ❌ **ไม่สามารถเข้าได้**

## ไฟล์ที่สร้าง/แก้ไข

### 1. Models
- `accounts/models.py` - เพิ่มบทบาท 'coordinator' และ method `is_coordinator()`
- `accounts/migrations/0005_alter_userrole_name.py` - Migration สำหรับบทบาทใหม่

### 2. Permissions
- `accounts/context_processors.py` - เพิ่ม `is_coordinator` ใน context processor

### 3. Commands
- `accounts/management/commands/setup_user_roles.py` - เพิ่มการสร้างบทบาท coordinator

## การใช้งาน

### 1. สร้างบทบาทเริ่มต้น
```bash
python manage.py setup_user_roles
```

### 2. กำหนดบทบาทให้ผู้ใช้
- เข้า Admin Panel → Users
- เลือกผู้ใช้ที่ต้องการ
- กำหนด User Role เป็น "เจ้าหน้าที่แผนกจัดดำเนินงาน"

### 3. ตรวจสอบสิทธิ์ใน Template
```html
{% if user_permissions.can_view_machine %}
    <!-- แสดงเนื้อหาสำหรับผู้ที่ดูเครื่องมือได้ -->
{% endif %}

{% if is_coordinator %}
    <!-- แสดงเนื้อหาสำหรับเจ้าหน้าที่แผนกจัดดำเนินงาน -->
{% endif %}
```

### 4. ตรวจสอบสิทธิ์ใน View
```python
from accounts.permissions import PermissionRequiredMixin

class MyView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'view_machine'
```

## สิทธิ์ที่ได้รับ

### เครื่องมือวัด (Machine) - ทุกสิทธิ์
- `can_view_machine` ✅
- `can_add_machine` ✅
- `can_edit_machine` ✅
- `can_delete_machine` ✅
- `can_send_notification` ✅

### สอบเทียบ (Calibration) - ทุกสิทธิ์
- `can_view_calibration` ✅
- `can_add_calibration` ✅
- `can_edit_calibration` ✅
- `can_delete_calibration` ✅

### หน่วยงาน (Organization) - ทุกสิทธิ์
- `can_view_organization` ✅
- `can_manage_organization` ✅

### ผู้ใช้ (Users) - ทุกสิทธิ์
- `can_view_users` ✅
- `can_manage_users` ✅

### เครื่องมือสอบเทียบ (Equipment) - ทุกสิทธิ์
- `can_view_equipment` ✅
- `can_manage_equipment` ✅

### เอกสารเทคนิค (Technical Docs) - ทุกสิทธิ์
- `can_view_technical_docs` ✅
- `can_manage_technical_docs` ✅

### รายงาน (Reports) - ทุกสิทธิ์
- `can_view_reports` ✅
- `can_export_reports` ✅
- `can_edit_reports` ✅
- `can_download_certificates` ✅

### สิทธิ์เพิ่มเติม - ทุกสิทธิ์
- `can_change_priority` ✅
- `can_close_work` ✅

### ระบบ (System) - จำกัดสิทธิ์
- `can_access_admin` ❌ (ไม่สามารถเข้าหลังบ้าน)

## การทดสอบ

1. **สร้างผู้ใช้ใหม่**
   - เข้า Admin Panel → Users → Add User
   - กำหนด User Role เป็น "เจ้าหน้าที่แผนกจัดดำเนินงาน"

2. **ทดสอบการเข้าถึง**
   - เข้าสู่ระบบด้วยผู้ใช้ใหม่
   - ตรวจสอบว่าเห็นทุกเมนูยกเว้น "จัดการระบบ"
   - ทดสอบการเข้าถึงหน้าต่างๆ ตามสิทธิ์

3. **ทดสอบฟีเจอร์เฉพาะ**
   - ตรวจสอบว่าสามารถเพิ่ม/แก้ไข/ลบเครื่องมือได้
   - ตรวจสอบว่าสามารถจัดการข้อมูลสอบเทียบได้
   - ตรวจสอบว่าสามารถจัดการหน่วยงานและผู้ใช้ได้
   - ตรวจสอบว่าสามารถส่งออกรายงานและดาวน์โหลดใบรับรองได้
   - ตรวจสอบว่าไม่สามารถเข้าหลังบ้านได้

## หมายเหตุ

- บทบาทเจ้าหน้าที่แผนกจัดดำเนินงานจะมีสิทธิ์เข้าถึงเกือบทุกฟีเจอร์
- ไม่สามารถเข้าถึงการจัดการระบบ (Admin Panel) ได้
- เหมาะสำหรับผู้ที่ต้องจัดการและควบคุมระบบในระดับสูง
- สามารถเปลี่ยนระดับความเร่งด่วนและปิดงานได้
