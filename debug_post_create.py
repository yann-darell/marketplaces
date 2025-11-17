# -*- coding: utf-8 -*-
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace_core.settings')
django.setup()
from django.test import Client
from django.contrib.auth.models import User
from accounts.models import Profile
from products.models import Category

client = Client()
# create seller
seller = User.objects.create_user(username='dbg_seller', password='testpass')
Profile.objects.get_or_create(user=seller, defaults={'role':'seller'})
client.login(username='dbg_seller', password='testpass')
cat = Category.objects.create(name='DBG')

response = client.post('/products/create/', data={
    'category': cat.id,
    'title': 'DBG Product',
    'description': 'desc',
    'price': '9.99',
    'stock': '5',
    'is_active': 'on'
})
print('Status:', response.status_code)
if hasattr(response, 'context') and response.context:
    form = None
    for v in response.context.values():
        if hasattr(v, 'errors'):
            form = v
            break
    if form is not None:
        print('Form errors:', form.errors)
    else:
        print('No form in context')
else:
    print('No context in response')
