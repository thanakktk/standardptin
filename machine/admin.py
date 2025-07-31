from django.contrib import admin
from .models import Machine, MachineType, MachineUnit, Manufacture, CalibrationEquipment

@admin.register(MachineType)
class MachineTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(MachineUnit)
class MachineUnitAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(CalibrationEquipment)
class CalibrationEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'machine_type', 'certificate', 'created_at')
    list_filter = ('machine_type', 'created_at')
    search_fields = ('name', 'model', 'serial_number')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'serial_number', 'organize', 'machine_type', 'manufacture', 'deleted')
    list_filter = ('machine_type', 'organize', 'manufacture', 'deleted', 'update')
    search_fields = ('name', 'model', 'serial_number')
    readonly_fields = ('update',)
    fieldsets = (
        ('ข้อมูลพื้นฐาน', {
            'fields': ('name', 'model', 'serial_number', 'organize', 'machine_type')
        }),
        ('ข้อมูลเทคนิค', {
            'fields': ('range', 'res_uuc', 'unit', 'manufacture')
        }),
        ('การสอบเทียบ', {
            'fields': ('calibration_equipment',)
        }),
        ('สถานะ', {
            'fields': ('deleted', 'update')
        }),
    )
