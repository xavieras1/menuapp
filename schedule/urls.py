from django.urls import path

from . import views

urlpatterns = [
    path('schedule/', views.Schedule.as_view()),  
]