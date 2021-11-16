from django.shortcuts import render

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Schedule, ScheduleItem
from .serializers import ScheduleSerializer

class ScheduleView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        schedules = Schedule.objects.filter(user=request.user)
        serializer = ScheduleSerializer(schedules, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        schedule = Schedule.objects.filter(user=request.user)
        schedule_items = ScheduleItem.objects.filter(schedule=schedule[0]).delete()
        #schedule_items.delete()
        serializer = ScheduleSerializer(schedule[0], data=request.data)
        serializer.create(request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)