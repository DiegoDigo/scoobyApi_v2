from django.urls import path
from custumer.api import views

urlpatterns = [
    path('new/', views.CreateUser.as_view(), name="create_user"),
    path('new/profile/', views.CreateProfile.as_view(), name="create_profile"),
    path('update/profile/<int:pk>', views.UpdateProfile.as_view(), name="update_profile"),
    # path('product/create/', views.CreateProduct.as_view(), name="create_product"),
    # path('product/delete/<int:pk>/', views.DeleteProduct.as_view(), name="delete_product"),

]
