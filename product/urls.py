from django.urls import path
from . import views

urlpatterns = [
    path('', views.insert_pro, name='insert-pro'),
    path('show/', views.show_pro, name='show-pro'),
    path('edit/<int:pk>', views.edit_pro, name='edit-pro'),
    path('remove/<int:pk>', views.remove_pro, name='remove-pro'),
]