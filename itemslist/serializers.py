from rest_framework import serializers

from .models import OrderList, ListItem

from product.serializers import ProductSerializer

class ListItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = ListItem
        fields = (
            "product",
            "quantity",
        )

class OrderListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, required=False, allow_null=True)
    

    class Meta:
        model = OrderList
        fields = (
            "type",
            "items",
        )

class OrderListSerializer2(serializers.ModelSerializer):
    etems = ListItemSerializer(many=True)
    

    class Meta:
        model = OrderList
        fields = (
            "type",
            "items",
        )

class OrderListSerializer3(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, required=False)
    

    class Meta:
        model = OrderList
        fields = (
            "type",
            "items",
        )