from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import ProductSerialzier, CreateProductSerializer
from product.models import Product


class ListProduct(generics.ListAPIView):
    serializer_class = ProductSerialzier
    queryset = Product.objects.all()
    permission_classes = [AllowAny]


class GetProduct(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerialzier
    queryset = Product.objects.all()
    permission_classes = [AllowAny]


class DeleteProduct(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductSerialzier
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class CreateProduct(generics.CreateAPIView):
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()
    permission_classes = [AllowAny]