from django.contrib import admin
from .models import Users, Stock, FavouriteStock, PurchasedStocks

admin.site.register(Users)
admin.site.register(Stock)
admin.site.register(FavouriteStock)
admin.site.register(PurchasedStocks)