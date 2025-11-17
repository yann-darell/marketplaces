from django import forms
from .models import Order, CartItem
import uuid


class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }


class CheckoutForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[
            ('credit_card', 'Carte de crédit'),
            ('mobile_money', 'Mobile Money'),
            ('bank_transfer', 'Virement bancaire'),
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )
    delivery_address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Adresse de livraison'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'})
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'payment_method', 'delivery_address', 'phone_number']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
