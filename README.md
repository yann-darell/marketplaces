# 🛍️ Marketplace Django - Plateforme E-commerce Complète

## 📖 Vue d'ensemble

Marketplace est une plateforme e-commerce Django complète permettant aux acheteurs et vendeurs de se connecter, consulter des produits, passer des commandes et gérer leurs magasins. Le projet est 100% fonctionnel avec authentification, gestion des profils, panier d'achat, système de commandes et bien plus.

---

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8+
- pip
- Environnement virtuel activé

### Installation Automatique (Recommandée)

#### Windows (PowerShell)
```powershell
# Exécuter le script de setup
.\setup.ps1
```

#### Windows (CMD)
```cmd
setup.bat
```

### Installation Manuelle

```bash
# 1. Activer l'environnement virtuel
.\env\Scripts\Activate.ps1  # PowerShell
# ou
env\Scripts\activate.bat     # CMD

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Appliquer les migrations
python manage.py migrate

# 4. Créer un superutilisateur
python manage.py createsuperuser

# 5. Créer les dossiers médias
mkdir media\products media\categories media\profiles media\product_images

# 6. Lancer le serveur
python manage.py runserver
```

### Accéder à l'Application
- **Site Principal**: http://127.0.0.1:8000/
- **Admin Django**: http://127.0.0.1:8000/admin/

---

## 📊 Structure du Projet

```
marketplace_core/
│
├── accounts/                    # Gestion des utilisateurs
│   ├── models.py               # Profile, roles (buyer/seller)
│   ├── views.py                # Registration, login, profile
│   ├── forms.py                # UserForm, ProfileForm, etc.
│   ├── admin.py                # Admin configuration
│   ├── urls.py                 # Routes
│   └── signals.py              # Auto-create profile
│
├── products/                   # Gestion des produits
│   ├── models.py               # Product, Category, ProductImage
│   ├── views.py                # Product list, detail, CRUD
│   ├── forms.py                # ProductForm, CategoryForm
│   ├── admin.py                # Admin configuration
│   └── urls.py                 # Routes
│
├── orders/                     # Gestion des commandes
│   ├── models.py               # Order, OrderItem, CartItem
│   ├── views.py                # Cart, Checkout, Orders
│   ├── forms.py                # CheckoutForm, CartItemForm
│   ├── admin.py                # Admin configuration
│   └── urls.py                 # Routes
│
├── dashboard/                  # Tableau de bord
│   ├── models.py               # Notification, Review
│   ├── views.py                # Dashboards, reviews
│   ├── forms.py                # ReviewForm
│   ├── admin.py                # Admin configuration
│   └── urls.py                 # Routes
│
├── marketplace_core/           # Configuration principale
│   ├── settings.py             # Configuration Django
│   ├── urls.py                 # URLs globales
│   ├── wsgi.py                 # WSGI
│   └── asgi.py                 # ASGI
│
├── templates/                  # Fichiers HTML (18 templates)
│   ├── base.html               # Template de base
│   ├── dashboard/              # Accueil, dashboards
│   ├── accounts/               # Login, register, profil
│   ├── products/               # Produits, catégories
│   └── orders/                 # Panier, commandes
│
├── static/                     # CSS, JS, images
├── media/                      # Images produits (généré)
├── db.sqlite3                  # Base de données
├── manage.py                   # Gestionnaire Django
├── requirements.txt            # Dépendances
├── setup.bat                   # Setup Windows (CMD)
├── setup.ps1                   # Setup Windows (PowerShell)
└── SETUP_INSTRUCTIONS.md       # Instructions détaillées
```

---

## 🔑 Modèles de Données

### Profile (Accounts)
```python
- user (OneToOne)
- role (buyer/seller)
- store_name, store_description
- phone_number, address, city, country
- profile_image, is_verified
- created_at, updated_at
```

### Product (Products)
```python
- seller (ForeignKey User)
- category (ForeignKey Category)
- title, description
- price, stock
- image, is_active
- created_at, updated_at
```

### Order (Orders)
```python
- buyer (ForeignKey User)
- order_number (unique)
- total_price, status
- payment_method
- delivery_address, phone_number
- created_at, updated_at
```

### OrderItem (Orders)
```python
- order (ForeignKey)
- product (ForeignKey)
- quantity, price
```

### CartItem (Orders)
```python
- user (ForeignKey)
- product (ForeignKey)
- quantity, added_at
- unique_together: (user, product)
```

### Review (Dashboard)
```python
- product (ForeignKey)
- buyer (ForeignKey)
- rating (1-5)
- comment, created_at
```

### Notification (Dashboard)
```python
- user (ForeignKey)
- title, message
- notification_type
- is_read, created_at
```

---

## 🗺️ Routes et Endpoints

### Authentification
| Route | Méthode | Description |
|-------|---------|-------------|
| `/accounts/register/` | GET/POST | Inscription utilisateur |
| `/accounts/login/` | GET/POST | Connexion |
| `/accounts/logout/` | GET | Déconnexion |
| `/accounts/profile/` | GET/POST | Mon profil (authentifié) |
| `/accounts/become-seller/` | GET/POST | Devenir vendeur (authentifié) |

### Produits
| Route | Méthode | Description |
|-------|---------|-------------|
| `/products/` | GET | Liste les produits |
| `/products/product/<id>/` | GET | Détail d'un produit |
| `/products/create/` | GET/POST | Créer un produit (vendeur) |
| `/products/update/<id>/` | GET/POST | Modifier un produit (vendeur) |
| `/products/delete/<id>/` | POST | Supprimer un produit (vendeur) |
| `/products/categories/` | GET | Lister les catégories |
| `/products/category/<id>/` | GET | Produits d'une catégorie |

### Panier et Commandes
| Route | Méthode | Description |
|-------|---------|-------------|
| `/orders/cart/` | GET | Voir le panier |
| `/orders/add-to-cart/<id>/` | POST | Ajouter au panier |
| `/orders/remove-from-cart/<id>/` | POST | Retirer du panier |
| `/orders/checkout/` | GET/POST | Passer une commande |
| `/orders/orders/` | GET | Mes commandes |
| `/orders/order/<id>/` | GET | Détail d'une commande |
| `/orders/seller-orders/` | GET | Commandes reçues (vendeur) |

### Tableau de Bord
| Route | Méthode | Description |
|-------|---------|-------------|
| `/` | GET | Accueil |
| `/buyer-dashboard/` | GET | Tableau de bord acheteur |
| `/seller-dashboard/` | GET | Tableau de bord vendeur |
| `/seller-products/` | GET | Mes produits (vendeur) |
| `/review/<id>/` | GET/POST | Ajouter un avis |
| `/notifications/` | GET/POST | Mes notifications |

### Admin
| Route | Méthode | Description |
|-------|---------|-------------|
| `/admin/` | GET | Panneau d'administration |

---

## 👤 Rôles et Permissions

### Acheteur (Buyer)
✅ Parcourir les produits  
✅ Filtrer et rechercher  
✅ Ajouter au panier  
✅ Passer des commandes  
✅ Voir l'historique des commandes  
✅ Laisser des avis  
✅ Recevoir des notifications  

### Vendeur (Seller)
✅ Créer et gérer des produits  
✅ Voir les commandes reçues  
✅ Gérer les catégories  
✅ Accéder au tableau de bord  
✅ Voir les statistiques de vente  
✅ Consulter les avis des clients  

---

## 🎯 Fonctionnalités Principales

### Authentification & Profils
- ✅ Système d'inscription complet
- ✅ Connexion/Déconnexion sécurisée
- ✅ Profils utilisateur détaillés
- ✅ Rôles (Acheteur/Vendeur)
- ✅ Auto-création de profil à l'inscription

### Gestion des Produits
- ✅ CRUD complet (Create, Read, Update, Delete)
- ✅ Catégories de produits
- ✅ Images multiples par produit
- ✅ Système d'inventaire
- ✅ Produits actif/inactif

### Panier d'Achat
- ✅ Ajouter/retirer du panier
- ✅ Gestion des quantités
- ✅ Calcul du total
- ✅ Sauvegarde de la session

### Système de Commandes
- ✅ Checkout complet
- ✅ Génération d'ordre unique
- ✅ Statuts de commande
- ✅ Détails de livraison
- ✅ Méthodes de paiement

### Système d'Avis
- ✅ Notes (1-5 étoiles)
- ✅ Commentaires
- ✅ Moyenne des avis
- ✅ Un avis par client/produit

### Tableaux de Bord
- ✅ Dashboard acheteur
- ✅ Dashboard vendeur complet
- ✅ Statistiques de vente
- ✅ Liste des commandes
- ✅ Notifications

---

## 🛠️ Commandes Utiles

### Migrations
```bash
# Créer les migrations
python manage.py makemigrations

# Voir l'état des migrations
python manage.py showmigrations

# Appliquer les migrations
python manage.py migrate

# Afficher le plan des migrations
python manage.py migrate --plan
```

### Administration
```bash
# Créer un superutilisateur
python manage.py createsuperuser

# Shell Django interactif
python manage.py shell

# Vérifier les problèmes
python manage.py check
```

### Fichiers Statiques
```bash
# Collecter les fichiers statiques
python manage.py collectstatic

# Collecter sans confirmation
python manage.py collectstatic --noinput
```

### Serveur
```bash
# Lancer le serveur de développement
python manage.py runserver

# Lancer sur un port spécifique
python manage.py runserver 8080

# Lancer sur toutes les interfaces
python manage.py runserver 0.0.0.0:8000
```

---

## 🔐 Sécurité

### Points à Configurer Avant Production

1. **Settings.py**
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['votre-domaine.com']
   SECRET_KEY = 'générer-une-nouvelle-clé'
   ```

2. **HTTPS**
   ```python
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

3. **Base de Données**
   - Passer de SQLite à PostgreSQL
   - Configurer un serveur dédie

4. **Fichiers Statiques**
   - Utiliser WhiteNoise ou CDN
   - Configurer CloudFront/S3

5. **Email**
   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'
   EMAIL_PORT = 587
   ```

---

## 📦 Dépendances

```
Django==5.2.8
Pillow==12.0.0
python-decouple==3.8
gunicorn==23.0.0
dj-database-url==3.0.1
whitenoise==6.11.0
sqlparse==0.5.3
```

---

## 🐛 Dépannage

### Erreur: "No such table"
```bash
python manage.py migrate
```

### Erreur: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Images n'affichent pas
- Vérifier le dossier `media/`
- Vérifier les permissions
- Redémarrer le serveur

### Migrations en conflit
```bash
# Afficher l'état
python manage.py showmigrations

# Simuler l'application
python manage.py migrate --plan

# Appliquer correctement
python manage.py migrate
```

---

## 📝 Templates Créés

1. **base.html** - Template de base avec navbar
2. **home.html** - Accueil
3. **login.html** - Connexion
4. **register.html** - Inscription
5. **profile.html** - Profil utilisateur
6. **become_seller.html** - Devenir vendeur
7. **product_list.html** - Liste des produits
8. **product_detail.html** - Détail d'un produit
9. **product_form.html** - Créer/modifier un produit
10. **cart.html** - Panier d'achat
11. **checkout.html** - Passer une commande
12. **order_list.html** - Mes commandes
13. **order_detail.html** - Détail d'une commande
14. **buyer_dashboard.html** - Tableau de bord acheteur
15. **seller_dashboard.html** - Tableau de bord vendeur
16. **seller_products.html** - Mes produits
17. **add_review.html** - Ajouter un avis
18. **notifications.html** - Notifications
19. **category_list.html** - Liste des catégories
20. **category_products.html** - Produits par catégorie
21. **seller_orders.html** - Commandes du vendeur

---

## 🚀 Déploiement Production

### Avec Gunicorn et Nginx

```bash
# Installer Gunicorn
pip install gunicorn

# Lancer avec Gunicorn
gunicorn marketplace_core.wsgi:application --workers 4 --bind 0.0.0.0:8000

# Configurer Nginx (reverse proxy)
# Fichier: /etc/nginx/sites-available/marketplace
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

### Avec Docker

```dockerfile
FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "marketplace_core.wsgi:application", "--bind", "0.0.0.0:8000"]
```

---

## 📚 Documentation Additionnelle

- [Django Officiel](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Pillow](https://python-pillow.org/)

---

## 📞 Support et Aide

Pour plus d'informations ou en cas de problème:
1. Consultez `SETUP_INSTRUCTIONS.md`
2. Vérifiez les migrations: `python manage.py showmigrations`
3. Exécutez le check: `python manage.py check`
4. Consultez les logs Django

---

## 📄 Licence

Ce projet est fourni à titre d'exemple éducatif.

---

**Prêt à lancer votre marketplace? 🚀**

```bash
# Activation de l'environnement
.\env\Scripts\Activate.ps1

# Lancer le serveur
python manage.py runserver

# Visiter http://127.0.0.1:8000/
```

Bon shopping! 🛍️
