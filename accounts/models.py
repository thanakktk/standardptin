from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission

class User(AbstractUser):
    # ข้อมูลพื้นฐาน
    username = models.CharField(max_length=150, unique=True, verbose_name="ชื่อผู้ใช้")
    email = models.EmailField(verbose_name="อีเมล")
    
    # คำนำหน้า
    prefix = models.CharField(max_length=20, blank=True, null=True, verbose_name="คำนำหน้า")
    
    # ชื่อภาษาไทย
    first_name_th = models.CharField(max_length=100, blank=True, null=True, verbose_name="ชื่อ (ไทย)")
    last_name_th = models.CharField(max_length=100, blank=True, null=True, verbose_name="นามสกุล (ไทย)")
    
    # ชื่อภาษาอังกฤษ
    first_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name="ชื่อ (อังกฤษ)")
    last_name_en = models.CharField(max_length=100, blank=True, null=True, verbose_name="นามสกุล (อังกฤษ)")
    
    # เบอร์โทรศัพท์
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="เบอร์โทรศัพท์")
    phone_extension = models.CharField(max_length=5, blank=True, null=True, verbose_name="เบอร์โทรศัพท์ 5 หลัก")
    
    # หน่วยงาน
    organize = models.ForeignKey('organize.Organize', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="หน่วยงาน")
    
    # ข้อมูลอื่นๆ
    level = models.CharField(max_length=50, blank=True, null=True, verbose_name="ระดับ")
    
    # บทบาทผู้ใช้
    user_role = models.ForeignKey('UserRole', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="บทบาทผู้ใช้")
    
    # ข้อมูลเวลา
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข", null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "ผู้ใช้งาน"
        verbose_name_plural = "ผู้ใช้งาน"
        ordering = ['username']

    def get_full_name_th(self):
        """ดึงชื่อเต็มภาษาไทย"""
        if self.first_name_th and self.last_name_th:
            return f"{self.first_name_th} {self.last_name_th}"
        return self.username

    def get_full_name_en(self):
        """ดึงชื่อเต็มภาษาอังกฤษ"""
        if self.first_name_en and self.last_name_en:
            return f"{self.first_name_en} {self.last_name_en}"
        return self.username

    def get_display_name(self):
        """ดึงชื่อที่แสดง (ไทยก่อน, อังกฤษถ้าไม่มีไทย)"""
        if self.first_name_th and self.last_name_th:
            return self.get_full_name_th()
        elif self.first_name_en and self.last_name_en:
            return self.get_full_name_en()
        return self.username

    def has_permission(self, permission_code):
        """ตรวจสอบสิทธิ์การใช้งาน"""
        if self.is_superuser:
            return True
        
        # ตรวจสอบสิทธิ์จาก groups
        for group in self.groups.all():
            if group.permissions.filter(codename=permission_code).exists():
                return True
        
        # ตรวจสอบสิทธิ์โดยตรง
        if self.user_permissions.filter(codename=permission_code).exists():
            return True
        
        return False

    def is_unit_user(self):
        """ตรวจสอบว่าเป็นผู้ใช้หน่วยงานหรือไม่"""
        if self.is_superuser:
            return True
        if self.user_role and self.user_role.name == 'unit_user':
            return True
        return self.has_permission('unit_user') or self.groups.filter(name='หน่วยผู้ใช้').exists()

    def is_admin_user(self):
        """ตรวจสอบว่าเป็นผู้ดูแลระบบหรือไม่"""
        if self.is_superuser:
            return True
        if self.user_role and self.user_role.name == 'admin':
            return True
        return self.groups.filter(name='ผู้ดูแลระบบ').exists()

    def is_technician(self):
        """ตรวจสอบว่าเป็นช่างเทคนิคหรือไม่"""
        if self.is_superuser:
            return True
        if self.user_role and self.user_role.name == 'technician':
            return True
        return self.has_permission('technician') or self.groups.filter(name='ช่างเทคนิค').exists()

    def is_coordinator(self):
        """ตรวจสอบว่าเป็นเจ้าหน้าที่แผนกจัดดำเนินงานหรือไม่"""
        if self.is_superuser:
            return True
        if self.user_role and self.user_role.name == 'coordinator':
            return True
        return self.has_permission('coordinator') or self.groups.filter(name='เจ้าหน้าที่แผนกจัดดำเนินงาน').exists()

    def can_access_feature(self, feature):
        """ตรวจสอบสิทธิ์การเข้าถึงฟีเจอร์ต่างๆ"""
        if self.is_superuser:
            return True
        
        if not self.user_role:
            return False
        
        # ตรวจสอบสิทธิ์ตามฟีเจอร์
        permission_map = {
            'view_machine': 'can_view_machine',
            'add_machine': 'can_add_machine',
            'edit_machine': 'can_edit_machine',
            'delete_machine': 'can_delete_machine',
            'send_notification': 'can_send_notification',
            'view_calibration': 'can_view_calibration',
            'add_calibration': 'can_add_calibration',
            'edit_calibration': 'can_edit_calibration',
            'delete_calibration': 'can_delete_calibration',
            'view_organization': 'can_view_organization',
            'manage_organization': 'can_manage_organization',
            'view_users': 'can_view_users',
            'manage_users': 'can_manage_users',
            'view_equipment': 'can_view_equipment',
            'manage_equipment': 'can_manage_equipment',
            'view_technical_docs': 'can_view_technical_docs',
            'manage_technical_docs': 'can_manage_technical_docs',
            'view_reports': 'can_view_reports',
            'export_reports': 'can_export_reports',
            'edit_reports': 'can_edit_reports',
            'download_certificates': 'can_download_certificates',
            'change_priority': 'can_change_priority',
            'close_work': 'can_close_work',
            'access_admin': 'can_access_admin',
        }
        
        if feature in permission_map:
            return getattr(self.user_role, permission_map[feature], False)
        
        return False


class UserRole(models.Model):
    """โมเดลสำหรับจัดการสิทธิ์ผู้ใช้งาน"""
    ROLE_CHOICES = [
        ('unit_user', 'หน่วยผู้ใช้'),
        ('admin', 'ผู้ดูแลระบบ'),
        ('technician', 'ช่างเทคนิค'),
        ('coordinator', 'เจ้าหน้าที่แผนกจัดดำเนินงาน'),
        ('viewer', 'ผู้ดูข้อมูล'),
    ]
    
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True, verbose_name="ชื่อบทบาท")
    description = models.TextField(blank=True, verbose_name="คำอธิบาย")
    
    # สิทธิ์การใช้งาน
    can_view_machine = models.BooleanField(default=True, verbose_name="ดูข้อมูลเครื่องมือ")
    can_add_machine = models.BooleanField(default=False, verbose_name="เพิ่มเครื่องมือ")
    can_edit_machine = models.BooleanField(default=False, verbose_name="แก้ไขเครื่องมือ")
    can_delete_machine = models.BooleanField(default=False, verbose_name="ลบเครื่องมือ")
    can_send_notification = models.BooleanField(default=False, verbose_name="ส่งแจ้งเตือน")
    
    can_view_calibration = models.BooleanField(default=True, verbose_name="ดูข้อมูลสอบเทียบ")
    can_add_calibration = models.BooleanField(default=False, verbose_name="เพิ่มข้อมูลสอบเทียบ")
    can_edit_calibration = models.BooleanField(default=False, verbose_name="แก้ไขข้อมูลสอบเทียบ")
    can_delete_calibration = models.BooleanField(default=False, verbose_name="ลบข้อมูลสอบเทียบ")
    
    can_view_organization = models.BooleanField(default=False, verbose_name="ดูข้อมูลหน่วยงาน")
    can_manage_organization = models.BooleanField(default=False, verbose_name="จัดการหน่วยงาน")
    
    can_view_users = models.BooleanField(default=False, verbose_name="ดูข้อมูลผู้ใช้")
    can_manage_users = models.BooleanField(default=False, verbose_name="จัดการผู้ใช้")
    
    can_view_equipment = models.BooleanField(default=False, verbose_name="ดูเครื่องมือสอบเทียบ")
    can_manage_equipment = models.BooleanField(default=False, verbose_name="จัดการเครื่องมือสอบเทียบ")
    
    can_view_technical_docs = models.BooleanField(default=False, verbose_name="ดูเอกสารเทคนิค")
    can_manage_technical_docs = models.BooleanField(default=False, verbose_name="จัดการเอกสารเทคนิค")
    
    can_view_reports = models.BooleanField(default=True, verbose_name="ดูรายงาน")
    can_export_reports = models.BooleanField(default=True, verbose_name="ส่งออกรายงาน")
    can_edit_reports = models.BooleanField(default=False, verbose_name="แก้ไขรายงาน")
    can_download_certificates = models.BooleanField(default=False, verbose_name="ดาวน์โหลดใบรับรอง")
    
    # สิทธิ์เพิ่มเติมสำหรับเจ้าหน้าที่ช่าง
    can_change_priority = models.BooleanField(default=False, verbose_name="เปลี่ยนระดับความเร่งด่วน")
    can_close_work = models.BooleanField(default=False, verbose_name="ปิดงาน")
    
    can_access_admin = models.BooleanField(default=False, verbose_name="เข้าถึงหลังบ้าน")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่แก้ไข")
    
    class Meta:
        verbose_name = "บทบาทผู้ใช้"
        verbose_name_plural = "บทบาทผู้ใช้"
        ordering = ['name']
    
    def __str__(self):
        return self.get_name_display()
