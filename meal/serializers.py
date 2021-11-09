from rest_framework import serializers

from .models import Meal, MealItem

from product.serializers import ProductSerializer

class MealItemSerializer(serializers.ModelSerializer): 
    product = ProductSerializer()   
    class Meta:
        model = MealItem
        fields = (
            "product",
            "quantity",
            "measure",
        )

class MealSerializer(serializers.ModelSerializer):
    items = MealItemSerializer(many=True)

    class Meta:
        model = Meal
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail"
        )

