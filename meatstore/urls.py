from django.contrib import admin
from django.urls import path
from myso.views import UserList, UserDetail, ProductList, ProductDetail, OrderList, OrderUserDetail, OrderDetailList, OrderDetailDetail, ShoppingCartList, ShoppingCartDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/int:pk/', UserDetail.as_view(), name='user-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/int:pk/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/int:pk/', OrderUserDetail.as_view(), name='order-detail'),
    path('orderdetails/', OrderDetailList.as_view(), name='orderdetail-list'),
    path('orderdetails/int:pk/', OrderDetailDetail.as_view(),
         name='orderdetail-detail'),
    path('shoppingcarts/', ShoppingCartList.as_view(), name='shoppingcart-list'),
    path('shoppingcarts/int:pk/', ShoppingCartDetail.as_view(),
         name='shoppingcart-detail'),
]
