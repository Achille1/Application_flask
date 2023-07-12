import pymongo
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource



app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://mongo:27017/usersdb'

api = Api(app=app, version='1.1', title='My Books Api', description='Mon premier API en Flask ', validate=True)

@api.route('/hello')  #
def get(): 
        return {"hello": "world!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)




####################
from flask import Flask, jsonify, request
from markupsafe import escape
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/mydatabase'  # Connexion à la base de données MongoDB
mongo = PyMongo(app)

init_users = [
    {"id": 1, "name":"John Doe", "email":"john@Doe.com"},
    {"id": 2, "name":"Jane Smith", "email":"Smith@Jane.com"},
    {"id": 3, "name":"Jean Dupont", "email":"Dupont@Jean.com"}
]

@app.before_first_request
def insert_init_users():
    users_collection = mongo.db.users
    for user in init_users:
        users_collection.insert_one(user)

# Route pour obtenir tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        user['_id'] = str(user['_id'])
        user_list.append(user)
    return jsonify(user_list)

# Route pour obtenir un utilisateur par son ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user)
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

# Route pour créer un nouvel utilisateur
@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    user_data = {'name': name, 'email': email}
    result = mongo.db.users.insert_one(user_data)
    return jsonify({'message': 'Utilisateur créé avec succès', 'id': str(result.inserted_id)})

# Route pour mettre à jour un utilisateur
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    if user:
        name = request.json['name']
        email = request.json['email']
        user_data = {'name': name, 'email': email}
        mongo.db.users.update_one({'_id': user_id}, {'$set': user_data})
        return jsonify({'message': 'Utilisateur mis à jour avec succès'})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

# Route pour supprimer un utilisateur
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = mongo.db.users.find_one({'_id': user_id})
    if user:
        mongo.db.users.delete_one({'_id': user_id})
        return jsonify({'message': 'Utilisateur supprimé avec succès'})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)





# app = Flask(__name__)
# app.config['MONGO_URI'] = 'mongodb://db:27017/mydatabase'  # Connexion à la base de données MongoDB
# mongo = PyMongo(app)

# # Utilisateurs initiaux
# init_users = [
#     {"name": "John Doe", "email": "john.doe@example.com"},
#     {"name": "Jane Smith", "email": "jane.smith@example.com"},
#     {"name": "Michael Johnson", "email": "michael.johnson@example.com"},
#     {"name": "Emily Davis", "email": "emily.davis@example.com"},
#     {"name": "William Wilson", "email": "william.wilson@example.com"},
#     {"name": "Sophia Martinez", "email": "sophia.martinez@example.com"},
#     {"name": "Matthew Taylor", "email": "matthew.taylor@example.com"}
# ]

# # Configuration de l'API
# api = Api(app=app, version='1.1', title="Ach's App", description='Mon premier API CRUD en Flask pour la gestion des utilisateurs', validate=True)

# # Définition des endpoints de l'API
# @api.route('/users')
# class Users(Resource):
#     def get(self):
#         users = mongo.db.users.find()
#         user_list = []
#         for user in users:
#             user['_id'] = str(user['_id'])
#             user_list.append(user)
#         return jsonify(user_list)

#     def post(self):
#         name = request.json['name']
#         email = request.json['email']
#         user_data = {'name': name, 'email': email}
#         result = mongo.db.users.insert_one(user_data)
#         inserted_id = str(result.inserted_id)
#         return jsonify({'message': 'Utilisateur créé avec succès', 'id': inserted_id})


# @api.route('/users/<user_id>')
# class User(Resource):
#     def get(self, user_id):
#         user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user:
#             user['_id'] = str(user['_id'])
#             return jsonify(user)
#         else:
#             return jsonify({'message': 'Utilisateur non trouvé'})

#     def put(self, user_id):
#         user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user:
#             name = request.json.get('name', user['name'])
#             email = request.json.get('email', user['email'])
#             user_data = {'name': name, 'email': email}
#             mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
#             return jsonify({'message': 'Utilisateur mis à jour avec succès'})
#         else:
#             return jsonify({'message': 'Utilisateur non trouvé'})

#     def delete(self, user_id):
#         user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user:
#             mongo.db.users.delete_one({'_id': ObjectId(user_id)})
#             return jsonify({'message': 'Utilisateur supprimé avec succès'})
#         else:
#             return jsonify({'message': 'Utilisateur non trouvé'})


# if __name__ == '__main__':
#     for user in init_users:
#         mongo.db.users.insert_one(user)

#     app.run(host='0.0.0.0', port=5000)


#************************ 1 **************************
######################################################
