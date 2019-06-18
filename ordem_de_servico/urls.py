from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('ordem/list', views.ordem_list, name='ordem_list'),
    path('equipamento/<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('equipment/new/', views.equipment_new, name='equipment_new'),
    path('ordem/<int:pk>/', views.ordem_detail, name='ordem_detail'),
    path('ordem/new/', views.ordem_new, name='ordem_new'),
]
