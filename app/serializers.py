from rest_framework import serializers
from .models import Store, Product


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['store_id', 'store_location','store_timestamp']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['Product_id', 'Product_location','Product_timestamp']
