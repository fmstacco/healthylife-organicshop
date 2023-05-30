from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Product, Wishlist
from .forms import UserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed.Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    products = user_wishlist.products.all()
    context = {'wishlist': products}
    return render(request, 'wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    user_wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    user_wishlist.products.add(product)

    messages.add_message(request, messages.SUCCESS, 'Product successfully added to the wishlist.')

    return redirect('wishlist')


@login_required
def delete_from_wishlist(request, product_id):
    user_wishlist = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    user_wishlist.products.remove(product)

    messages.add_message(request, messages.SUCCESS, 'Product deleted from your wishlist.')

    return redirect('wishlist')
    