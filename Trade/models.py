from django.db import models

class Users(models.Model):
    #userId = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=256)
    password = models.CharField(max_length=50)

class Stock(models.Model):
    #stockId = models.AutoField(primary_key=True)
    stockName = models.CharField(max_length=100)

class FavouriteStock(models.Model):
    #favouriteId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    stockId = models.ForeignKey(Stock, on_delete=models.CASCADE)
    isFavourite = models.BooleanField()

class PurchasedStocks(models.Model):
    #purchaseId = models.AutoField(primary_key=True)
    stockId = models.ForeignKey(Stock, on_delete=models.CASCADE)
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)
    purchaseValue = models.IntegerField()
    purchaseDate = models.DateTimeField()
    sellValue = models.IntegerField()
    sellDate = models.DateTimeField()
    

