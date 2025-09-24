from django.urls import path
from .views import (
    CalibrationForceListView, CalibrationForceCreateView, CalibrationForceUpdateView, CalibrationForceDeleteView,
    CalibrationPressureListView, CalibrationPressureCreateView, CalibrationPressureUpdateView, CalibrationPressureDeleteView,
    CalibrationTorqueListView, CalibrationTorqueCreateView, CalibrationTorqueUpdateView, CalibrationTorqueDeleteView,
    BalanceCalibrationListView, BalanceCalibrationCreateView, BalanceCalibrationUpdateView, BalanceCalibrationDeleteView,
    HighFrequencyCalibrationUpdateView, LowFrequencyCalibrationUpdateView,
    calibration_dashboard, machine_calibration_list, create_calibration_for_machine, calibration_by_type,
    select_machine_for_calibration, create_calibration_with_machine, calibration_report, calibration_report_detail, export_to_word, export_to_excel,
    increase_priority, close_work, export_certificate_excel, export_balance_certificate_docx
)

urlpatterns = [
    # หน้าหลักการสอบเทียบ
    path('', calibration_dashboard, name='calibrate-dashboard'),
    
    # รายงานสอบเทียบ
    path('report/', calibration_report, name='calibrate-report'),
    path('report/detail/', calibration_report_detail, name='calibrate-report-detail'),
    path('export/word/', export_to_word, name='export-calibration-word'),
    path('export/excel/', export_to_excel, name='export-calibration-excel'),
    
    # หน้าดึงข้อมูลเครื่องมือเพื่อบันทึกการสอบเทียบ
    path('select-machine/', select_machine_for_calibration, name='select-machine-for-calibration'),
    path('create-with-machine/<int:machine_id>/', create_calibration_with_machine, name='create-calibration-with-machine'),
    
    # การสอบเทียบตามประเภท
    path('type/<str:calibration_type>/', calibration_by_type, name='calibrate-by-type'),
    
    # การสอบเทียบของเครื่องมือเฉพาะ
    path('machine/<int:machine_id>/', machine_calibration_list, name='machine-calibration-list'),
    path('machine/<int:machine_id>/add/', create_calibration_for_machine, name='machine-calibration-add'),
    
    # URL เดิม (สำหรับการจัดการทั่วไป)
    path('force/', CalibrationForceListView.as_view(), name='calibrate-force-list'),
    path('force/add/', CalibrationForceCreateView.as_view(), name='calibrate-force-add'),
    path('force/<int:pk>/edit/', CalibrationForceUpdateView.as_view(), name='calibrate-force-edit'),
    path('force/<int:pk>/delete/', CalibrationForceDeleteView.as_view(), name='calibrate-force-delete'),

    path('pressure/', CalibrationPressureListView.as_view(), name='calibrate-pressure-list'),
    path('pressure/add/', CalibrationPressureCreateView.as_view(), name='calibrate-pressure-add'),
    path('pressure/<int:pk>/edit/', CalibrationPressureUpdateView.as_view(), name='calibrate-pressure-edit'),
    path('pressure/<int:pk>/delete/', CalibrationPressureDeleteView.as_view(), name='calibrate-pressure-delete'),

    path('torque/', CalibrationTorqueListView.as_view(), name='calibrate-torque-list'),
    path('torque/add/', CalibrationTorqueCreateView.as_view(), name='calibrate-torque-add'),
    path('torque/<int:pk>/edit/', CalibrationTorqueUpdateView.as_view(), name='calibrate-torque-edit'),
    path('torque/<int:pk>/delete/', CalibrationTorqueDeleteView.as_view(), name='calibrate-torque-delete'),

    path('balance/', BalanceCalibrationListView.as_view(), name='calibrate-balance-list'),
    path('balance/add/', BalanceCalibrationCreateView.as_view(), name='calibrate-balance-add'),
    path('balance/<int:pk>/edit/', BalanceCalibrationUpdateView.as_view(), name='calibrate-balance-edit'),
    path('balance/<int:pk>/delete/', BalanceCalibrationDeleteView.as_view(), name='calibrate-balance-delete'),
    
    path('high-frequency/<int:pk>/edit/', HighFrequencyCalibrationUpdateView.as_view(), name='calibrate-high-frequency-edit'),
    path('low-frequency/<int:pk>/edit/', LowFrequencyCalibrationUpdateView.as_view(), name='calibrate-low-frequency-edit'),
    
    # เพิ่มระดับความเร่งด่วน
    path('increase-priority/<str:cal_type>/<int:cal_id>/', increase_priority, name='increase-priority'),
    
    # ปิดงาน
    path('close-work/<str:cal_type>/<int:cal_id>/', close_work, name='close-work'),
    
    # Export ใบรับรอง
    path('export-certificate/<int:cal_id>/<str:cal_type>/', export_certificate_excel, name='export-certificate-excel'),
    path('export-balance-certificate/<int:cal_id>/', export_balance_certificate_docx, name='export-balance-certificate-docx'),
] 