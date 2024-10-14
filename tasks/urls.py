from django.urls import path 
from . import views

urlpatterns = [
    path('tasks', views.tasks, name='tasks'),
    path('logout', views.logout, name='logout'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('change_status/<int:id>', views.change_status, name='change_status'),
]
