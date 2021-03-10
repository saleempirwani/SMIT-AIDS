from django.shortcuts import render
from .models import Product

def index(request):
    params = {
        'products': Product.objects.all()[:]
    }
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')