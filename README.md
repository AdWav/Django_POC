# Django

## installation de l'environnement

#### Command d'exécution pour installer l'environnement de travail :
```bash
./install_django_ubuntu.sh
```

#### Entrer dans l'environnement virtuel
```bash
source ./.venv/bin/activate
```

#### Cloner ce projet (ici en ssh)
```bash
git@github.com:AdWav/Django_Tuto.git
```

#### Installez les packages nécessaires
```bash
pip install -r requirements.txt
```

#### Si serveur de type Mysql / Mariadb , Ajoutez ces packages (de base db.sqlite3) 
Assurez-vous d'avoir le bon type de server, dans le fichier POC_livredor/settings.py
```bash
sudo apt-get install mysql-server mysql-client
```

#### Puis parametrez ce serveur
```bash
sudo mysql_secure_installation
```
liste des paramètres : 
+ Enter current password for root (enter for none) : [enter]
+ Switch to unix_socket authentication: [n]
+ Change the root password : [Y] → Cf emplacement du mot de passe
+ Remove anonymous users ? [Y]
+ Disallow root login remotely ? [n]
+ Remove test Database and access to it ? [Y]
+ Reload privilege table now ? [n]

#### connectez-vous à la DB...
```bash
mysql -u root -p
```

#### ...pour créer la DB
```sql
CREATE DATABASE mabase;
```
#### Activez le server
```bash
python3 manage.py runserver
```

#### Rendez-vous à l'adresse pour vous connecter
```http
http://localhost:8000/admin/
```

#### Test de fonctionnement du projet
```bash
curl -X POST http://127.0.0.1:8000/article/ \
	-H "Content-Type: application/json" \
	-d '{"title":"article_1","article":"test_1"}' \
	-u user_1:user1user
```
