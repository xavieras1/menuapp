from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Meal
from .serializers import MealSerializer

class LatestMealsList(APIView):
    def get(self, request, format=None):
        meals = Meal.objects.all()[0:4]
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

class MealDetail(APIView):
    def get_object(self, meal_slug):
        try:
            return Meal.objects.get(slug=meal_slug)
        except Meal.DoesNotExist:
            raise Http404
    
    def get(self, request, meal_slug, format=None):
        meal = self.get_object(meal_slug)
        serializer = MealSerializer(meal)
        return Response(serializer.data)
