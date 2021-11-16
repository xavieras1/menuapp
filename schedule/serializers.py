from rest_framework import serializers

from .models import Schedule, ScheduleItem

from meal.models import Meal
from meal.serializers import MealSerializer

class ScheduleItemSerializer(serializers.ModelSerializer):    
    meal = MealSerializer()

    class Meta:
        model = ScheduleItem
        fields = (
            "schedule",
            "meal",
            "quantity",
            "person",
            "shift",
            "day"
        )

class ScheduleSerializer(serializers.ModelSerializer):
    items = ScheduleItemSerializer(many=True, required=False, allow_null=True)
    
    class Meta:
        model = Schedule
        fields = (
            "id",
            "user",
            "items",
        )

    def create(self, pre_validated_data):
        validated_data = pre_validated_data.data
        items_data = validated_data.pop('items')
        schedule = Schedule.objects.filter(user=pre_validated_data.user)

        for item_data in items_data:
            meal_data = item_data.pop('meal')
            meal = Meal.objects.get(pk=meal_data['id'])
            ScheduleItem.objects.create(schedule=schedule[0],meal=meal, **item_data)
            
        return schedule
