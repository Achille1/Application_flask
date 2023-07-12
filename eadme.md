

### Application Flask pour la gestion des utilisateurs avec MongoDB

Cette application Flask est conçue pour gérer les utilisateurs en utilisant une base de données MongoDB. Elle permet de créer, lire, mettre à jour et supprimer des utilisateurs.

#### Étapes: :rocket:

1. **Coder l'application Flask** : Le code de l'application Flask se trouve dans le fichier `app_flask.py`. Il utilise Flask et Flask-PyMongo pour interagir avec la base de données MongoDB.

2. **Dockeriser l'application** : Utilisez un fichier Dockerfile pour créer une image Docker de l'application Flask. Le Dockerfile peut être configuré pour installer les dépendances et copier les fichiers nécessaires.

3. **Déployer avec Docker Compose et MongoDB** : Utilisez Docker Compose pour déployer l'application Flask avec une base de données MongoDB. Le fichier docker-compose.yml définit les services Flask et MongoDB, en les reliant ensemble.

4. **Ajouter une interface utilisateur MongoDB avec Mongo Express** : En plus de l'application Flask et de MongoDB, vous pouvez ajouter une interface utilisateur pour MongoDB avec Mongo Express. Cela permet de gérer la base de données de manière conviviale.

5. **Bonus : Ajouter un volume de persistance pour la base de données** : Pour assurer la persistance des données, vous pouvez configurer un volume Docker pour stocker les fichiers de la base de données MongoDB. Cela permet de conserver les données même si les conteneurs sont redémarrés.



### Licence

Ce projet est sous licence [MIT](LICENSE).