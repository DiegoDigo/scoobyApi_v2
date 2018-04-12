from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include("product.api.urls")),
    path('api/v1/user/', include("custumer.api.urls")),
    path('api/v1/order/', include("order.api.urls")),
]
