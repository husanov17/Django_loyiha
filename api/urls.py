from django.urls import path
from .views import ProductApiView, ProductDetailApiView,CreateProductAPIView

urlpatterns = [
    path('products/', ProductApiView.as_view(), name='product-list'),
    path('product/', CreateProductAPIView.as_view(), name='product-create'),
    path('product/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail'),
]