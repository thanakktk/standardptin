from django.core.management.base import BaseCommand
from accounts.models import UserRole


class Command(BaseCommand):
    help = 'อัปเดตบทบาทเจ้าหน้าที่ช่างตามความต้องการใหม่'

    def handle(self, *args, **options):
        try:
            # หาบทบาทเจ้าหน้าที่ช่าง
            technician_role = UserRole.objects.get(name='technician')
            
            # อัปเดตสิทธิ์ตามความต้องการใหม่
            technician_role.description = 'เจ้าหน้าที่ช่าง - สามารถจัดการข้อมูลสอบเทียบและเครื่องมือได้'
            technician_role.can_add_machine = False  # ไม่สามารถเพิ่มเครื่องมือ
            technician_role.can_edit_machine = False  # ไม่สามารถแก้ไขเครื่องมือ
            technician_role.can_delete_machine = False  # ไม่สามารถลบเครื่องมือ
            technician_role.can_send_notification = False  # ไม่สามารถส่งแจ้งเตือน
            technician_role.can_add_calibration = True  # กดบันทึกการปรับเทียบได้
            technician_role.can_edit_calibration = True  # แก้ไขการสอบเทียบได้
            technician_role.can_delete_calibration = True  # กดลบได้
            technician_role.can_view_organization = False  # ไม่สามารถมองเห็นหน้าหน่วยงาน
            technician_role.can_manage_organization = False
            technician_role.can_view_users = False  # ไม่สามารถมองเห็นหน้าพนักงาน
            technician_role.can_manage_users = False
            technician_role.can_view_equipment = True  # เห็นทุกอย่างในเครื่องมือสอบเทียบ
            technician_role.can_manage_equipment = True
            technician_role.can_view_technical_docs = True  # เห็นทุกอย่างในเอกสารเทคนิค
            technician_role.can_manage_technical_docs = True
            technician_role.can_export_reports = True  # สามารถกด export word, excel ได้
            technician_role.can_edit_reports = False  # ไม่สามารถแก้ไขรายงาน
            technician_role.can_download_certificates = True  # สามารถดาวน์โหลดใบรับรองได้
            technician_role.can_change_priority = False  # เปลี่ยนระดับความเร่งด่วนไม่ได้
            technician_role.can_close_work = False  # ปิดงานไม่ได้
            technician_role.can_access_admin = False  # ไม่สามารถเข้าได้จัดการหลังบ้าน
            
            technician_role.save()
            
            self.stdout.write(
                self.style.SUCCESS('อัปเดตบทบาท "เจ้าหน้าที่ช่าง" เรียบร้อย')
            )
            
        except UserRole.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('ไม่พบบทบาท "เจ้าหน้าที่ช่าง" กรุณารัน setup_user_roles ก่อน')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'เกิดข้อผิดพลาด: {str(e)}')
            )
