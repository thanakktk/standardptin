from django.urls import path
from .views import CertificateListView, CertificateCreateView, CertificateUpdateView, CertificateDeleteView

urlpatterns = [
    path('', CertificateListView.as_view(), name='cert-list'),
    path('add/', CertificateCreateView.as_view(), name='cert-add'),
    path('<int:pk>/edit/', CertificateUpdateView.as_view(), name='cert-edit'),
    path('<int:pk>/delete/', CertificateDeleteView.as_view(), name='cert-delete'),
] 