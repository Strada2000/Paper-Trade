from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, Stock, FavouriteStock, PurchasedStocks
from .serializers import UserSerializer, StockSerializer, FavoutitestockSerializer, PurchasedstockSerializer

@api_view(['POST'])
def signup(request):
    data = request.data
    users =  Users.objects.create(
        email = data['email'],
        password = data['password']
    )
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)
