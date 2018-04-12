from django.urls import path
from order.api import views

urlpatterns = [
    path('', views.OrdersList.as_view(), name="orders"),
    path('<int:pk>', views.OrdersDetail.as_view(), name="orders_detail"),
    path('new/', views.OrdersCreate.as_view(), name="orders_create"),

]
