# ระบบสิทธิ์ผู้ใช้งาน (User Permission System)

## สรุปการใช้งาน

ระบบสิทธิ์ผู้ใช้งานได้ถูกสร้างขึ้นเพื่อควบคุมการเข้าถึงฟีเจอร์ต่างๆ ตามบทบาทของผู้ใช้ โดยแบ่งเป็น 4 บทบาทหลัก:

### บทบาทผู้ใช้ (User Roles)

1. **หน่วยผู้ใช้ (Unit User)**
   - ดูข้อมูลเครื่องมือ ✅
   - ส่งคำร้องขอบันทึกสอบเทียบ ✅
   - กรองและค้นหาข้อมูล ✅
   - ไม่สามารถแก้ไข/ลบเครื่องมือ ❌
   - ไม่สามารถส่งแจ้งเตือน ❌
   - ไม่สามารถเพิ่มเครื่องมือ ❌
   - ดูข้อมูลสอบเทียบ ✅
   - ส่งออกรายงาน ✅
   - ไม่สามารถแก้ไขรายงาน ❌
   - ไม่สามารถดาวน์โหลดใบรับรอง ❌
   - ไม่สามารถเข้าหลังบ้าน ❌

2. **ผู้ดูแลระบบ (Admin)**
   - เข้าถึงทุกฟีเจอร์ ✅
   - จัดการผู้ใช้ ✅
   - จัดการหน่วยงาน ✅
   - เข้าหลังบ้าน ✅

3. **ช่างเทคนิค (Technician)**
   - จัดการข้อมูลสอบเทียบ ✅
   - จัดการเครื่องมือสอบเทียบ ✅
   - จัดการเอกสารเทคนิค ✅
   - ดาวน์โหลดใบรับรอง ✅
   - ไม่สามารถเข้าหลังบ้าน ❌

4. **ผู้ดูข้อมูล (Viewer)**
   - ดูข้อมูลได้เท่านั้น ✅
   - ไม่สามารถแก้ไข/เพิ่ม/ลบ ❌

## ไฟล์ที่สร้าง/แก้ไข

### 1. Models
- `accounts/models.py` - เพิ่ม UserRole model และ permission methods
- `accounts/migrations/0003_userrole_user_user_role.py` - Migration สำหรับ UserRole

### 2. Permissions
- `accounts/permissions.py` - Decorators และ Mixins สำหรับตรวจสอบสิทธิ์
- `accounts/context_processors.py` - Context processor สำหรับใช้ใน templates

### 3. Admin
- `accounts/admin.py` - เพิ่ม UserRoleAdmin
- `accounts/management/commands/setup_user_roles.py` - Command สำหรับสร้างบทบาทเริ่มต้น

### 4. Views (Updated with Permissions)
- `machine/views.py` - เพิ่ม permission checks
- `calibrate/views.py` - เพิ่ม permission checks

### 5. Templates (Updated with Permission Checks)
- `templates/base.html` - Navigation menu ตามสิทธิ์
- `machine/templates/machine/list.html` - ปุ่มต่างๆ ตามสิทธิ์
- `calibrate/templates/calibrate/pressure_list.html` - ปุ่มต่างๆ ตามสิทธิ์

### 6. Settings
- `projest/settings.py` - เพิ่ม context processor

## การใช้งาน

### 1. สร้างบทบาทเริ่มต้น
```bash
python manage.py setup_user_roles
```

### 2. กำหนดบทบาทให้ผู้ใช้
- เข้า Admin Panel
- ไปที่ Users
- เลือกผู้ใช้ที่ต้องการ
- กำหนด User Role

### 3. ตรวจสอบสิทธิ์ใน Template
```html
{% if user_permissions.can_view_machine %}
    <!-- แสดงเนื้อหาสำหรับผู้ที่ดูเครื่องมือได้ -->
{% endif %}
```

### 4. ตรวจสอบสิทธิ์ใน View
```python
from accounts.permissions import PermissionRequiredMixin

class MyView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'view_machine'
```

## สิทธิ์ที่ควบคุม

### เครื่องมือวัด (Machine)
- `can_view_machine` - ดูข้อมูลเครื่องมือ
- `can_add_machine` - เพิ่มเครื่องมือ
- `can_edit_machine` - แก้ไขเครื่องมือ
- `can_delete_machine` - ลบเครื่องมือ
- `can_send_notification` - ส่งแจ้งเตือน

### สอบเทียบ (Calibration)
- `can_view_calibration` - ดูข้อมูลสอบเทียบ
- `can_add_calibration` - เพิ่มข้อมูลสอบเทียบ
- `can_edit_calibration` - แก้ไขข้อมูลสอบเทียบ
- `can_delete_calibration` - ลบข้อมูลสอบเทียบ

### หน่วยงาน (Organization)
- `can_view_organization` - ดูข้อมูลหน่วยงาน
- `can_manage_organization` - จัดการหน่วยงาน

### ผู้ใช้ (Users)
- `can_view_users` - ดูข้อมูลผู้ใช้
- `can_manage_users` - จัดการผู้ใช้

### เครื่องมือสอบเทียบ (Equipment)
- `can_view_equipment` - ดูเครื่องมือสอบเทียบ
- `can_manage_equipment` - จัดการเครื่องมือสอบเทียบ

### เอกสารเทคนิค (Technical Docs)
- `can_view_technical_docs` - ดูเอกสารเทคนิค
- `can_manage_technical_docs` - จัดการเอกสารเทคนิค

### รายงาน (Reports)
- `can_view_reports` - ดูรายงาน
- `can_export_reports` - ส่งออกรายงาน
- `can_edit_reports` - แก้ไขรายงาน
- `can_download_certificates` - ดาวน์โหลดใบรับรอง

### ระบบ (System)
- `can_access_admin` - เข้าถึงหลังบ้าน

## การทดสอบ

1. สร้างผู้ใช้ใหม่
2. กำหนดบทบาท "หน่วยผู้ใช้"
3. เข้าสู่ระบบด้วยผู้ใช้ใหม่
4. ตรวจสอบว่าเห็นเฉพาะเมนูและปุ่มที่อนุญาต
5. ทดสอบการเข้าถึงหน้าต่างๆ ตามสิทธิ์

## หมายเหตุ

- Superuser จะมีสิทธิ์เข้าถึงทุกฟีเจอร์โดยอัตโนมัติ
- ระบบจะตรวจสอบสิทธิ์ทั้งใน View และ Template
- การเปลี่ยนแปลงสิทธิ์จะมีผลทันทีหลังจากบันทึก
