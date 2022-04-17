from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse #Requestを受けてResponseを返すため
from .models import Product  # model Product Classを呼び出す
# Create your views here.

#Requestを受けてResponseを返す　responseの種類は、文字列、Html
def index(request):
    return HttpResponse("Hello world")  #文字列のみ返す

def products(request):
    products = Product.objects.all()  # Product テーブル内検索
    context = {
        "products":products
    }
    return render(request,"myapp/index.html",context)  # Htmlファイルを返す

def product_detail(request,id): # urlのid(数字をparameterとして)受け取る
    product = Product.objects.get(id=id)#urlの数字から、modelのidを検索
    context={
        "product":product
    }
    return render(request,"myapp/detail.html",context)
    #HttpResponse("The product id is:" + str(id)) テスト用


def Test(request):
    return render(request,"myapp/Test.html")  # Htmlファイルを返す