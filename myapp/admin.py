from django.contrib import admin
from .models import Product #Modelを読み込む
from .models import Test_DB #Modelを読み込む

# Register your models here.
admin.site.register(Product) #Modelを登録する
admin.site.register(Test_DB) #Modelを登録する
