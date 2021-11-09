from django.urls import path, include

from meal import views

urlpatterns = [
    path('latest-meals/', views.LatestMealsList.as_view()),
    #path('products/search/', views.search),
    #path('products/<slug:location_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    #path('products/<slug:location_slug>/', views.LocationDetail.as_view()),
]