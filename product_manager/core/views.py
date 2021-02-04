from django.http import Http404
from django.shortcuts import render, redirect, resolve_url
from product_manager.core.models import Product
from product_manager.core.forms import ProductForm

# Create your views here.
def list_products(request):
    return render(request, 'list_products.html',
                  context={'products': Product.objects.all()})

def new(request):
    if request.method == 'GET':
        return render(request, 'new_product.html',
                      context={'form': ProductForm()})

    form = ProductForm(request.POST)
    if not form.is_valid():
        return render(request, 'new_product.html', context={'form': form})

    Product(**form.cleaned_data).save()
    return redirect('list')

def edit(request, product_id):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product(**form.cleaned_data, id=product_id).save()
            return redirect('list')

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404

    form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form,
                                                 'product_id': product_id})

def delete(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404
    product.delete()
    return redirect(resolve_url('list'))
