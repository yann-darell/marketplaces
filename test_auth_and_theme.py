#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de test pour vérifier l'authentification et la configuration
"""

import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace_core.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile
from django.test import Client
from django.urls import reverse

print("=" * 70)
print("🧪 Tests d'Authentification et Configuration")
print("=" * 70)

# Test 1: Vérifier les settings
print("\n✓ Test 1: Vérifier les settings d'authentification")
from django.conf import settings
assert settings.LOGIN_URL == 'login', "❌ LOGIN_URL incorrect"
assert settings.LOGIN_REDIRECT_URL == 'dashboard', "❌ LOGIN_REDIRECT_URL incorrect"
assert settings.LOGOUT_REDIRECT_URL == 'home', "❌ LOGOUT_REDIRECT_URL incorrect"
print("   ✅ Settings corrects")

# Test 2: Vérifier les URLs
print("\n✓ Test 2: Vérifier les URLs")
try:
    url_login = reverse('login')
    url_dashboard = reverse('dashboard')
    url_home = reverse('home')
    print(f"   ✅ login: {url_login}")
    print(f"   ✅ dashboard: {url_dashboard}")
    print(f"   ✅ home: {url_home}")
except Exception as e:
    print(f"   ❌ Erreur URL: {e}")

# Test 3: Vérifier les utilisateurs existants
print("\n✓ Test 3: Vérifier les utilisateurs")
users = User.objects.all()
print(f"   ✅ Nombre d'utilisateurs: {users.count()}")
for user in users:
    has_profile = hasattr(user, 'profile')
    print(f"      - {user.username} (admin: {user.is_staff}, profil: {has_profile})")

# Test 4: Tester le flux d'authentification
print("\n✓ Test 4: Simuler le flux d'authentification")
client = Client()

# Créer un utilisateur de test
print("   Création d'un utilisateur de test...")
test_user, created = User.objects.get_or_create(
    username='test_user',
    defaults={
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    }
)

if created:
    test_user.set_password('testpass123')
    test_user.save()
    Profile.objects.create(user=test_user, role='buyer')
    print(f"   ✅ Utilisateur 'test_user' créé")
else:
    print(f"   ⓘ Utilisateur 'test_user' existant utilisé")

# Créer le profil s'il n'existe pas
if created:
    try:
        Profile.objects.create(user=test_user, role='buyer')
    except:
        pass

# Tester la connexion
print("   Test de connexion...")
try:
    login_success = client.login(username='test_user', password='testpass123')
except Exception as e:
    print(f"   ⚠️  Erreur de connexion: {e}")
    login_success = False
if login_success:
    print(f"   ✅ Connexion réussie")
    # Tester la redirection
    response = client.get('/login/', follow=True)
    print(f"   ✅ Session établie")
else:
    print(f"   ❌ Connexion échouée")

# Test 5: Vérifier les fichiers statiques
print("\n✓ Test 5: Vérifier les fichiers CSS")
theme_css = Path('static/css/theme.css')
if theme_css.exists():
    print(f"   ✅ theme.css trouvé ({theme_css.stat().st_size} bytes)")
else:
    print(f"   ❌ theme.css NOT FOUND")

base_html = Path('templates/base.html')
if base_html.exists():
    content = base_html.read_text()
    if 'theme.css' in content:
        print(f"   ✅ theme.css lié dans base.html")
    else:
        print(f"   ❌ theme.css NOT LINKED in base.html")
else:
    print(f"   ❌ base.html NOT FOUND")

# Test 6: Vérifier les variables CSS
print("\n✓ Test 6: Vérifier les variables CSS")
if theme_css.exists():
    theme_content = theme_css.read_text()
    required_vars = [
        '--color-primary-dark',
        '--color-secondary-deep',
        '--color-accent',
        '--color-surface',
        '--color-warm',
        '--color-text-primary',
        '--color-text-secondary',
    ]
    missing = []
    for var in required_vars:
        if var not in theme_content:
            missing.append(var)
    
    if not missing:
        print(f"   ✅ Toutes les variables CSS sont présentes ({len(required_vars)})")
    else:
        print(f"   ❌ Variables manquantes: {missing}")

print("\n" + "=" * 70)
print("✅ Tous les tests de vérification sont terminés!")
print("=" * 70)
print("\n📝 Prochaines étapes:")
print("   1. Redémarrer le serveur Django")
print("   2. Tester la connexion depuis le navigateur")
print("   3. Vérifier que les couleurs s'affichent correctement")
print("   4. Vérifier les redirections d'authentification")
print("\n💡 Commande pour redémarrer:")
print("   python manage.py runserver 0.0.0.0:8000")
print("\n" + "=" * 70)
