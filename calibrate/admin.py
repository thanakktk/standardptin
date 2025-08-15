from django.contrib import admin
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque, UUC, UUCStdMap

@admin.register(CalibrationForce)
class CalibrationForceAdmin(admin.ModelAdmin):
    list_display = ("cal_force_id", "apply_com", "apply_ten", "compress", "tension", "fullscale", "error", "update", "uuc_id", "calibrator", "certificate_issuer")
    search_fields = ("cal_force_id",)
    exclude = ('uncer',)

@admin.register(CalibrationPressure)
class CalibrationPressureAdmin(admin.ModelAdmin):
    list_display = ("cal_pressure_id", "set", "m1", "m2", "m3", "m4", "avg", "error", "update", "uuc_id", "calibrator", "certificate_issuer")
    search_fields = ("cal_pressure_id",)
    exclude = ('uncer',)

@admin.register(CalibrationTorque)
class CalibrationTorqueAdmin(admin.ModelAdmin):
    list_display = ("cal_torque_id", "cwset", "cw0", "cw90", "cw180", "cw270", "cw_avg", "cw_error", "ccwset", "ccw0", "ccw90", "ccw180", "ccw270", "ccw_avg", "ccw_error", "update", "uuc_id", "calibrator", "certificate_issuer")
    search_fields = ("cal_torque_id",)
    exclude = ('cw_uncen', 'ccw_uncen',)

@admin.register(UUC)
class UUCAdmin(admin.ModelAdmin):
    list_display = ("name", "machine", "std")
    search_fields = ("name",)

@admin.register(UUCStdMap)
class UUCStdMapAdmin(admin.ModelAdmin):
    list_display = ("uuc", "std")
    search_fields = ("uuc", "std")
