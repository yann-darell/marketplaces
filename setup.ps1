# Script de démarrage du projet Marketplace Django (PowerShell)
# ============================================================

Write-Host ""
Write-Host "=================================================="
Write-Host "  Bienvenue dans le Marketplace Django" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""

# Vérifier si l'environnement virtuel existe
if (-not (Test-Path "env\Scripts\Activate.ps1")) {
    Write-Host "[ERREUR] L'environnement virtuel n'existe pas!" -ForegroundColor Red
    Write-Host "Veuillez créer un environnement virtuel avant de lancer ce script."
    exit 1
}

# Activer l'environnement virtuel
Write-Host "[1/6] Activation de l'environnement virtuel..." -ForegroundColor Cyan
& env\Scripts\Activate.ps1

# Installer les dépendances
Write-Host ""
Write-Host "[2/6] Installation des dépendances..." -ForegroundColor Cyan
pip install -q -r requirements.txt

# Afficher les migrations disponibles
Write-Host ""
Write-Host "[3/6] Vérification des migrations..." -ForegroundColor Cyan
python manage.py showmigrations

# Appliquer les migrations
Write-Host ""
Write-Host "[4/6] Application des migrations..." -ForegroundColor Cyan
python manage.py migrate

# Collecter les fichiers statiques
Write-Host ""
Write-Host "[5/6] Collecte des fichiers statiques..." -ForegroundColor Cyan
python manage.py collectstatic --noinput

# Créer les répertoires médias
Write-Host ""
Write-Host "[6/6] Création des répertoires médias..." -ForegroundColor Cyan
@("media", "media\products", "media\categories", "media\profiles", "media\product_images") | ForEach-Object {
    if (-not (Test-Path $_)) {
        New-Item -ItemType Directory -Force -Path $_ | Out-Null
    }
}

Write-Host ""
Write-Host "=================================================="
Write-Host "  ✓ Installation terminée!" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Pour créer un superutilisateur (admin):" -ForegroundColor Yellow
Write-Host "  python manage.py createsuperuser"
Write-Host ""
Write-Host "Pour lancer le serveur de développement:" -ForegroundColor Yellow
Write-Host "  python manage.py runserver"
Write-Host ""
Write-Host "L'application sera accessible à:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:8000/"
Write-Host ""
Write-Host "L'admin sera accessible à:" -ForegroundColor Cyan
Write-Host "  http://127.0.0.1:8000/admin/"
Write-Host ""
