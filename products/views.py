from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q, Avg
from .models import Product, Category, ProductImage
from .forms import ProductForm, ProductImageForm, ProductFilterForm
from dashboard.models import Review
from orders.models import CartItem


def product_list(request):
    products = Product.objects.filter(is_active=True).select_related('seller', 'category')
    form = ProductFilterForm(request.GET)
    
    if form.is_valid():
        if form.cleaned_data.get('search'):
            search = form.cleaned_data['search']
            products = products.filter(Q(title__icontains=search) | Q(description__icontains=search))
        
        if form.cleaned_data.get('category'):
            products = products.filter(category=form.cleaned_data['category'])
        
        if form.cleaned_data.get('min_price'):
            products = products.filter(price__gte=form.cleaned_data['min_price'])
        
        if form.cleaned_data.get('max_price'):
            products = products.filter(price__lte=form.cleaned_data['max_price'])
    
    context = {
        'products': products,
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'images': product.images.all(),
    }
    return render(request, 'products/product_detail.html', context)


@login_required(login_url='login')
def create_product(request):
    if request.user.profile.role != 'seller':
        messages.error(request, 'Vous devez être vendeur pour créer un produit.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, 'Produit créé avec succès!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Créer un produit'})


@login_required(login_url='login')
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.seller != request.user:
        messages.error(request, 'Vous ne pouvez pas modifier ce produit.')
        return redirect('home')
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit mis à jour avec succès!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'products/product_form.html', {'form': form, 'product': product, 'title': 'Modifier le produit'})


@login_required(login_url='login')
@require_POST
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.seller != request.user:
        messages.error(request, 'Vous ne pouvez pas supprimer ce produit.')
        return redirect('home')
    
    product.delete()
    messages.success(request, 'Produit supprimé avec succès!')
    return redirect('seller_products')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_products(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.filter(is_active=True)
    return render(request, 'products/category_products.html', {'category': category, 'products': products})

