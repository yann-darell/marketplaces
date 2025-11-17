# 🛍️ Marketplace Django - Guide de Lancement

## 📋 Prérequis

- Python 3.8+
- pip (gestionnaire de paquets Python)
- Environnement virtuel Python

## 🚀 Instructions d'Installation et de Lancement

### 1. Activation de l'Environnement Virtuel

```bash
# Windows (PowerShell)
cd c:\Users\User\Desktop\marketpaces
.\env\Scripts\Activate.ps1

# Ou sur CMD
env\Scripts\activate.bat
```

### 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

### 3. Exécution des Migrations

C'est **TRÈS IMPORTANT** d'exécuter les migrations pour créer les tables en base de données:

```bash
# Afficher les migrations qui seront appliquées
python manage.py migrate --plan

# Appliquer toutes les migrations
python manage.py migrate
```

#### Migrations spécifiques par app:

```bash
# Créer les migrations (si nécessaire)
python manage.py makemigrations accounts
python manage.py makemigrations products
python manage.py makemigrations orders
python manage.py makemigrations dashboard

# Appliquer les migrations
python manage.py migrate
```

### 4. Créer un Superutilisateur (Admin)

```bash
python manage.py createsuperuser
```

Suivez les instructions pour entrer:
- Nom d'utilisateur
- Email
- Mot de passe

### 5. Créer les répertoires médias

```bash
# PowerShell
New-Item -ItemType Directory -Force -Path media/products
New-Item -ItemType Directory -Force -Path media/categories
New-Item -ItemType Directory -Force -Path media/profiles
New-Item -ItemType Directory -Force -Path media/product_images
```

### 6. Lancer le serveur de développement

```bash
python manage.py runserver
```

Le serveur sera accessible à: **http://127.0.0.1:8000/**

### 7. Accéder à l'Administration Django

- URL: http://127.0.0.1:8000/admin/
- Utilisez les identifiants du superutilisateur créé précédemment

## 📊 Structure du Projet

```
marketplace_core/
├── accounts/              # Gestion des utilisateurs et profils
│   ├── models.py         # Modèle Profile
│   ├── views.py          # Vues (login, register, profile)
│   ├── forms.py          # Formulaires
│   ├── admin.py          # Admin Django
│   └── urls.py           # URLs
├── products/             # Gestion des produits
│   ├── models.py         # Modèles (Product, Category, ProductImage)
│   ├── views.py          # Vues (liste, détail, créer)
│   ├── forms.py          # Formulaires
│   ├── admin.py          # Admin Django
│   └── urls.py           # URLs
├── orders/               # Gestion des commandes
│   ├── models.py         # Modèles (Order, OrderItem, CartItem)
│   ├── views.py          # Vues (panier, checkout, commandes)
│   ├── forms.py          # Formulaires
│   ├── admin.py          # Admin Django
│   └── urls.py           # URLs
├── dashboard/            # Tableau de bord et avis
│   ├── models.py         # Modèles (Notification, Review)
│   ├── views.py          # Vues (dashboards, avis)
│   ├── forms.py          # Formulaires
│   ├── admin.py          # Admin Django
│   └── urls.py           # URLs
├── marketplace_core/     # Configuration principale
│   ├── settings.py       # Configuration Django
│   ├── urls.py           # URLs principales
│   ├── wsgi.py           # WSGI
│   └── asgi.py           # ASGI
├── templates/            # Fichiers HTML
├── static/               # Fichiers statiques (CSS, JS)
├── media/                # Fichiers médias (images)
├── db.sqlite3            # Base de données
├── manage.py             # Gestionnaire Django
└── requirements.txt      # Dépendances Python
```

## 🗺️ Routes Principales

### Authentification
- `/accounts/register/` - Inscription
- `/accounts/login/` - Connexion
- `/accounts/logout/` - Déconnexion
- `/accounts/profile/` - Mon profil
- `/accounts/become-seller/` - Devenir vendeur

### Produits
- `/products/` - Liste des produits
- `/products/product/<id>/` - Détail du produit
- `/products/create/` - Créer un produit (vendeur)
- `/products/update/<id>/` - Modifier un produit
- `/products/delete/<id>/` - Supprimer un produit
- `/products/categories/` - Lister les catégories
- `/products/category/<id>/` - Produits par catégorie

### Panier et Commandes
- `/orders/cart/` - Voir le panier
- `/orders/add-to-cart/<product_id>/` - Ajouter au panier
- `/orders/remove-from-cart/<item_id>/` - Retirer du panier
- `/orders/checkout/` - Passer la commande
- `/orders/orders/` - Mes commandes
- `/orders/order/<id>/` - Détail de la commande
- `/orders/seller-orders/` - Commandes pour vendeur

### Tableau de Bord
- `/` - Accueil
- `/buyer-dashboard/` - Tableau de bord acheteur
- `/seller-dashboard/` - Tableau de bord vendeur
- `/seller-products/` - Mes produits
- `/review/<product_id>/` - Ajouter un avis
- `/notifications/` - Mes notifications

### Admin
- `/admin/` - Panneau d'administration Django

## 🎯 Fonctionnalités Principales

### Acheteurs
- ✅ Inscription et connexion
- ✅ Parcourir les produits
- ✅ Filtrer et rechercher
- ✅ Ajouter au panier
- ✅ Passer des commandes
- ✅ Voir l'historique des commandes
- ✅ Laisser des avis et notes
- ✅ Gérer le profil

### Vendeurs
- ✅ Créer et gérer des produits
- ✅ Voir les commandes reçues
- ✅ Gérer les catégories
- ✅ Accéder au tableau de bord
- ✅ Voir les statistiques de vente
- ✅ Gérer le profil du magasin

## 📱 Modèles de Données

### Profile (Accounts)
- user (OneToOne User)
- role (buyer/seller)
- store_name
- store_description
- phone_number
- address
- city
- country
- profile_image

### Product (Products)
- seller (FK User)
- category (FK Category)
- title
- description
- price
- stock
- image
- is_active

### Order (Orders)
- buyer (FK User)
- order_number
- total_price
- status
- payment_method
- delivery_address

### Review (Dashboard)
- product (FK Product)
- buyer (FK User)
- rating (1-5)
- comment

## 🔧 Commandes Utiles

```bash
# Créer des migrations
python manage.py makemigrations

# Voir les migrations
python manage.py showmigrations

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Shell Django interactif
python manage.py shell

# Collecter les fichiers statiques
python manage.py collectstatic

# Vérifier les problèmes
python manage.py check

# Lancer les tests
python manage.py test
```

## 🛠️ Déploiement Production

Pour le déploiement en production:

1. Définir `DEBUG = False` dans `settings.py`
2. Ajouter votre domaine à `ALLOWED_HOSTS`
3. Utiliser une base de données PostgreSQL
4. Configurer WhiteNoise pour les fichiers statiques
5. Utiliser Gunicorn: `gunicorn marketplace_core.wsgi`

## 📝 Notes Importantes

- Les **migrations** doivent être appliquées pour que l'application fonctionne
- Les dossiers médias (`media/`) sont créés dynamiquement
- Les dossiers statiques (`static/`) contiennent CSS, JS et images
- L'authentification est requise pour certaines fonctionnalités
- Le rôle "vendeur" doit être assigné dans le profil

## 🐛 Dépannage

### Erreur: "No such table"
```bash
python manage.py migrate
```

### Erreur: "Module not found"
```bash
pip install -r requirements.txt
```

### Images n'affichent pas
- Vérifier le dossier `media/`
- Vérifier que `MEDIA_ROOT` et `MEDIA_URL` sont configurés
- Redémarrer le serveur

### Permissions d'accès
- Vérifier que vous êtes connecté
- Vérifier votre rôle (buyer/seller)
- Vérifier les permissions dans l'admin

## 📞 Support

Pour plus d'informations sur Django: https://docs.djangoproject.com/

---

**Prêt à lancer? Allez-y! 🚀**
