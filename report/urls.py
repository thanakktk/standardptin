from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report-list'),
    path('export-word/', views.export_word, name='report-export-word'),
    path('export-excel/', views.export_excel, name='report-export-excel'),
    path('download-certificate/', views.download_certificate, name='report-download-certificate'),
]
