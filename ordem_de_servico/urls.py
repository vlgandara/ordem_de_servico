from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('equipamento/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/new/', views.equipment_new, name='equipment_new'),
]
