# 🚀 DÉMARRAGE RAPIDE - Marketplace Django

## ⚡ En 5 minutes

### 1️⃣ Activer l'environnement virtuel

```powershell
# PowerShell
.\env\Scripts\Activate.ps1

# ou CMD
env\Scripts\activate.bat
```

### 2️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Appliquer les migrations
```bash
python manage.py migrate
```

### 4️⃣ Créer un admin
```bash
python manage.py createsuperuser
```

### 5️⃣ Lancer le serveur
```bash
python manage.py runserver
```

### ✅ C'est fait!
- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

## 📋 Checklist de Démarrage

- ✅ Environnement virtuel activé
- ✅ Dépendances installées (`pip install -r requirements.txt`)
- ✅ Migrations appliquées (`python manage.py migrate`)
- ✅ Superuser créé (`python manage.py createsuperuser`)
- ✅ Dossiers médias créés (`mkdir media/...`)
- ✅ Serveur lancé (`python manage.py runserver`)

---

## 🎯 Premiers Pas

### Créer un Compte Acheteur
1. Aller à http://127.0.0.1:8000/accounts/register/
2. Remplir le formulaire
3. Se connecter

### Devenir Vendeur
1. Aller à http://127.0.0.1:8000/accounts/profile/
2. Cliquer sur "Devenir Vendeur"
3. Remplir les infos du magasin

### Créer un Produit (en tant que vendeur)
1. Aller à http://127.0.0.1:8000/products/create/
2. Remplir le formulaire
3. Cliquer sur "Créer"

### Acheter un Produit
1. Parcourir les produits
2. Ajouter au panier
3. Aller au panier
4. Passer la commande

---

## 🔧 Problèmes Courants

### Erreur: "No such table"
```bash
python manage.py migrate
```

### Erreur: "Module not found"
```bash
pip install -r requirements.txt
```

### Port 8000 déjà utilisé
```bash
python manage.py runserver 8080
```

### Réinitialiser la base de données
```bash
# ⚠️ ATTENTION: Cela supprimera tous les données!
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Documentation Complète

Voir `SETUP_INSTRUCTIONS.md` pour:
- Installation détaillée
- Structure du projet
- Tous les endpoints
- Dépannage avancé
- Déploiement production

---

## 🎓 Structure Basique

```
Marketplace
├── Acheteurs → Voir produits → Panier → Commande
└── Vendeurs → Créer produits → Voir commandes → Ventes
```

---

## 📞 Support Rapide

| Problème | Solution |
|----------|----------|
| Pas de produits | Créer un compte vendeur et ajouter des produits |
| Pas de catégories | Aller à l'admin pour ajouter des catégories |
| Images ne s'affichent pas | Créer les dossiers `media/` |
| Données perdues | Réinitialiser la base de données |

---

## ✨ Fonctionnalités Déjà Disponibles

✅ Authentification complète  
✅ Gestion des profils  
✅ CRUD des produits  
✅ Système de panier  
✅ Passages de commandes  
✅ Système d'avis  
✅ Tableaux de bord  
✅ Admin Django  
✅ 20+ templates  
✅ Migrations prêtes  

---

**C'est prêt! Bon développement! 🚀**
