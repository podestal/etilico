from . import models
from rest_framework import serializers
from core.serializers import UserSerializer

class GetPromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Promotion
        fields = '__all__'

class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'

class GetProductSerializer(serializers.ModelSerializer):

    category = GetCategorySerializer()

    class Meta:
        model = models.Product
        fields = ['id', 'title', 'description', 'unit_price', 'quantity', 'last_update', 'category']

class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['title', 'description', 'unit_price', 'quantity', 'category']

class UpdateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = ['title', 'description', 'unit_price', 'quantity', 'category']

class GetCustomerSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = models.Customer
        fields = ['id', 'phone', 'membership', 'user']

class CreateCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['phone', 'membership', 'user']


class GetCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cart
        fields = '__all__'

class GetCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CartItem
        fields = '__all__'

class GetOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'

class GetOrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.OrderItem
        fields = '__all__'
