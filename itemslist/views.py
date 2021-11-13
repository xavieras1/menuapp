from django.shortcuts import render

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import OrderList
from .serializers import OrderListSerializer

class ItemsList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = OrderList.objects.filter(user=request.user)
        serializer = OrderListSerializer(orders, many=True)
        return Response(serializer.data)

    #def post(self, request, format=None):
    #    orders = Order.objects.filter(user=request.user)
    #    serializer = MyOrderSerializer(orders, many=True)
    #    return Response(serializer.data)
