from rest_framework import generics
from rest_framework.permissions import AllowAny
from order.models import Order
from order.api.serializers import OrderSerializer, CreateOrderSerializer


class OrdersList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrdersDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, id=self.kwargs['pk'])


class OrdersCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()


