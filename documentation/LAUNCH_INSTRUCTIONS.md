# 🎬 INSTRUCTIONS DE LANCEMENT - Marketplace Django

## ✅ ÉTAT ACTUEL

La base de données a été initialisée avec succès! ✨

```
✅ 35+ migrations appliquées
✅ Toutes les tables créées
✅ Structure complète en place
✅ Prêt à l'usage
```

---

## 🚀 DÉMARRAGE IMMÉDIAT

### Étape 1️⃣: Activer l'environnement virtuel

**PowerShell:**
```powershell
.\env\Scripts\Activate.ps1
```

**CMD:**
```cmd
env\Scripts\activate.bat
```

### Étape 2️⃣: Créer un superutilisateur (Admin)

```bash
python manage.py createsuperuser
```

Entrez:
- Username: `admin`
- Email: `admin@marketplace.local`
- Password: `votre-mot-de-passe-secure`

### Étape 3️⃣: Lancer le serveur

```bash
python manage.py runserver
```

### Étape 4️⃣: Accéder à l'application

Ouvrez votre navigateur et allez à:

🌐 **Site Principal**: http://127.0.0.1:8000/  
🔐 **Admin Panel**: http://127.0.0.1:8000/admin/

---

## 📝 PREMIERS ACTIONS

### Dans l'Admin (http://127.0.0.1:8000/admin/)

1. **Ajouter des catégories de produits**
   - Aller à: Products → Categories
   - Cliquer sur "Add Category"
   - Ajouter: "Électronique", "Vêtements", "Livres", etc.

2. **Vérifier les profils**
   - Aller à: Accounts → Profiles
   - Voir les profils créés automatiquement

### Sur le Site Principal

1. **S'inscrire comme acheteur**
   - Cliquer sur "Inscription"
   - Remplir le formulaire
   - Vous serez automatiquement acheteur

2. **S'inscrire comme vendeur**
   - Créer un nouveau compte
   - Aller à: Mon Profil
   - Cliquer sur "Devenir Vendeur"
   - Remplir les infos du magasin

3. **Créer des produits** (en tant que vendeur)
   - Aller à: Créer un Produit
   - Remplir le formulaire
   - Ajouter une image
   - Cliquer sur "Créer"

4. **Acheter des produits** (en tant qu'acheteur)
   - Parcourir les produits
   - Ajouter au panier
   - Aller au panier
   - Passer la commande

---

## 🗺️ NAVIGATION PRINCIPALE

### Acheteur
```
Accueil
├── Parcourir Produits
├── Ajouter au Panier
├── Passer une Commande
├── Voir Mes Commandes
├── Laisser des Avis
└── Mon Dashboard
```

### Vendeur
```
Accueil
├── Créer un Produit
├── Gérer Mes Produits
├── Voir Mes Commandes
├── Consulter les Avis
└── Dashboard Vendeur
```

---

## 📊 ENDPOINTS UTILES

| Page | URL | Rôle |
|------|-----|------|
| Accueil | `/` | Tous |
| Produits | `/products/` | Tous |
| Panier | `/orders/cart/` | Acheteur |
| Mes Commandes | `/orders/orders/` | Acheteur |
| Créer Produit | `/products/create/` | Vendeur |
| Dashboard Vendeur | `/seller-dashboard/` | Vendeur |
| Admin | `/admin/` | Admin |

---

## 🎯 CHECKLIST DE VÉRIFICATION

Avant de commencer à utiliser:

- [ ] Environnement activé
- [ ] Serveur lancé (`python manage.py runserver`)
- [ ] Admin créé (`python manage.py createsuperuser`)
- [ ] Accès à http://127.0.0.1:8000/ ✅
- [ ] Accès à http://127.0.0.1:8000/admin/ ✅
- [ ] Catégories créées dans l'admin
- [ ] Compte acheteur créé
- [ ] Compte vendeur créé (devenir vendeur)
- [ ] Produits créés (en tant que vendeur)
- [ ] Achat testé (en tant qu'acheteur)

---

## 🔧 COMMANDES UTILES

```bash
# Voir l'état des migrations
python manage.py showmigrations

# Shell Django interactif
python manage.py shell

# Vérifier les erreurs
python manage.py check

# Créer un nouvel admin
python manage.py createsuperuser

# Collecte des statics
python manage.py collectstatic --noinput

# Réinitialiser la base
# ⚠️ ATTENTION: Détruit toutes les données!
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📋 STRUCTURE DES MIGRATIONS

Les migrations appliquées incluent:

✅ **Accounts**
- Profile (user, role, store info, etc)

✅ **Products**
- Product (titre, description, prix, stock)
- Category (catégories de produits)
- ProductImage (images supplémentaires)

✅ **Orders**
- Order (commandes avec statut)
- OrderItem (articles dans la commande)
- CartItem (articles dans le panier)

✅ **Dashboard**
- Review (avis et évaluations)
- Notification (notifications utilisateur)

---

## 🎓 CAS D'USAGE

### Cas 1: Acheteur Simple
```
1. S'inscrire
2. Parcourir les produits
3. Ajouter au panier
4. Passer une commande
5. Voir l'historique
```

### Cas 2: Vendeur
```
1. S'inscrire
2. Aller à Mon Profil → Devenir Vendeur
3. Remplir les infos du magasin
4. Créer des produits
5. Voir les commandes reçues
```

### Cas 3: Admin
```
1. Créer des catégories
2. Gérer les utilisateurs
3. Modérer les contenus
4. Voir les statistiques
```

---

## 🐛 DÉPANNAGE RAPIDE

### Erreur "Port 8000 occupé"
```bash
python manage.py runserver 8080
# ou tuer le processus
lsof -ti:8000 | xargs kill -9
```

### Oublié le mot de passe admin
```bash
python manage.py changepassword admin
```

### Besoin de réinitialiser
```bash
# Sauvegarder les données d'abord!
# Puis:
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Images ne s'affichent pas
```bash
# Créer les dossiers
mkdir media
mkdir media\products
mkdir media\categories
mkdir media\profiles
mkdir media\product_images
```

---

## 📞 SUPPORT

Pour des problèmes:

1. **Consultez SETUP_INSTRUCTIONS.md** - Documentation complète
2. **Consultez QUICKSTART.md** - Guide rapide
3. **Consultez README.md** - Guide complet
4. **Exécutez `python manage.py check`** - Vérifier les erreurs

---

## ✨ PROCHAINES ÉTAPES

Une fois lancé:

1. **Tester les fonctionnalités**
   - Créer des comptes
   - Créer des produits
   - Passer des commandes
   - Laisser des avis

2. **Personnaliser**
   - Modifier les templates
   - Ajouter des styles
   - Ajouter des fonctionnalités

3. **Optimiser**
   - Ajouter des indexes DB
   - Mettre en cache
   - Optimiser les requêtes

4. **Déployer**
   - Configurer production
   - Ajouter HTTPS
   - Configurer un serveur dédié

---

## 🎉 VOUS ÊTES PRÊT!

```
╔══════════════════════════════════════╗
║  Marketplace Django est Prêt! 🎉   ║
║                                      ║
║  ✅ Tous les modèles créés          ║
║  ✅ Toutes les migrations appliquées ║
║  ✅ Admin configuré                  ║
║  ✅ Prêt à l'usage                  ║
║                                      ║
║  Lancez: python manage.py runserver ║
║  Visitez: http://127.0.0.1:8000/   ║
╚══════════════════════════════════════╝
```

**Bon shopping! 🛍️**
