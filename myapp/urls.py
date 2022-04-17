from django.contrib import admin
from django.urls import path
from .import views  # viewファイルの呼び出し

app_name = "myapp"  # NameSpaseの仕組み
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("hello/", views.index), # views.def名
    path("products/",views.products),
    path("products/<int:id>/",views.product_detail,name="product_detail")  # urlに書いてあるidによって変化させる
]

 
 
