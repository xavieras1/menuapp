from django.db.models import Q
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Location
from .serializers import ProductSerializer, LocationSerializer

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, location_slug, product_slug):
        try:
            return Product.objects.filter(location__slug=location_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, location_slug, product_slug, format=None):
        product = self.get_object(location_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class LocationDetail(APIView):
    def get_object(self, location_slug):
        try:
            return Location.objects.get(slug=location_slug)
        except Location.DoesNotExist:
            raise Http404
    
    def get(self, request, location_slug, format=None):
        location = self.get_object(location_slug)
        serializer = LocationSerializer (location)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})