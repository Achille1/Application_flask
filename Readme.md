# Application Flask pour la gestion des utilisateurs et de la localisation

Une petite application Flask (Python) pour gérer des utilisateurs et leurs localisations associés à une base de données MongoDB.

## Fonctionnalités :  :dart:

- Gestion des utilisateurs : :one:
    - Récupérer tous les utilisateurs
    - Récupérer un utilisateur par son ID
    - Créer un nouvel utilisateur
    - Mettre à jour un utilisateur
    - Supprimer un utilisateur

- Gestion de la localisation : :two:
    - Récupérer toutes les localisations des utilisateurs
    - Récupérer la localisation d'un utilisateur par son ID
    - Créer une nouvelle localisation pour un utilisateur
    - Mettre à jour la localisation d'un utilisateur
    - Supprimer la localisation d'un utilisateur

## Étapes: :zap:

1. **Coder l'application Flask** : Le code de l'application Flask se trouve dans le fichier `app_flask.py`. Il utilise Flask et Flask-PyMongo pour interagir avec la base de données MongoDB.

2. **Dockeriser l'application** : Utilisez un fichier Dockerfile pour créer une image Docker de l'application Flask. Le Dockerfile peut être configuré pour installer les dépendances et copier les fichiers nécessaires.

3. **Déployer avec Docker Compose et MongoDB** : Utilisez Docker Compose pour déployer l'application Flask avec une base de données MongoDB. Le fichier docker-compose.yml définit les services Flask et MongoDB, en les reliant ensemble.

4. **Ajouter une interface utilisateur MongoDB avec Mongo Express** : En plus de l'application Flask et de MongoDB, vous pouvez ajouter une interface utilisateur pour MongoDB avec Mongo Express. Cela permet de gérer la base de données de manière conviviale.

5. **Ajouter un volume de persistance pour la base de données** : Pour assurer la persistance des données, vous pouvez configurer un volume Docker pour stocker les fichiers de la base de données MongoDB. Cela permet de conserver les données même si les conteneurs sont redémarrés.


## Installation : :rocket:

1. Clonez ce dépôt sur votre machine locale :

```shell
    git clone https://github.com/Achille1/Application_flask.git
```

### Licence

Ce projet est sous licence [MIT](LICENSE).