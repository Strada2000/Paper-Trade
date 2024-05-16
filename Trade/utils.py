from django.core.exceptions import ObjectDoesNotExist
from .serializers import StockSerializer
from .models import Stock

def getStock(name, externalId=None):
    try:
        stocks = Stock.objects.get(stockName = name)
        return stocks
    
    except ObjectDoesNotExist:
        stockobject=createStock(name, externalId)
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

