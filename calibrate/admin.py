from django.contrib import admin
from .models import CalibrationForce, CalibrationPressure, CalibrationTorque, UUC, UUCStdMap, DialGaugeCalibration, DialGaugeReading, BalanceCalibration, BalanceReading, MicrowaveCalibration, MicrowaveReading

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

@admin.register(DialGaugeCalibration)
class DialGaugeCalibrationAdmin(admin.ModelAdmin):
    list_display = ("machine", "date_calibration", "status", "priority", "calibrator", "certificate_issuer")
    search_fields = ("machine__name", "machine__model", "machine__serial_number")
    list_filter = ("status", "priority", "date_calibration")
    date_hierarchy = "date_calibration"

@admin.register(DialGaugeReading)
class DialGaugeReadingAdmin(admin.ModelAdmin):
    list_display = ("calibration", "uuc_set", "average_up", "average_down", "error", "uncertainty")
    search_fields = ("calibration__machine__name", "calibration__machine__model")
    list_filter = ("calibration__date_calibration",)

@admin.register(BalanceCalibration)
class BalanceCalibrationAdmin(admin.ModelAdmin):
    list_display = ("machine", "date_calibration", "status", "priority", "calibrator", "certificate_issuer", "unit")
    search_fields = ("machine__name", "machine__model", "machine__serial_number")
    list_filter = ("status", "priority", "date_calibration", "unit")
    date_hierarchy = "date_calibration"

@admin.register(BalanceReading)
class BalanceReadingAdmin(admin.ModelAdmin):
    list_display = ("calibration", "uuc_set", "average", "standard_deviation", "uncertainty")
    search_fields = ("calibration__machine__name", "calibration__machine__model")
    list_filter = ("calibration__date_calibration",)

@admin.register(MicrowaveCalibration)
class MicrowaveCalibrationAdmin(admin.ModelAdmin):
    list_display = ("machine", "date_calibration", "certificate_number", "status", "priority", "calibrator", "certificate_issuer")
    search_fields = ("machine__name", "machine__model", "machine__serial_number", "certificate_number")
    list_filter = ("status", "priority", "date_calibration")
    date_hierarchy = "date_calibration"

@admin.register(MicrowaveReading)
class MicrowaveReadingAdmin(admin.ModelAdmin):
    list_display = ("calibration", "test_type", "function_test", "nominal_value", "measured_value", "unit", "test_result")
    search_fields = ("calibration__machine__name", "calibration__machine__model", "function_test", "nominal_value")
    list_filter = ("test_type", "test_result", "calibration__date_calibration")
