from django.shortcuts import render

from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import OrderList, ListItem
from .serializers import OrderListSerializer

class ItemsList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = OrderList.objects.filter(user=request.user)
        serializer = OrderListSerializer(orders, many=True)
        
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        #order_list = OrderList.objects.get(pk=request.data.id)
        #print(order_list)
        #order_items = ListItem.objects.filter(list=order_list)#.delete()
        #print(order_items)
        #serializer = OrderListSerializer(order_list, data=request.data)
        #print(serializer.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def post(self, request, format=None):
    #    serializer = OrderListSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def post(self, request, format=None):
    #    orders = Order.objects.filter(user=request.user)
    #    serializer = MyOrderSerializer(orders, many=True)
    #    return Response(serializer.data)
