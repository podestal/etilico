from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers

class PromotionViewSet(ModelViewSet):

    queryset = models.Promotion.objects.all()
    serializer_class = serializers.GetPromotionSerializer

class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.GetCategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]


class ProductViewSet(ModelViewSet):
    
    queryset = models.Product.objects.filter(quantity__gt=1)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['quantity']
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):

        if self.request.method == 'POST':
            return serializers.CreateProductSerializer
        if self.request.method == 'PATCH':
            return serializers.UpdateProductSerializer
        return serializers.GetProductSerializer
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Product.objects.select_related('category')
        return models.Product.objects.filter(quantity__gt=1).select_related('category')
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'DELETE']:
            return [IsAdminUser()]
        return [AllowAny()]
        

class CustomerViewSet(ModelViewSet):

    queryset = models.Customer.objects.all()
    serializer_class = serializers.GetCustomerSerializer
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = models.Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = serializers.GetCustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = serializers.GetCustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)



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


