# คู่มือการนำระบบสิทธิ์ไปใช้ในแต่ละหน้า

## สรุปสิ่งที่ต้องทำ

คุณต้องนำระบบสิทธิ์ไปใช้ในแต่ละหน้าเพื่อให้ทำงานได้จริง โดยมีขั้นตอนดังนี้:

### 1. ✅ Views ที่อัปเดตแล้ว

#### หน้าเครื่องมือ (Machine)
- ✅ `machine/views.py` - เพิ่ม permission checks
- ✅ `machine/templates/machine/list.html` - ซ่อน/แสดงปุ่มตามสิทธิ์

#### หน้าสอบเทียบ (Calibration)
- ✅ `calibrate/views.py` - เพิ่ม permission checks
- ✅ `calibrate/templates/calibrate/pressure_list.html` - ซ่อน/แสดงปุ่มตามสิทธิ์

#### หน้าหน่วยงาน (Organization)
- ✅ `organize/views.py` - เพิ่ม permission checks

#### หน้าผู้ใช้งาน (Employee)
- ✅ `employee/views.py` - เพิ่ม permission checks

#### หน้าเอกสารเทคนิค (Technical Docs)
- ✅ `technical_docs/views.py` - เพิ่ม permission checks

### 2. 🔄 Views ที่ยังต้องอัปเดต

#### หน้ารายงาน (Reports)
- ❌ `report/views.py` - ยังไม่ได้อัปเดต
- ❌ Templates - ยังไม่ได้อัปเดต

### 3. 📝 Templates ที่ยังต้องอัปเดต

#### หน้าหน่วยงาน
- ❌ `organize/templates/organize/list.html` - เพิ่ม permission checks
- ❌ `organize/templates/organize/form.html` - เพิ่ม permission checks

#### หน้าผู้ใช้งาน
- ❌ `employee/templates/employee/list.html` - เพิ่ม permission checks
- ❌ `employee/templates/employee/form.html` - เพิ่ม permission checks

#### หน้าเอกสารเทคนิค
- ❌ `technical_docs/templates/technical_docs/document_list.html` - เพิ่ม permission checks

## วิธีการอัปเดต Views

### 1. เพิ่ม Import
```python
from accounts.permissions import PermissionRequiredMixin as CustomPermissionRequiredMixin
from accounts.permissions import permission_required
```

### 2. อัปเดต Class-based Views
```python
# เปลี่ยนจาก
class MyListView(LoginRequiredMixin, ListView):

# เป็น
class MyListView(LoginRequiredMixin, CustomPermissionRequiredMixin, ListView):
    permission_required = 'view_feature'
```

### 3. อัปเดต Function-based Views
```python
# เพิ่ม decorator
@login_required
@permission_required('manage_feature')
def my_view(request):
    # view logic
```

## วิธีการอัปเดต Templates

### 1. ซ่อน/แสดงปุ่มตามสิทธิ์
```html
{% if user_permissions.can_add_machine %}
    <a href="{% url 'machine-add' %}" class="btn btn-success">
        เพิ่มเครื่องมือ
    </a>
{% endif %}
```

### 2. ซ่อน/แสดงเมนูตามสิทธิ์
```html
{% if user_permissions.can_view_organization %}
    <li class="nav-item">
        <a class="nav-link" href="{% url 'organize-list' %}">
            หน่วยงาน
        </a>
    </li>
{% endif %}
```

### 3. ซ่อน/แสดงฟอร์มตามสิทธิ์
```html
{% if user_permissions.can_manage_users %}
    <form method="post">
        <!-- ฟอร์มสำหรับจัดการผู้ใช้ -->
    </form>
{% endif %}
```

## สิทธิ์ที่ใช้ในแต่ละหน้า

### หน้าเครื่องมือ
- `view_machine` - ดูข้อมูลเครื่องมือ
- `add_machine` - เพิ่มเครื่องมือ
- `edit_machine` - แก้ไขเครื่องมือ
- `delete_machine` - ลบเครื่องมือ
- `send_notification` - ส่งแจ้งเตือน

### หน้าสอบเทียบ
- `view_calibration` - ดูข้อมูลสอบเทียบ
- `add_calibration` - เพิ่มข้อมูลสอบเทียบ
- `edit_calibration` - แก้ไขข้อมูลสอบเทียบ
- `delete_calibration` - ลบข้อมูลสอบเทียบ
- `change_priority` - เปลี่ยนระดับความเร่งด่วน
- `close_work` - ปิดงาน

### หน้าหน่วยงาน
- `view_organization` - ดูข้อมูลหน่วยงาน
- `manage_organization` - จัดการหน่วยงาน

### หน้าผู้ใช้งาน
- `view_users` - ดูข้อมูลผู้ใช้
- `manage_users` - จัดการผู้ใช้

### หน้าเครื่องมือสอบเทียบ
- `view_equipment` - ดูเครื่องมือสอบเทียบ
- `manage_equipment` - จัดการเครื่องมือสอบเทียบ

### หน้าเอกสารเทคนิค
- `view_technical_docs` - ดูเอกสารเทคนิค
- `manage_technical_docs` - จัดการเอกสารเทคนิค

### หน้ารายงาน
- `view_reports` - ดูรายงาน
- `export_reports` - ส่งออกรายงาน
- `edit_reports` - แก้ไขรายงาน
- `download_certificates` - ดาวน์โหลดใบรับรอง

## ขั้นตอนการทดสอบ

### 1. สร้างผู้ใช้ทดสอบ
```bash
python manage.py createsuperuser
```

### 2. กำหนดบทบาทให้ผู้ใช้
- เข้า Admin Panel → Users
- เลือกผู้ใช้ → กำหนด User Role

### 3. ทดสอบการเข้าถึง
- เข้าสู่ระบบด้วยผู้ใช้ที่กำหนดบทบาท
- ตรวจสอบว่าเห็นเฉพาะเมนูที่อนุญาต
- ทดสอบการเข้าถึงหน้าต่างๆ ตามสิทธิ์

### 4. ทดสอบฟีเจอร์เฉพาะ
- ตรวจสอบปุ่มต่างๆ ตามสิทธิ์
- ทดสอบการเพิ่ม/แก้ไข/ลบข้อมูล
- ตรวจสอบการส่งออกรายงาน

## หมายเหตุ

- ระบบสิทธิ์จะทำงานทันทีหลังจากอัปเดต Views และ Templates
- Superuser จะมีสิทธิ์เข้าถึงทุกฟีเจอร์โดยอัตโนมัติ
- การเปลี่ยนแปลงสิทธิ์จะมีผลทันทีหลังจากบันทึก
- ควรทดสอบทุกบทบาทเพื่อให้แน่ใจว่าระบบทำงานถูกต้อง
