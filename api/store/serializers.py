from . import models
from rest_framework import serializers

class GetPromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Promotion
        fields = '__all__'

class GetCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'

class GetProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'

class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = '__all__'

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
