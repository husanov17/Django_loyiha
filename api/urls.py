from django.urls import path
from .views import ProductApiView, ProductDetailApiView

urlpatterns = [
    path('product/', ProductApiView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail'),
]