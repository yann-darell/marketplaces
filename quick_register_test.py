# -*- coding: utf-8 -*-
"""
Quick test script to POST to the registration view and ensure no IntegrityError occurs.
"""
import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace_core.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from accounts.models import Profile
import random

client = Client()

username = f"reg_test_{random.randint(1000,9999)}"
password = 'safe_pass_123'
email = f"{username}@example.com"

print('Posting registration for', username)
response = client.post('/accounts/register/', data={
    'username': username,
    'email': email,
    'password': password,
    'password_confirm': password,
    'first_name': 'Test',
    'last_name': 'Reg',
})

print('Response status code:', response.status_code)
# Follow redirects to see final location if any
if response.status_code in (301, 302):
    print('Redirected to:', response['Location'])

# Verify user exists and profile exists
try:
    user = User.objects.get(username=username)
    print('User created:', user.username)
    try:
        profile = user.profile
        print('Profile exists for user:', profile.id)
    except Exception as e:
        print('Profile missing or error:', e)
except Exception as e:
    print('User not created:', e)

print('Done')
