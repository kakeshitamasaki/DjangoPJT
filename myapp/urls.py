from django.contrib import admin
from django.urls import path
from .import views  # viewファイルの呼び出し

app_name = "myapp"  # NameSpaseの仕組み
urlpatterns = [
    #path('admin/', admin.site.urls),
    path("hello/", views.index), # views.def名
    path("products/",views.products,name="products"),
    path("products/<int:id>/",views.product_detail,name="product_detail"),  # urlに書いてあるidによって変化させる
    path("products/add/",views.add_product,name="add_product"),
    path("products/update/<int:id>/",views.update_product,name="update_product"),  # urlに書いてあるid(数字)によって変化させる
    path("products/delete/<int:id>/",views.delete_product,name="delete_product"),
    path("products/Test/",views.Test),
    path("products/Test/result",views.TestResult,name="TestResultAA"),
    path("products/StressForm/",views.StressForm),

]

 
 
