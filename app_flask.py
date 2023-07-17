from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_restx import Api, Resource, fields
import os

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/mydatabase'  # Connexion à la base de données MongoDB
mongo = PyMongo(app)

# Utilisateurs initiaux
init_users = [
    {"name": "John Doe", "email": "john.doe@example.com", "country": "USA", "city": "New York"},
    {"name": "Jane Smith", "email": "jane.smith@example.com", "country": "UK", "city": "London"},
    {"name": "Michael Johnson", "email": "michael.johnson@example.com", "country": "USA", "city": "Los Angeles"},
    {"name": "Emily Davis", "email": "emily.davis@example.com", "country": "Canada", "city": "Toronto"},
    {"name": "William Wilson", "email": "william.wilson@example.com", "country": "USA", "city": "Chicago"},
    {"name": "Sophia Martinez", "email": "sophia.martinez@example.com", "country": "Spain", "city": "Barcelona"},
    {"name": "Matthew Taylor", "email": "matthew.taylor@example.com", "country": "France", "city": "Paris"}
]

# Configuration de l'API
api = Api(app=app, version='1.1', title="Manag's App", description='Mon premier API CRUD en Flask pour la gestion des utilisateurs', validate=True)
ns_user = api.namespace('Infos', description="User's contact")
ns_stay = api.namespace('Stay', description="User's localisation")

# Modèle d'utilisateur
user_model = api.model('User', {
    'name': fields.String(required=True, description='Nom de l\'utilisateur'),
    'email': fields.String(required=True, description='Email de l\'utilisateur')
})

# Modèle de localisation
need_model = api.model('Need', {
    'country': fields.String(required=True, description='Pays de résidence de l\'utilisateur'),
    'city': fields.String(required=True, description='Ville de résidence de l\'utilisateur')
})

@ns_user.route('/users')
class Users(Resource):
    """
    Endpoint pour la gestion des utilisateurs
    """
    def get(self):
        """
        Récupère tous les utilisateurs
        """
        users = mongo.db.users.find()
        user_list = []
        for user in users:
            user['_id'] = str(user['_id'])
            user_list.append(user)
        return jsonify(user_list)

    @ns_user.expect(user_model, validate=True)
    def post(self):
        """
        Crée un nouvel utilisateur
        """
        user_data = request.json
        result = mongo.db.users.insert_one(user_data)
        inserted_id = str(result.inserted_id)
        return jsonify({'message': 'Utilisateur créé avec succès', 'id': inserted_id})

@ns_user.route('/users/<user_id>')
class User(Resource):
    """
    Endpoint pour un utilisateur spécifique
    """
    def get(self, user_id):
        """
        Récupère un utilisateur par son ID
        """
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user)
        else:
            return jsonify({'message': 'Utilisateur non trouvé'})

    @ns_user.expect(user_model, validate=True)
    def put(self, user_id):
        """
        Met à jour un utilisateur
        """
        user_data = request.json
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
        return jsonify({'message': 'Utilisateur mis à jour avec succès'})

    def delete(self, user_id):
        """
        Supprime un utilisateur
        """
        mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return jsonify({'message': 'Utilisateur supprimé avec succès'})

@ns_stay.route('/users')
class StayList(Resource):
    """
    Endpoint pour la gestion des localisations
    """
    def get(self):
        """
        Récupère toutes les localisations
        """
        stays = mongo.db.users.find({}, {'name': 1, 'country': 1, 'city': 1})
        stay_list = []
        for stay in stays:
            stay['_id'] = str(stay['_id'])
            stay_list.append(stay)
        return jsonify(stay_list)

    @ns_stay.expect(need_model, validate=True)
    def post(self):
        """
        Crée une nouvelle localisation
        """
        stay_data = request.json
        result = mongo.db.users.insert_one(stay_data)
        inserted_id = str(result.inserted_id)
        return jsonify({'message': 'Localisation créée avec succès', 'id': inserted_id})

@ns_stay.route('/users/<user_id>')
class Stay(Resource):
    """
    Endpoint pour une localisation spécifique
    """
    def get(self, user_id):
        """
        Récupère la localisation d'un utilisateur par son ID
        """
        stay = mongo.db.users.find_one({'_id': ObjectId(user_id)}, {'name': 1, 'country': 1, 'city': 1})
        if stay:
            stay['_id'] = str(stay['_id'])
            return jsonify(stay)
        else:
            return jsonify({'message': 'Localisation non trouvée'})

    @ns_stay.expect(need_model, validate=True)
    def put(self, user_id):
        """
        Met à jour la localisation d'un utilisateur
        """
        stay_data = request.json
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': stay_data})
        return jsonify({'message': 'Localisation mise à jour avec succès'})

    def delete(self, user_id):
        """
        Supprime la localisation d'un utilisateur
        """
        mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return jsonify({'message': 'Localisation supprimée avec succès'})

if __name__ == '__main__':
    for user in init_users:
        mongo.db.users.insert_one(user)

    # Utilisation de l'adresse IP et du port fournis par Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
