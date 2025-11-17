@echo off
REM Script de démarrage rapide pour le serveur Django

echo.
echo ============================================================
echo  Django Marketplace - Démarrage du Serveur
echo ============================================================
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "env\Scripts\activate.bat" (
    echo ERROR: Environnement virtuel non trouvé!
    echo Veuillez créer un environnement virtuel d'abord:
    echo   python -m venv env
    pause
    exit /b 1
)

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call env\Scripts\activate.bat

REM Afficher la version Python
echo Python utilisé:
python --version
echo.

REM Vérifier Django
echo Vérification de la configuration Django...
python manage.py check
if errorlevel 1 (
    echo ERROR: Vérification Django échouée!
    pause
    exit /b 1
)
echo ✓ Configuration Django valide
echo.

REM Afficher les infos de démarrage
echo ============================================================
echo  Serveur prêt à démarrer!
echo ============================================================
echo.
echo URL: http://localhost:8000
echo Admin: http://localhost:8000/admin/
echo Connexion: http://localhost:8000/accounts/login/
echo.
echo Appuyez sur CTRL+C pour arrêter le serveur
echo ============================================================
echo.

REM Démarrer le serveur
python manage.py runserver 0.0.0.0:8000

pause
