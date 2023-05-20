from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N9gETBXRfaz1sT29UxcI46996Ito0I6KX9iCih5w85Usy9ODKhhduTgufK2EwLJiNXmVsF47QaX9wmbt3OaFvDy00KYNh2hjC',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
    