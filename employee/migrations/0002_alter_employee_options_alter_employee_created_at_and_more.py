# Generated by Django 5.2.4 on 2025-07-12 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('organize', '0002_alter_organize_options_alter_organize_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'พนักงาน', 'verbose_name_plural': 'พนักงาน'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='วันที่สร้าง'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='อีเมล'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ชื่อพนักงาน'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='organize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organize.organize', verbose_name='หน่วยงาน'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='เบอร์โทรศัพท์'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ตำแหน่ง'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='วันที่แก้ไขล่าสุด'),
        ),
    ]
