from django.urls import path 
from todolist import views

urlpatterns = [
    path('dailytasks/', views.dailyTasksAdd),
    path('dailytasks/<int:pk>/', views.dailyTasksEdit),
]