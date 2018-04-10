from rest_framework import serializers
from product.models import Product, TypeProduct


class TypeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProduct
        fields = '__all__'


class ProductSerialzier(serializers.ModelSerializer):
    type_product = TypeProductSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):

    type_product = TypeProductSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        type_prd = validated_data['type_product']
        type_product = TypeProduct.objects.create(**type_prd)
        Product.objects.create(type_product=type_product, **validated_data)
        return Product
