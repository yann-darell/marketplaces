@echo off
REM Script de démarrage du projet Marketplace Django
REM ====================================================

echo.
echo ==================================================
echo  Bienvenue dans le Marketplace Django
echo ==================================================
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "env\Scripts\activate.bat" (
    echo [ERREUR] L'environnement virtuel n'existe pas!
    echo Veuillez créer un environnement virtuel avant de lancer ce script.
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
echo [1/6] Activation de l'environnement virtuel...
call env\Scripts\activate.bat

REM Installer les dépendances
echo.
echo [2/6] Installation des dépendances...
pip install -q -r requirements.txt

REM Afficher les migrations disponibles
echo.
echo [3/6] Vérification des migrations...
python manage.py showmigrations

REM Appliquer les migrations
echo.
echo [4/6] Application des migrations...
python manage.py migrate

REM Collecter les fichiers statiques
echo.
echo [5/6] Collecte des fichiers statiques...
python manage.py collectstatic --noinput

REM Créer les répertoires médias
echo.
echo [6/6] Création des répertoires médias...
if not exist "media" mkdir media
if not exist "media\products" mkdir media\products
if not exist "media\categories" mkdir media\categories
if not exist "media\profiles" mkdir media\profiles
if not exist "media\product_images" mkdir media\product_images

echo.
echo ==================================================
echo  ✓ Installation terminée!
echo ==================================================
echo.
echo Pour créer un superutilisateur (admin):
echo   python manage.py createsuperuser
echo.
echo Pour lancer le serveur de développement:
echo   python manage.py runserver
echo.
echo L'application sera accessible à:
echo   http://127.0.0.1:8000/
echo.
echo L'admin sera accessible à:
echo   http://127.0.0.1:8000/admin/
echo.
pause
