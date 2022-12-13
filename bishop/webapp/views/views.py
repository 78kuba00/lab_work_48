from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from webapp.models import Product, CATEGORIES_CHOICES
from webapp.forms import SearchForm, ProductForm
from webapp.views.base_views import SearchView, UpdateView, DeleteView


# Create your views here.

class IndexViews(SearchView):
    template_name = 'product/index.html'
    context_object_name = 'tasks'
    model = Product
    # ordering = ('-updated_at',)
    paginate_by = 10
    paginate_orphans = 2
    search_form_class = SearchForm
    search_fields = ['name__icontains', 'description__icontains']

    def post(self, request, *args, **kwargs):
        for task_pk in request.POST.getlist('tasks', []):
            self.model.objects.get(pk=task_pk).delete()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

# def index_view(request):
#     products = Product.objects.filter(balance__gt=0).order_by('category', 'name')
#     form = ProductForm()
#     search_form = SearchForm(data=request.GET)
#     if search_form.is_valid():
#         name = search_form.cleaned_data['search']
#         if name:
#             products = products.filter(name=name)
#             # products = products.filter(name__icontains=name)
#
#     return render(request, 'product/index.html',
#                   {'products': products, 'form': form, 'search_form': search_form, 'categories': CATEGORIES_CHOICES})



class ProductView(DetailView):
    template_name = 'product/product_by_category.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return context

def product_by_category_view(request, category, ):
    products = Product.objects.filter(balance__gt=0, category=category).order_by('name')
    form = ProductForm()
    search_form = SearchForm(data=request.GET)
    if search_form.is_valid():
        name = search_form.cleaned_data['search']
        if name:
            products = products.filter(name=name)
            # products = products.filter(name__icontains=name)
    try:
        name_category = dict(CATEGORIES_CHOICES)[category]
    except KeyError:
        raise Http404()
    return render(request, 'product/product_by_category.html',
                  {'products': products, 'form': form, 'search_form': search_form, 'category': name_category})


# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'product/product_view.html', {'product': product})


class ProductCreate(CreateView):
    template_name = 'product/product_by_category.html'
    model = Product
    form_class = ProductForm


# def product_create_view(request):
#     if request.method == "POST":
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product = Product.objects.create(**form.cleaned_data)
#             return redirect('product_view', pk=product.pk)
#         else:
#             products = Product.objects.filter(balance__gt=0).order_by('category', 'name')
#             search_form = SearchForm(data=request.GET)
#             if search_form.is_valid():
#                 name = search_form.cleaned_data['search']
#                 if name:
#                     products = products.filter(name=name)
#             return render(request, 'product/index.html', {'products': products, 'form': form, 'search_form': search_form,
#                                                   'categories': CATEGORIES_CHOICES})


class ProductUpdate(UpdateView):
    form_class = ProductForm
    template_name = 'product/product_create.html'
    model = Product
    product = None
    context_object_name = 'product'
    redirect_url = 'index'


# def product_update_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         form = ProductForm(initial={
#             'name': product.name,
#             'description': product.description,
#             'category': product.category,
#             'balance': product.balance,
#             'price': product.price,
#         })
#         return render(request, 'product_create.html', {'form': form, 'product': product})
#     elif request.method == "POST":
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data['name']
#             product.description = form.cleaned_data['description']
#             product.category = form.cleaned_data['category']
#             product.balance = form.cleaned_data['balance']
#             product.price = form.cleaned_data['price']
#             product.save()
#             return redirect('product_view', pk=product.pk)
#         return render(request, 'product/product_update.html', {'form': form})

class ProductDelete(DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_key = 'product'
    redirect_url = reverse_lazy('index')


# def product_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         return render(request, 'product/product_delete.html', {'product': product})
#     elif request.method == "POST":
#         product.delete()
#         return redirect('index')