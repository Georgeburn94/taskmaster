from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Define your URL patterns here
    path('', views.index, name='index'),
    path('edit/<int:id>/', views.edit_task, name='edit'),
    path('complete/<int:id>/', views.complete_task, name='complete'),
    path('incomplete/<int:id>/', views.incomplete_task, name='incomplete'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
]