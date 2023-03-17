from django.shortcuts import render, redirect, reverse 
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
        'stripe_public_key': 'pk_test_51MmbifEGL49n1U78UdJX0RSh3utAaUqEd9rZUyRIQgTEhXRDBtzd5cqq6Xk02ay7Cq3XHo1hsSMZeIUt4TYXKHhE00dDNzkQb8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

