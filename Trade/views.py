from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users, Stock, FavouriteStock, PurchasedStocks
from .serializers import UserSerializer, StockSerializer, FavoutitestockSerializer, PurchasedstockSerializer
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST'])
def signup(request):
    data = request.data
    users =  Users.objects.create(
        email = data['email'],
        password = data['password']
    )
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    data = request.data
    users = Users.objects.get(email = data['email'])
    serializer = UserSerializer(users, many=False)

    if users.password == data['password']:
        return Response(
            {
                "userid": serializer.data['id']
            }
         )
    else:
        return Response(serializer.errors)
    
@api_view(['POST'])
def buyStocks(request):
    data = request.data
    stock_instance = getStock(data['stockName'], data['stockExternalId'])
    user_instance = Users.objects.get(id = data['userId'])
    purchase = PurchasedStocks.objects.create(
        stockId = stock_instance,
        userId = user_instance,
        purchaseValue = data['purchaseValue'],
        purchaseDate = datetime.now(),
        sellValue = None,
        sellDate = None
    )
    serializer = PurchasedstockSerializer(purchase, many=False)
    return Response(serializer.data)

def getStock(name, externalId):
    try:
        stocks = Stock.objects.get(stockName = name)
        return stocks
    
    except ObjectDoesNotExist:
        stockobject=createStock(name, externalId)
        serializer1 = StockSerializer(stockobject,many=False)
        return stockobject

def createStock(name, externalId):
    stocks = Stock.objects
    try:
        stocks.create(
            stockName = name,
            stockExternalId = externalId
        )
    except:
        return False
    return Stock.objects.get(stockName = name)
