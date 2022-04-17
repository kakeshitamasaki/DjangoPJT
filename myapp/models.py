from django.db import models

# Create your models here.
# Databaseの中身を定義する(SPOのLIST設定のように)

class Product(models.Model):
    def __str__(self):  # 特殊メソッド　文字列で値を返す
        return self.name

    name = models.CharField(max_length=100)  # name列 文字列がた 100文字
    price = models.IntegerField()            # price列　整数型
    desc = models.CharField(max_length=200)