from multiprocessing import context
from django.shortcuts import render,redirect #ページ遷移用
from django.http import HttpResponse #Requestを受けてResponseを返すため
from .models import Product  # model Product Classを呼び出す
from .models import Test_DB  # model Test_DB Classを呼び出す
from django.conf import settings  # 設定からファイルパスを呼び出すため

# Create your views here.

#Requestを受けてResponseを返す　responseの種類は、文字列、Html
def index(request):
    return HttpResponse("Hello world")  #文字列のみ返す

def products(request):
    products = Product.objects.all()  # Product テーブル内検索
    context = {
        "products":products
    }
    return render(request,"myapp/index.html",context)  # Htmlファイルを返す contextで値をhtmlに渡す

def product_detail(request,id): # urlのid(数字をparameterとして)受け取る
    product = Product.objects.get(id=id)#urlの数字から、modelのidを検索
    context={
        "product":product
    }
    return render(request,"myapp/detail.html",context)
    #HttpResponse("The product id is:" + str(id)) テスト用

def add_product(request):
    if request.method == "POST":  # requestがpostだったらsubmitされたデータを取得する
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        image = request.FILES["upload"]

        #データベースへ値を追加する
        product = Product(name=name,price=price,desc=desc,image=image)
        product.save()
    return render(request, "myapp/addproduct.html")

def update_product(request,id):  # idはあくまで引数(Urlから取得する)
    product = Product.objects.get(id=id)#urlの数字から、modelのidを検索
    if request.method=="POST":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.desc = request.POST.get("desc")
        product.image = request.FILES["upload"]
        product.save()
        
        return redirect("/myapp/products")


    context={
        "product":product
    }
    #HttpResponse("The product id is:" + str(id)) テスト用
    return render(request, "myapp/updateproduct.html",context)


def delete_product(request,id):
    product = Product.objects.get(id=id)
    context={
        "product":product
    }

    if request.method =="POST":
        product.delete()
        return redirect("/myapp/products")
    
    return render(request,"myapp/delete.html",context)





def Test(request):

    from tensorflow.keras.models import load_model
    import joblib
    import numpy as np
    # 設定からモデルファイルのパスを取得
    print(settings.MODEL_FILE_PATH)

    flower_model = load_model(settings.MODEL_FILE_PATH)
    flower_scaler = joblib.load(settings.SCALER_FILE_PATH)

    flower = [[14,14,1,41]]
    flower = flower_scaler.transform(flower)
    predicted = np.argmax(flower_model.predict(flower),axis=1)
    classes = np.array(["setosa","versicolor","virginica"])
    print(predicted)
    print(classes[predicted])

    context={
        "product1":classes[predicted],
    }




    if request.method == "POST":  # requestがpostだったらsubmitされたデータを取得する
        name = request.POST.get("name")
        price = request.POST.get("price")
        desc = request.POST.get("desc")
        #image = request.FILES["upload"]
        print(name,price,desc)
        return redirect("/myapp/products/Test/result")


    return render(request,"myapp/Test.html",context)  # Htmlファイルを返す


def TestResult(request):
    product1 = "A"
    product2 = "B"
    context={
        "product1":product1,
        "product2":product2
    }

    


    return render(request,"myapp/TestResult.html",context) 

def StressForm(request):


    return render(request,"myapp/StressForm.html")

