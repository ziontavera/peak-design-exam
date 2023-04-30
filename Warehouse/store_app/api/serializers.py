from django.utils.timezone import now
from rest_framework import serializers
from store_app.models import Store, Product
from django.db import transaction


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, required=False)
    sku = serializers.CharField(max_length=50, required=False)
    inventory_quantity = serializers.IntegerField(required=False)
    inventory_updated_time = serializers.DateTimeField(required=False)
    store_id = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'sku', 'inventory_quantity', 'inventory_updated_time', 'store_id']

    
    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.inventory_quantity = validated_data.get('inventory_quantity')
            instance.inventory_updated_time = now()
        
            instance.save()
        return instance
        


class StoreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    url = serializers.URLField(max_length=100)

    class Meta:
        model = Store
        fields = ['id', 'name', 'url']
