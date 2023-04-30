from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from store_app.api.serializers import StoreSerializer, ProductSerializer
from store_app.models import Product
from django.db import transaction
from django.shortcuts import get_object_or_404

class StoreView(APIView):

     def post(self, request):
        with transaction.atomic():
            serializer = StoreSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductView(APIView):
    
    def post(self, request,):
        with transaction.atomic():
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        store_id = request.data['store_id']
        result = None

        if 'product_id'  in kwargs:
            product = get_object_or_404(Product, store_id=store_id, id=kwargs['product_id'])
            serializer = ProductSerializer(product)
            result = serializer.data
        else:
            related_products = Product.objects.filter(store_id=request.data['store_id'])
            result = list(related_products.values('id', 'name', 'sku', 'inventory_quantity', 'inventory_updated_time', 'store_id'))

        return Response(result, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        product = get_object_or_404(Product, store_id=request.data['store_id'], id=kwargs['product_id'])
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({'message': 'OK', 'data': serializer.data}, status=status.HTTP_200_OK)
