from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Meal
from .serializers import MealSerializer

class LatestMealsList(APIView):
    def get(self, request, format=None):
        meals = Meal.objects.all()[0:4]
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)
