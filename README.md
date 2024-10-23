# Django

## installation de l'environnement

### Création d'un Script Bash (`install_django_ubuntu.sh`) pour installer l'environnement de travail à son exécution :

#### Création du fichier de destination
touch install_django_ubuntu.sh

#### Ajout du contenu au fichier 

cat << 'EOF' > install_django_ubuntu.sh
```bash
#!/bin/bash

# Installation d'un environnement de travail Python Django sur Ubuntu

# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation de Python et des outils nécessaires
sudo apt install python3 python3-pip python3-venv -y

# Création d'un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installation de Django et des outils nécessaires 
pip install django djangorestframework pygments
##### pygments is used for the code highlitghting

# Vérification de l'installation
django-admin --version

# Création d'un projet Django
django-admin startproject monprojet
cd monprojet

# Lancement du serveur de développement
python manage.py runserver

# Note : N'oubliez pas d'activer votre environnement virtuel à chaque utilisation
# avec la commande : source .venv/bin/activate
```

# Ajout manuel de datas
http -a admin:waadwaad POST htto://127.0.0.1:8000/snippets/ code="print(message)"

