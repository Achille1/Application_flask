from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://db:27017/mydatabase'  # Connexion à la base de données MongoDB
mongo = PyMongo(app)

# Utilisateurs initiaux
init_users = [
    {"name": "John Deo", "email": "john@Deo.com"},
    {"name": "Al Smith", "email": "Smith@Jane.com"},
    {"name": "Jean Dupont", "email": "Dupont@Jean.com"}
]


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
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
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
    inserted_id = str(result.inserted_id)
    return jsonify({'message': 'Utilisateur créé avec succès', 'id': inserted_id})

# Route pour mettre à jour un utilisateur
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user:
        name = request.json.get('name', user['name'])
        email = request.json.get('email', user['email'])
        user_data = {'name': name, 'email': email}
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
        return jsonify({'message': 'Utilisateur mis à jour avec succès'})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

# Route pour supprimer un utilisateur
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    if user:
        mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        return jsonify({'message': 'Utilisateur supprimé avec succès'})
    else:
        return jsonify({'message': 'Utilisateur non trouvé'})

if __name__ == '__main__':
    for user in init_users:
        mongo.db.users.insert_one(user)

    app.run(host='0.0.0.0', port=5000)


