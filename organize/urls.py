from django.urls import path
from .views import OrganizeListView, OrganizeCreateView, OrganizeUpdateView, OrganizeDeleteView

urlpatterns = [
    path('', OrganizeListView.as_view(), name='organize-list'),
    path('add/', OrganizeCreateView.as_view(), name='organize-add'),
    path('<int:pk>/edit/', OrganizeUpdateView.as_view(), name='organize-edit'),
    path('<int:pk>/delete/', OrganizeDeleteView.as_view(), name='organize-delete'),
] 