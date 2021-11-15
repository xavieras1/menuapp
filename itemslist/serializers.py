from rest_framework import serializers

from .models import OrderList, ListItem

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
            ListItem.objects.create(order=order, **item_data)
            
        return order
