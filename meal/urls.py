from django.urls import path, include

from meal import views

urlpatterns = [
    path('latest-meals/', views.LatestMealsList.as_view()),
    path('meals/', views.GetMealsList.as_view()),
    #path('products/search/', views.search),
    #path('products/<slug:location_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('meals/<slug:meal_slug>/', views.MealDetail.as_view()),
]