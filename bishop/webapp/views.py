from django.shortcuts import render
from webapp.models import Product

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# Create your views here.
