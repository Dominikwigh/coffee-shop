from django.shortcuts import render, redirect, reverse 
from .forms import OrderForm
from django.contrib import messages
from bag.contexts import bag_contents
import stripe
from django.conf import settings

# Checkout view
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MmbifEGL49n1U78UdJX0RSh3utAaUqEd9rZUyRIQgTEhXRDBtzd5cqq6Xk02ay7Cq3XHo1hsSMZeIUt4TYXKHhE00dDNzkQb8',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

