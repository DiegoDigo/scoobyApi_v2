from rest_framework import serializers
from product.models import Product, TypeProduct
from validators.validSerializers import RelationModelSerializer


class TypeProductSerializer(RelationModelSerializer):
    class Meta:
        model = TypeProduct
        fields = '__all__'
        read_only_fields = ('id',)


class ProductSerialzier(serializers.ModelSerializer):
    type_product = TypeProductSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):
    type_product = TypeProductSerializer(read_only=False, is_relation=True)

    class Meta:
        model = Product
        fields = '__all__'