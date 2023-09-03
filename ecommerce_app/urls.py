from django.urls import path
from . import views

urlpatterns=[
    # vendor
    path('vendors/',views.VendorList.as_view()),
    path('vendor/<int:pk>',views.VendorDetail.as_view()),
    # product
    path('products/',views.ProductList.as_view()),
    path('product/<int:pk>',views.ProductDetail.as_view()),
    # customer
    path('customers/',views.CustomerList.as_view()),
    path('customer/<int:pk>',views.CustomerDetail.as_view()),
    # order
    path('orders/',views.OrderList.as_view()),
    path('order/<int:pk>',views.OrderDetail.as_view()),
]