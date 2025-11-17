from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import CartItem
from products.models import Product


@receiver(user_logged_in)
def merge_session_cart(sender, user, request, **kwargs):
    """When an anonymous user logs in, merge session cart into DB-backed CartItem.

    Session cart structure: request.session.get('cart', {}) -> {str(product_id): quantity}
    """
    session_cart = request.session.get('cart')
    if not session_cart:
        return

    for pid, qty in list(session_cart.items()):
        try:
            product = Product.objects.get(pk=int(pid))
        except (Product.DoesNotExist, ValueError):
            continue

        cart_item, created = CartItem.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': qty}
        )
        if not created:
            cart_item.quantity = cart_item.quantity + int(qty)
            cart_item.save()

    # clear session cart after merge
    try:
        del request.session['cart']
    except KeyError:
        pass