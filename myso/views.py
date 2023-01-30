from rest_framework import generics
from .models import Product, ShoppingCart, User, Order, OrderDetail
from .serializers import ProductSerializer, ShoppingCartSerializer, UserAccountSerializer, OrderSerializer, OrderDetailSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailList(generics.ListCreateAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class ShoppingCartList(generics.ListCreateAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class ShoppingCartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
