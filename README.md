# MyBlog avec Django 🌟

Un blog moderne et élégant développé avec Django, conçu pour démontrer des compétences full-stack et les bonnes pratiques de développement web.

## ✨ Fonctionnalités

- **Articles de blog** avec système CRUD complet
- **Interface responsive** adaptée à tous les appareils
- **Système d'authentification** utilisateur (inscription, connexion, déconnexion)
- **Espace administrateur** Django sur mesure
- **Gestion des commentaires** pour une interaction communautaire
- **Système de catégories** pour organiser le contenu
- **Recherche intuitive** dans les articles
- **Design moderne** avec Bootstrap/CSS personnalisé

## 🛠️ Technologies Utilisées

- **Backend:** Django 4.x, Python 3.x
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap
- **Base de données:** SQLite (développement) / PostgreSQL (production)
- **Autres:** Git, pip, virtualenv

## 🚀 Installation et Démarrage

### Prérequis

- Python 3.8 ou supérieur
- pip
- virtualenv

### Étapes d'installation

1. **Cloner le repository**

```bash
git clone https://github.com/votre-username/MyBlog-with-django.git
cd MyBlog-with-django
```

2. **Créer un environnement virtuel**

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Configurer la base de données**

```bash
python manage.py migrate
```

5. **Créer un superutilisateur**

```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**

```bash
python manage.py runserver
```

7. **Accéder à l'application**  
   Ouvrez votre navigateur à l'adresse: `http://localhost:8000`

## 📦 Structure du Projet

```
MyBlog-with-django/
├── blog/                          # Application principale
│   ├── models.py                  # Modèles de données
│   ├── views.py                   # Logique des vues
│   ├── urls.py                    # Routes de l'application
│   └── templates/                 # Templates HTML
├── static/                        # Fichiers statiques (CSS, JS, images)
├── media/                         # Fichiers uploadés par les utilisateurs
├── manage.py                      # Script de gestion Django
└── requirements.txt               # Dépendances du projet
```

## 🎯 Compétences Démonstrées

- **Architecture MVC/MVT** avec Django
- **Développement full-stack** de A à Z
- **Gestion de base de données** avec l'ORM Django
- **Création d'API RESTful** (si applicable)
- **Sécurité web** (CSRF protection, validation des données)
- **Interface utilisateur responsive**
- **Gestion de version** avec Git
- **Déploiement** et configuration serveur

## 🌐 Déploiement

Ce projet peut être déployé sur diverses plateformes:

- **Heroku** (voir branche `deployment/heroku`)
- **PythonAnywhere**
- **Serveur VPS** avec Nginx + Gunicorn

Instructions détaillées de déploiement disponibles dans DEPLOYMENT.md.

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à:

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committer vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Pusher sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📞 Contact
  
Lien du projet: https://github.com/souleCode/MyBlog-with-django
