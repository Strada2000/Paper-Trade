from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name = 'Signup API' ),
    path('login',views.login, name = 'Login API'),
    path('purchase', views.buyStocks, name='Purchase Stocks'),
    path('sell',views.sellStocks,name = 'selling stocks'),
    path('myStocks', views.getMyStocks, name = 'My purchased stocks list')
]
