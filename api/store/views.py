from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class PromotionViewSet(ModelViewSet):

    queryset = models.Promotion.objects.all()
    serializer_class = serializers.GetPromotionSerializer

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.GetCategorySerializer

class ProductViewSet(ModelViewSet):
    
    queryset = models.Product.objects.all()
    serializer_class = serializers.GetProductSerializer

class CustomerViewSet(ModelViewSet):

    queryset = models.Customer.objects.all()
    serializer_class = serializers.GetCustomerSerializer

class CartViewSet(ModelViewSet): 

    queryset = models.Cart.objects.all()
    serializer_class = serializers.GetCartSerializer

class CartItemViewSet(ModelViewSet):

    queryset = models.CartItem.objects.all()
    serializer_class = serializers.GetCartItemSerializer

class OrderViewSet(ModelViewSet):
    
    queryset = models.Order.objects.all()
    serializer_class = serializers.GetOrderSerializer

class OrderItemViewSet(ModelViewSet):

    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.GetOrderItemSerializer


