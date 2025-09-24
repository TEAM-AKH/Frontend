# Create your views here.
from django.shortcuts import render
from .models import Products_data, Events_data

def admin_login(request):
    return render(request, 'admin_login.html')

def product_list(request):
    products = Products_data.objects.all()
    return render(request, 'products.html', {'products': products})

def event_list(request):
    events = Events_data.objects.all()
    return render(request, 'event.html', {'events': events})

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def products(request):
    products_data = Products_data.objects.exclude(category__in=['AI-ML', 'Cyber'])
    return render(request, 'products.html', {'products_data': products_data})

def cyberproducts(request):
    cyber_products = Products_data.objects.filter(category='Cyber')
    return render(request, 'cyberproducts.html', {'cyber_products': cyber_products})

def aimlproducts(request):
    aiml_products = Products_data.objects.filter(category='AI-ML')
    return render(request, 'aimlproducts.html', {'aiml_products': aiml_products})

def event(request):
    events = Events_data.objects.all()
    return render(request, 'event.html', {'events': events})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def sap(request):
    return render(request, 'sap.html')

def cloud(request):
    return render(request, 'cloud.html')

def customsap(request):
    return render(request, 'customsap.html')

def ongoing(request):
    return render(request, 'ongoing.html')

def training(request):
    return render(request, 'training.html')

def optimization(request):
    return render(request, 'optimization.html')

def fullstack(request):
    return render(request, 'fullstack.html')

def mobile(request):
    return render(request, 'mobile.html')

def expertise(request):
    return render(request, 'expertise.html')

def aiml(request):
    return render(request, 'aiml.html')