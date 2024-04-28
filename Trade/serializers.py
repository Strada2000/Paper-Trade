from rest_framework.serializers import ModelSerializer
from .models import Users, Stock, FavouriteStock, PurchasedStocks

class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class FavoutitestockSerializer(ModelSerializer):
    class Meta:
        model = FavouriteStock
        fields = '__all__'

class PurchasedstockSerializer(ModelSerializer):
    class Meta:
        model = PurchasedStocks
        fields = '__all__'