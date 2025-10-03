# Generated manually to update Torque calibration default status

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calibrate', '0009_alter_calibrationforce_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calibrationtorque',
            name='status',
            field=models.CharField(choices=[('pending', 'รอสอบเทียบ'), ('in_progress', 'กำลังสอบเทียบ'), ('passed', 'ผ่านการสอบเทียบ'), ('cert_issued', 'ออกใบรับรอง'), ('failed', 'ไม่ผ่านการสอบเทียบ'), ('closed', 'ปิดงาน')], default='pending', max_length=20, verbose_name='สถานะปรับเเทียบ'),
        ),
    ]
