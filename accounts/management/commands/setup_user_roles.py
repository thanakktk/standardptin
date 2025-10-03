from django.core.management.base import BaseCommand
from accounts.models import UserRole


class Command(BaseCommand):
    help = 'สร้างบทบาทผู้ใช้เริ่มต้น'

    def handle(self, *args, **options):
        # สร้างบทบาทหน่วยผู้ใช้
        unit_user_role, created = UserRole.objects.get_or_create(
            name='unit_user',
            defaults={
                'description': 'ผู้ใช้หน่วยงาน - สามารถดูข้อมูลและส่งคำร้องขอได้',
                'can_view_machine': True,
                'can_add_machine': False,
                'can_edit_machine': False,
                'can_delete_machine': False,
                'can_send_notification': False,
                'can_view_calibration': True,
                'can_add_calibration': False,
                'can_edit_calibration': False,
                'can_delete_calibration': False,
                'can_view_organization': False,
                'can_manage_organization': False,
                'can_view_users': False,
                'can_manage_users': False,
                'can_view_equipment': False,
                'can_manage_equipment': False,
                'can_view_technical_docs': False,
                'can_manage_technical_docs': False,
                'can_view_reports': True,
                'can_export_reports': True,
                'can_edit_reports': False,
                'can_download_certificates': False,
                'can_access_admin': False,
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('สร้างบทบาท "หน่วยผู้ใช้" เรียบร้อย')
            )
        else:
            self.stdout.write('บทบาท "หน่วยผู้ใช้" มีอยู่แล้ว')

        # สร้างบทบาทผู้ดูแลระบบ
        admin_role, created = UserRole.objects.get_or_create(
            name='admin',
            defaults={
                'description': 'ผู้ดูแลระบบ - มีสิทธิ์เข้าถึงทุกฟีเจอร์',
                'can_view_machine': True,
                'can_add_machine': True,
                'can_edit_machine': True,
                'can_delete_machine': True,
                'can_send_notification': True,
                'can_view_calibration': True,
                'can_add_calibration': True,
                'can_edit_calibration': True,
                'can_delete_calibration': True,
                'can_view_organization': True,
                'can_manage_organization': True,
                'can_view_users': True,
                'can_manage_users': True,
                'can_view_equipment': True,
                'can_manage_equipment': True,
                'can_view_technical_docs': True,
                'can_manage_technical_docs': True,
                'can_view_reports': True,
                'can_export_reports': True,
                'can_edit_reports': True,
                'can_download_certificates': True,
                'can_access_admin': True,
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('สร้างบทบาท "ผู้ดูแลระบบ" เรียบร้อย')
            )
        else:
            self.stdout.write('บทบาท "ผู้ดูแลระบบ" มีอยู่แล้ว')

        # สร้างบทบาทเจ้าหน้าที่ช่าง
        technician_role, created = UserRole.objects.get_or_create(
            name='technician',
            defaults={
                'description': 'เจ้าหน้าที่ช่าง - สามารถจัดการข้อมูลสอบเทียบและเครื่องมือได้',
                'can_view_machine': True,
                'can_add_machine': False,  # ไม่สามารถเพิ่มเครื่องมือ
                'can_edit_machine': False,  # ไม่สามารถแก้ไขเครื่องมือ
                'can_delete_machine': False,  # ไม่สามารถลบเครื่องมือ
                'can_send_notification': False,  # ไม่สามารถส่งแจ้งเตือน
                'can_view_calibration': True,
                'can_add_calibration': True,  # กดบันทึกการปรับเทียบได้
                'can_edit_calibration': True,  # แก้ไขการสอบเทียบได้
                'can_delete_calibration': True,  # กดลบได้
                'can_view_organization': False,  # ไม่สามารถมองเห็นหน้าหน่วยงาน
                'can_manage_organization': False,
                'can_view_users': False,  # ไม่สามารถมองเห็นหน้าพนักงาน
                'can_manage_users': False,
                'can_view_equipment': True,  # เห็นทุกอย่างในเครื่องมือสอบเทียบ
                'can_manage_equipment': True,
                'can_view_technical_docs': True,  # เห็นทุกอย่างในเอกสารเทคนิค
                'can_manage_technical_docs': True,
                'can_view_reports': True,
                'can_export_reports': True,  # สามารถกด export word, excel ได้
                'can_edit_reports': False,  # ไม่สามารถแก้ไขรายงาน
                'can_download_certificates': True,  # สามารถดาวน์โหลดใบรับรองได้
                'can_change_priority': False,  # เปลี่ยนระดับความเร่งด่วนไม่ได้
                'can_close_work': False,  # ปิดงานไม่ได้
                'can_access_admin': False,  # ไม่สามารถเข้าได้จัดการหลังบ้าน
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('สร้างบทบาท "ช่างเทคนิค" เรียบร้อย')
            )
        else:
            self.stdout.write('บทบาท "ช่างเทคนิค" มีอยู่แล้ว')

        # สร้างบทบาทเจ้าหน้าที่แผนกจัดดำเนินงาน
        coordinator_role, created = UserRole.objects.get_or_create(
            name='coordinator',
            defaults={
                'description': 'เจ้าหน้าที่แผนกจัดดำเนินงาน - มีสิทธิ์เข้าถึงทุกฟีเจอร์ยกเว้นหลังบ้าน',
                'can_view_machine': True,  # เห็นทุกอย่างในหน้าเครื่องมือ
                'can_add_machine': True,
                'can_edit_machine': True,
                'can_delete_machine': True,
                'can_send_notification': True,
                'can_view_calibration': True,  # เห็นทุกอย่างในหน้าปรับเทียบ
                'can_add_calibration': True,
                'can_edit_calibration': True,
                'can_delete_calibration': True,
                'can_view_organization': True,  # เห็นทุกอย่างในหน้าหน่วยงาน
                'can_manage_organization': True,
                'can_view_users': True,  # เห็นทุกอย่างในหน้าพนักงาน
                'can_manage_users': True,
                'can_view_equipment': True,  # เห็นทุกอย่างในเครื่องมือสอบเทียบ
                'can_manage_equipment': True,
                'can_view_technical_docs': True,  # เห็นทุกอย่างในเอกสารเทคนิค
                'can_manage_technical_docs': True,
                'can_view_reports': True,
                'can_export_reports': True,  # สามารถกด export word, excel ได้
                'can_edit_reports': True,
                'can_download_certificates': True,  # สามารถดาวน์โหลดใบรับรองได้
                'can_change_priority': True,
                'can_close_work': True,
                'can_access_admin': False,  # ไม่สามารถเข้าได้จัดการหลังบ้าน
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('สร้างบทบาท "เจ้าหน้าที่แผนกจัดดำเนินงาน" เรียบร้อย')
            )
        else:
            self.stdout.write('บทบาท "เจ้าหน้าที่แผนกจัดดำเนินงาน" มีอยู่แล้ว')

        # สร้างบทบาทผู้ดูข้อมูล
        viewer_role, created = UserRole.objects.get_or_create(
            name='viewer',
            defaults={
                'description': 'ผู้ดูข้อมูล - สามารถดูข้อมูลได้เท่านั้น',
                'can_view_machine': True,
                'can_add_machine': False,
                'can_edit_machine': False,
                'can_delete_machine': False,
                'can_send_notification': False,
                'can_view_calibration': True,
                'can_add_calibration': False,
                'can_edit_calibration': False,
                'can_delete_calibration': False,
                'can_view_organization': False,
                'can_manage_organization': False,
                'can_view_users': False,
                'can_manage_users': False,
                'can_view_equipment': False,
                'can_manage_equipment': False,
                'can_view_technical_docs': False,
                'can_manage_technical_docs': False,
                'can_view_reports': True,
                'can_export_reports': False,
                'can_edit_reports': False,
                'can_download_certificates': False,
                'can_access_admin': False,
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS('สร้างบทบาท "ผู้ดูข้อมูล" เรียบร้อย')
            )
        else:
            self.stdout.write('บทบาท "ผู้ดูข้อมูล" มีอยู่แล้ว')

        self.stdout.write(
            self.style.SUCCESS('การตั้งค่าบทบาทผู้ใช้เสร็จสิ้น')
        )
