"""
URL configuration for acknowledgementhub_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from backend import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    path('home.html', views.home, name='home'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('aiml.html', views.aiml, name='aiml'),
    path('aimlproducts.html', views.aimlproducts, name='aimlproducts'),
    path('cloud.html', views.cloud, name='cloud'),
    path('customsap.html', views.customsap, name='customsap'),
    path('cyberproducts.html', views.cyberproducts, name='cyberproducts'),
    path('expertise.html', views.expertise, name='expertise'),
    path('fullstack.html', views.fullstack, name='fullstack'),
    path('mobile.html', views.mobile, name='mobile'),
    path('ongoing.html', views.ongoing, name='ongoing'),
    path('optimization.html', views.optimization, name='optimization'),
    path('sap.html', views.sap, name='sap'),
    path('services.html', views.services, name='services'),
    path('training.html', views.training, name='training'),
    path('products.html', views.products, name='products'),
    path('event.html', views.event_list, name='event'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
