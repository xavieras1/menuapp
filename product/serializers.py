from rest_framework import serializers

from .models import Location, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "order",
            "get_absolute_url",
            "description",
            #"price",
            "get_image",
            "get_thumbnail",
            "location"
        )

class LocationSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Location
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )