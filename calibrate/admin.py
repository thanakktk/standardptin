from django.contrib import admin

from .models import CalibrationPressure, CalibrationTorque, UUC, UUCStdMap, DialGaugeCalibration, DialGaugeReading, BalanceCalibration, BalanceReading, MicrowaveCalibration, MicrowaveReading, LowFrequencyCalibration, HighFrequencyCalibration




@admin.register(CalibrationPressure)
class CalibrationPressureAdmin(admin.ModelAdmin):
    list_display = (
        'cal_pressure_id',
        'set',
        'm1',
        'm2',
        'm3',
        'm4',
        'avg',
        'error',
        'uncer',
        'tolerance_start',
        'tolerance_end',
        'update',
        'next_due',
        'status',
        'priority',
        'uuc_id',
        'std_id',
        'calibrator',
        'certificate_issuer',
    )
    list_filter = (
        'update',
        'next_due',
        'uuc_id',
        'std_id',
        'calibrator',
        'certificate_issuer',
    )


@admin.register(CalibrationTorque)
class CalibrationTorqueAdmin(admin.ModelAdmin):
    list_display = (
        'cal_torque_id',
        'cwset',
        'cw0',
        'cw90',
        'cw180',
        'cw270',
        'cw_reading',
        'cw_avg',
        'cw_error',
        'cw_uncen',
        'cw_tolerance_start',
        'cw_tolerance_end',
        'ccwset',
        'ccw0',
        'ccw90',
        'ccw180',
        'ccw270',
        'ccw_reading',
        'ccw_avg',
        'ccw_error',
        'ccw_uncen',
        'ccw_tolerance_start',
        'ccw_tolerance_end',
        'update',
        'next_due',
        'status',
        'priority',
        'uuc_id',
        'std_id',
        'calibrator',
        'certificate_issuer',
    )
    list_filter = (
        'update',
        'next_due',
        'uuc_id',
        'std_id',
        'calibrator',
        'certificate_issuer',
    )


@admin.register(UUC)
class UUCAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'machine', 'std')
    list_filter = ('machine', 'std')
    search_fields = ('name',)


@admin.register(UUCStdMap)
class UUCStdMapAdmin(admin.ModelAdmin):
    list_display = ('id', 'uuc', 'std')
    list_filter = ('uuc', 'std')


@admin.register(DialGaugeCalibration)
class DialGaugeCalibrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'res_uuc',
        'acc_std',
        'status',
        'priority',
        'type_a_sd',
        'type_b_res_uuc',
        'type_b_acc_std',
        'type_b_hysteresis',
        'uc_68',
        'k_factor',
        'expanded_uncertainty_95',
    )
    list_filter = (
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
    )


@admin.register(DialGaugeReading)
class DialGaugeReadingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'calibration',
        'uuc_set',
        'std_read_up1',
        'std_read_down1',
        'std_read_up2',
        'std_read_down2',
        'average_up',
        'average_down',
        'error',
        'uncertainty',
        'hysteresis',
        'value_root2',
        'value_root3',
        'value_2root3',
    )
    list_filter = ('calibration',)


@admin.register(BalanceCalibration)
class BalanceCalibrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'received_date',
        'issue_date',
        'certificate_number',
        'procedure_number',
        'unit',
        'status',
        'priority',
        'drift',
        'res_push',
        'res_tip',
        'air_buoyancy',
        'uncertainty_68',
        'uncertainty_95_k',
        'final_uncertainty',
    )
    list_filter = (
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'received_date',
        'issue_date',
    )


@admin.register(BalanceReading)
class BalanceReadingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'calibration',
        'uuc_set',
        'std_read_1',
        'std_read_2',
        'std_read_3',
        'std_read_4',
        'std_read_5',
        'std_read_6',
        'std_read_7',
        'std_read_8',
        'std_read_9',
        'std_read_10',
        'average',
        'standard_deviation',
        'uncertainty',
        'conventional_mass',
        'displayed_value',
    )
    list_filter = ('calibration',)


@admin.register(MicrowaveCalibration)
class MicrowaveCalibrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'certificate_number',
        'status',
        'priority',
    )
    list_filter = (
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
    )


@admin.register(MicrowaveReading)
class MicrowaveReadingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'calibration',
        'test_type',
        'function_test',
        'nominal_value',
        'rf_level',
        'frequency',
        'measured_value',
        'measured_value_numeric',
        'unit',
        'uncertainty',
        'tolerance_limit_min',
        'tolerance_limit_max',
        'test_result',
        'notes',
    )
    list_filter = ('calibration',)


@admin.register(LowFrequencyCalibration)
class LowFrequencyCalibrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'certificate_number',
        'measurement_range',
        'status',
        'priority',
        'dc_uuc_range',
        'dc_uuc_setting',
        'dc_measured_value',
        'dc_uncertainty',
        'dc_tolerance_limit',
        'ac_uuc_range',
        'ac_uuc_setting',
        'ac_measured_value',
        'ac_uncertainty',
        'ac_tolerance_limit',
        'res_uuc_range',
        'res_uuc_setting',
        'res_measured_value',
        'res_uncertainty',
        'res_tolerance_limit',
    )
    list_filter = (
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'status',
        'priority',
    )
    search_fields = (
        'machine__name',
        'machine__serial_number',
        'certificate_number',
    )
    date_hierarchy = 'date_calibration'


@admin.register(HighFrequencyCalibration)
class HighFrequencyCalibrationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'certificate_number',
        'measurement_range',
        'status',
        'priority',
    )
    list_filter = (
        'machine',
        'std_id',
        'calibrator',
        'certificate_issuer',
        'date_calibration',
        'update',
        'next_due',
        'status',
        'priority',
    )
    search_fields = (
        'machine__name',
        'machine__serial_number',
        'certificate_number',
    )
    date_hierarchy = 'date_calibration'


# Import CalibrationEquipmentUsed if it exists
try:
    from .models import CalibrationEquipmentUsed
    
    @admin.register(CalibrationEquipmentUsed)
    class CalibrationEquipmentUsedAdmin(admin.ModelAdmin):
        list_display = (
            'id',
            'calibration_type',
            'calibration_id',
            'equipment',
            'created_at',
        )
        list_filter = ('calibration_type', 'equipment')
        search_fields = (
            'calibration_type',
            'equipment__name',
            'equipment__model',
        )
        readonly_fields = ('created_at',)
        
except ImportError:
    pass