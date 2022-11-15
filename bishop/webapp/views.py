from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Product, STATUS_CHOICES
from django.urls import reverse
from django.http import HttpResponseRedirect

def index_view(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def product_create(request):
    if request.method == "GET":
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        errors = {}
        product = request.POST.get('product')
        details = request.POST.get('details')
        price = request.POST.get('price')
        balance = request.POST.get('balance')
        status = request.POST.get('status')
        if not product:
            errors['product'] = 'Наименование товара не может быть пустым'
        elif len(product) > 100:
            errors['product'] = 'Автор не можеть быть длиннее 100 символов'
        elif not details:
            errors['details'] = 'Описание товара не может быть пустым'
        elif len(details) > 1000:
            errors['details'] = 'Описание товара не можеть быть длиннее 3000 символов'
        # elif not price:
        #     errors['price'] = 'Цена не может быть пустым'
        # elif len(price) < 0:
        #     errors['price'] = 'Цена не можеть быть меньше 0'
        # elif not price:
        #     errors['price'] = 'Цена не может быть пустым'
        # elif len(price) < 0:
        #     errors['price'] = 'Цена не можеть быть меньше 0'
        new_product = Product(
            product=product,
            details=details,
            price=price,
            balance=balance,
            status=status
        )
        new_product.save()
        url = reverse('view')
        return HttpResponseRedirect(url)

def product_view(request, pk, *args, **kwargs):
    # article_id = kwargs.get('pk')
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'view.html', context)

def edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "GET":
        return render(request, 'edit.html', {'product': product, 'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        product.product = request.POST.get('product')
        product.details = request.POST.get('details')
        product.balance = request.POST.get('balance')
        product.price = request.POST.get('price')
        product.status = request.POST.get('status')
        product.save()
        return redirect('index')

def delete_view(request, pk):
    Product.objects.filter(pk=pk).delete()
    return redirect('index')