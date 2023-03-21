from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Fields for contact form """
    name = forms.Charfield(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.Emailfield(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.Charfield(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.Charfield(widget=forms.TextArea(attrs={'class': 'form-control', 'placeholder': 'Write your message here!'}))

    class Meta:
        model = Contact
        fields = ('name', 'emial', 'subject', 'message')