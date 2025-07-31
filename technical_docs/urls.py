from django.urls import path
from . import views

app_name = 'technical_docs'

urlpatterns = [
    path('', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('download/<int:pk>/', views.download_document, name='download_document'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
] 