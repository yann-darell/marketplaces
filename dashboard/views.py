from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q
from .models import Notification, Review
from .forms import ReviewForm
from products.models import Product
from orders.models import Order, CartItem


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(is_active=True)[:6]
        cart_count = CartItem.objects.filter(user=request.user).count()
        context = {
            'products': products,
            'cart_count': cart_count,
        }
    else:
        products = Product.objects.filter(is_active=True)[:6]
        context = {'products': products}
    
    return render(request, 'dashboard/home.html', context)


@login_required(login_url='login')
def dashboard(request):
    """Vue de redirection qui envoie l'utilisateur vers son dashboard approprié"""
    profile = request.user.profile
    if profile.role == 'seller':
        return redirect('seller_dashboard')
    else:
        return redirect('buyer_dashboard')


@login_required(login_url='login')
def buyer_dashboard(request):
    if request.user.profile.role == 'seller':
        return redirect('seller_dashboard')
    
    orders = Order.objects.filter(buyer=request.user)
    notifications = Notification.objects.filter(user=request.user, is_read=False)[:5]
    cart_items = CartItem.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
        'notifications': notifications,
        'cart_count': cart_items.count(),
        'total_spent': orders.aggregate(Sum('total_price'))['total_price__sum'] or 0,
    }
    return render(request, 'dashboard/buyer_dashboard.html', context)


@login_required(login_url='login')
def seller_dashboard(request):
    if request.user.profile.role != 'seller':
        messages.error(request, 'Vous devez être vendeur.')
        return redirect('buyer_dashboard')
    
    products = Product.objects.filter(seller=request.user)
    orders = Order.objects.filter(items__product__seller=request.user).distinct()
    
    stats = {
        'total_products': products.count(),
        'total_sales': orders.aggregate(Sum('total_price'))['total_price__sum'] or 0,
        'total_orders': orders.count(),
        'active_products': products.filter(is_active=True).count(),
    }
    
    context = {
        'products': products,
        'orders': orders[:10],
        'stats': stats,
    }
    return render(request, 'dashboard/seller_dashboard.html', context)


@login_required(login_url='login')
def seller_products(request):
    if request.user.profile.role != 'seller':
        messages.error(request, 'Vous devez être vendeur.')
        return redirect('home')
    
    products = Product.objects.filter(seller=request.user)
    return render(request, 'dashboard/seller_products.html', {'products': products})


@login_required(login_url='login')
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review, created = Review.objects.get_or_create(
                product=product,
                buyer=request.user,
                defaults={'rating': form.cleaned_data['rating'], 'comment': form.cleaned_data['comment']}
            )
            if not created:
                review.rating = form.cleaned_data['rating']
                review.comment = form.cleaned_data['comment']
                review.save()
            
            messages.success(request, 'Avis ajouté avec succès!')
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    
    return render(request, 'dashboard/add_review.html', {'form': form, 'product': product})


@login_required(login_url='login')
def notifications(request):
    user_notifications = Notification.objects.filter(user=request.user)
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        if notification_id:
            notification = get_object_or_404(Notification, pk=notification_id, user=request.user)
            notification.is_read = True
            notification.save()
            messages.success(request, 'Notification marquée comme lue.')
            return redirect('notifications')
    
    context = {'notifications': user_notifications}
    return render(request, 'dashboard/notifications.html', context)

