from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Sum, F
from decimal import Decimal
import uuid
from .models import Order, OrderItem, CartItem
from .forms import CartItemForm, CheckoutForm
from products.models import Product


def cart(request):
    """Display the user's cart. Supports both authenticated (DB-backed) and
    anonymous users (session-backed cart stored as {'product_id': quantity}).
    """
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user).select_related('product')
        total = sum(item.product.price * item.quantity for item in cart_items)
    else:
        session_cart = request.session.get('cart', {})
        cart_items = []
        total = 0
        for pid, qty in session_cart.items():
            try:
                prod = Product.objects.get(pk=int(pid))
            except Product.DoesNotExist:
                continue
            # create a lightweight object with product & quantity & pk
            class _Item:
                pass
            it = _Item()
            it.product = prod
            it.quantity = qty
            it.pk = prod.pk
            cart_items.append(it)
            total += prod.price * qty

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'orders/cart.html', context)


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    else:
        # session-backed cart: store as {product_id: quantity}
        session_cart = request.session.get('cart', {})
        pid = str(product.pk)
        session_cart[pid] = session_cart.get(pid, 0) + quantity
        request.session['cart'] = session_cart

    messages.success(request, f'{product.title} ajouté au panier!')
    return redirect('cart')


@require_POST
def remove_from_cart(request, item_id):
    # support both DB-backed and session-backed removal
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, pk=item_id, user=request.user)
        product_title = cart_item.product.title
        cart_item.delete()
        messages.success(request, f'{product_title} supprimé du panier!')
    else:
        # item_id will be the product id in session cart
        session_cart = request.session.get('cart', {})
        pid = str(item_id)
        if pid in session_cart:
            # try to get product title for message
            try:
                prod = Product.objects.get(pk=int(pid))
                product_title = prod.title
            except Product.DoesNotExist:
                product_title = 'Article'
            session_cart.pop(pid, None)
            request.session['cart'] = session_cart
            messages.success(request, f'{product_title} supprimé du panier!')

    return redirect('cart')


@login_required(login_url='login')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    if not cart_items.exists():
        messages.error(request, 'Votre panier est vide.')
        return redirect('product_list')
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
            order = Order.objects.create(
                buyer=request.user,
                order_number=order_number,
                total_price=total,
                payment_method=form.cleaned_data['payment_method'],
                delivery_address=form.cleaned_data['delivery_address'],
                phone_number=form.cleaned_data['phone_number'],
            )
            
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                )
                item.product.stock -= item.quantity
                item.product.save()
            
            cart_items.delete()
            messages.success(request, f'Commande créée: {order_number}')
            return redirect('order_detail', pk=order.pk)
    else:
        form = CheckoutForm()
    
    context = {
        'cart_items': cart_items,
        'total': total,
        'form': form,
    }
    return render(request, 'orders/checkout.html', context)


@login_required(login_url='login')
def order_list(request):
    orders = Order.objects.filter(buyer=request.user).prefetch_related('items')
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required(login_url='login')
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.buyer != request.user and request.user != order.items.first().product.seller if order.items.exists() else True:
        messages.error(request, 'Accès non autorisé.')
        return redirect('home')
    
    items = order.items.all()
    context = {
        'order': order,
        'items': items,
    }
    return render(request, 'orders/order_detail.html', context)


@login_required(login_url='login')
def seller_orders(request):
    if request.user.profile.role != 'seller':
        messages.error(request, 'Vous devez être vendeur.')
        return redirect('home')
    
    orders = Order.objects.filter(items__product__seller=request.user).distinct()
    return render(request, 'orders/seller_orders.html', {'orders': orders})

