from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import APIException
from product.api.serializers import ProductSerialzier
from custumer.api.serializers import UserSerializer
from order.models import Order, ItensOrder


class ItensOrderSerializer(serializers.ModelSerializer):
    product = ProductSerialzier(read_only=False, is_relation=True)

    class Meta:
        model = ItensOrder
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    itens = ItensOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    itens = ItensOrderSerializer(many=True)
    user = UserSerializer(read_only=False, is_relation=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        itens = validated_data.pop('itens')
        instance = Order.objects.create(**validated_data)
        for iten in itens:
            print(iten['product'], iten['quantity'], iten['price'])
            item, created = ItensOrder.objects.create(product=iten['product'], quantity=iten['quantity'],
                                                      price=iten['price'])
            instance.itens.add(item)
        return instance
