from django.urls import path
from . import views

urlpatterns = [
    path('', views.MachineListView.as_view(), name='machine-list'),
    path('add/', views.MachineCreateView.as_view(), name='machine-add'),
    path('<int:pk>/edit/', views.MachineUpdateView.as_view(), name='machine-edit'),
    path('<int:pk>/delete/', views.MachineDeleteView.as_view(), name='machine-delete'),
    path('<int:pk>/send-email/', views.send_machine_email, name='machine-send-email'),
    path('send-filtered-email/', views.send_filtered_email, name='machine-send-filtered-email'),
    path('<int:pk>/calibration/', views.calibration_data, name='machine-calibration'),
    path('<int:pk>/create-calibration-request/', views.create_calibration_request, name='create-calibration-request'),
    
    # CalibrationEquipment URLs
    path('calibration-equipment/', views.CalibrationEquipmentListView.as_view(), name='calibration-equipment-list'),
    path('calibration-equipment/add/', views.CalibrationEquipmentCreateView.as_view(), name='calibration-equipment-add'),
    path('calibration-equipment/<int:pk>/edit/', views.CalibrationEquipmentUpdateView.as_view(), name='calibration-equipment-edit'),
    path('calibration-equipment/<int:pk>/delete/', views.CalibrationEquipmentDeleteView.as_view(), name='calibration-equipment-delete'),
] 