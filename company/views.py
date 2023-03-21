from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm


def contact(request, *args, **kwargs):
    """ Contact page functionality """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            # Send email 
            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(
                request, 'Thank you for contacting us \
                        we will come back to you shortly.')
            # Redirect to home page
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Something went wrong, please try again.'
            )
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

