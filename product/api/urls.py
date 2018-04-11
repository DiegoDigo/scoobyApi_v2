from django.urls import path
from product.api import views

urlpatterns = [
    path('product/', views.ListProduct.as_view(), name="products"),
    path('product/<int:pk>/', views.GetProduct.as_view(), name="detail_product"),
    path('product/create/', views.CreateProduct.as_view(), name="create_product"),
    path('product/delete/<int:pk>/', views.DeleteProduct.as_view(), name="delete_product"),
    path('product/update/<int:pk>/', views.UpdateProduct.as_view(), name="update_product"),
]
