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
    print('tests')
    etems = ListItemSerializer(many=True)
    print(etems)
    items = ListItemSerializer(many=True, required=False)
    print(items)
    

    class Meta:
        model = OrderList
        fields = (
            "type",
            "items",
        )