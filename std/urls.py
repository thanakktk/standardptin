from django.urls import path
from .views import StandardListView, StandardCreateView, StandardUpdateView, StandardDeleteView

urlpatterns = [
    path('', StandardListView.as_view(), name='std-list'),
    path('add/', StandardCreateView.as_view(), name='std-add'),
    path('<int:pk>/edit/', StandardUpdateView.as_view(), name='std-edit'),
    path('<int:pk>/delete/', StandardDeleteView.as_view(), name='std-delete'),
] 