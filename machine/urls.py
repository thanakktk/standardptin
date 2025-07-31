from django.urls import path
from .views import MachineListView, MachineCreateView, MachineUpdateView, MachineDeleteView
from . import views

urlpatterns = [
    path('', MachineListView.as_view(), name='machine-list'),
    path('add/', MachineCreateView.as_view(), name='machine-add'),
    path('<int:pk>/edit/', MachineUpdateView.as_view(), name='machine-edit'),
    path('<int:pk>/delete/', MachineDeleteView.as_view(), name='machine-delete'),
]

urlpatterns += [
    path('<int:pk>/send_email/', views.send_machine_email, name='machine-send-email'),
    path('<int:pk>/calibration/', views.calibration_data, name='machine-calibration'),
    path('send_filtered_email/', views.send_filtered_email, name='machine-send-filtered-email'),
] 