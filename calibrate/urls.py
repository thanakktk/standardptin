from django.urls import path
from .views import (
    CalibrationForceListView, CalibrationForceCreateView, CalibrationForceUpdateView, CalibrationForceDeleteView,
    CalibrationPressureListView, CalibrationPressureCreateView, CalibrationPressureUpdateView, CalibrationPressureDeleteView,
    CalibrationTorqueListView, CalibrationTorqueCreateView, CalibrationTorqueUpdateView, CalibrationTorqueDeleteView,
    calibration_dashboard, machine_calibration_list, create_calibration_for_machine, calibration_by_type,
    select_machine_for_calibration, create_calibration_with_machine, calibration_report, calibration_report_detail, export_to_word, export_to_excel
)

urlpatterns = [
    # หน้าหลักการปรับเทียบ
    path('', calibration_dashboard, name='calibrate-dashboard'),
    
    # รายงานปรับเทียบ
    path('report/', calibration_report, name='calibrate-report'),
    path('report/detail/', calibration_report_detail, name='calibrate-report-detail'),
    path('export/word/', export_to_word, name='export-calibration-word'),
    path('export/excel/', export_to_excel, name='export-calibration-excel'),
    
    # หน้าดึงข้อมูลเครื่องมือเพื่อบันทึกการปรับเทียบ
    path('select-machine/', select_machine_for_calibration, name='select-machine-for-calibration'),
    path('create-with-machine/<int:machine_id>/', create_calibration_with_machine, name='create-calibration-with-machine'),
    
    # การปรับเทียบตามประเภท
    path('type/<str:calibration_type>/', calibration_by_type, name='calibrate-by-type'),
    
    # การปรับเทียบของเครื่องมือเฉพาะ
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
] 