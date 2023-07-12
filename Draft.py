
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
# api = Api(app=app, version='1.1', title="Manag's App", description='Mon premier API CRUD en Flask pour la gestion des utilisateurs', validate=True)
# ns_user = api.namespace('Infos', description = "User's contact")
# ns_need = api.namespace('Stay', description = "User's localisation")

# # Modèle d'utilisateur
# user_model = api.model('User', {
#     'name': fields.String(required=True, description='Nom de l\'utilisateur'),
#     'email': fields.String(required=True, description='Email de l\'utilisateur')
# })

# # Définition des endpoints de l'API
# @ns_user.route('/users')
# class Users(Resource):
#     def get(self):
#         users = mongo.db.users.find()
#         user_list = []
#         for user in users:
#             user['_id'] = str(user['_id'])
#             user_list.append(user)
#         return jsonify(user_list)

#     @ns_user.expect(user_model, validate=True)
#     def post(self):
#         name = request.json['name']
#         email = request.json['email']
#         user_data = {'name': name, 'email': email}
#         result = mongo.db.users.insert_one(user_data)
#         inserted_id = str(result.inserted_id)
#         return jsonify({'message': 'Utilisateur créé avec succès', 'id': inserted_id})

# @ns_user.route('/users/<user_id>')
# class User(Resource):
#     def get(self, user_id):
#         user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user:
#             user['_id'] = str(user['_id'])
#             return jsonify(user)
#         else:
#             return jsonify({'message': 'Utilisateur non trouvé'})

#     @ns_user.expect(user_model, validate=True)
#     def put(self, user_id):
#         user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user:
#             name = request.json['name']
#             email = request.json['email']
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

# @ns_need.route("/")
# class Staylist(Resource):
#     def get(self):
#         """
#         returns a list of Needs
#         """
#     def post(self):
#         """
#         Add a new need to the list
#         """
# @ns_need.route("/<string:country>")
# class Stay(Resource):
#     def put(self, stay):
#         """
#         Edits a selected food
#         """
#     def delete(self, stay):
#         """
#     delete a selected food
#     """

# if __name__ == '__main__':
#     for user in init_users:
#         mongo.db.users.insert_one(user)

#     app.run(host='0.0.0.0', port=5000)

