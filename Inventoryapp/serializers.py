from rest_framework import serializers
from .models import Inventory


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        # fields = '_all_'
        fields = ['id', 'name', 'category', 'quantity', 'price']
