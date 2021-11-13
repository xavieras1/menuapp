from django.urls import path

from . import views

urlpatterns = [
    #path('checkout/', views.checkout),
    path('itemslist/', views.ItemsList.as_view()),  
]