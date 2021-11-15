from rest_framework import serializers

from .models import OrderList, ListItem

from product.models import Product
from product.serializers import ProductSerializer

class ListItemSerializer(serializers.ModelSerializer):    
    product = ProductSerializer()

    class Meta:
        model = ListItem
        fields = (
            "list",
            "product",
            "quantity",
        )

class OrderListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, required=False, allow_null=True)
    
    class Meta:
        model = OrderList
        fields = (
            "id",
            "type",
            "items",
        )

    def create(self, validated_data):
        print('serializer')
        print(validated_data)
        items_data = validated_data.pop('items')
        order = OrderList.objects.filter(type=validated_data['type'])
        print(order)
        #order = OrderList.objects.create(**validated_data)

        for item_data in items_data:
            product_data = item_data.pop('product')
            product = Product.objects.get(pk=product_data['id'])
            ListItem.objects.create(order=order,product=product, **item_data)
            
        return order
