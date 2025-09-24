from django.urls import path
from . import views

urlpatterns = [
    path('admin/login/', views.admin_login, name='admin_login'),
    path('', views.index, name='index'),
    path('products.html',views.products,name='products'),
    path('cyberproducts.html',views.cyberproducts,name='cyberproducts'),
    path('aimlproducts.html',views.aimlproducts,name='aimlproducts'),
]