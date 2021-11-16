from django.urls import path

from . import views

urlpatterns = [
    path('itemslist/', views.ItemsList.as_view()),  
]