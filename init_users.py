from pymongo import MongoClient


init_users = [
    {"name": "John Deo", "email": "john@Deo.com"},
    {"name": "Al Smith", "email": "Smith@Jane.com"},
    {"name": "Jean Dupont", "email": "Dupont@Jean.com"}
]


def insert_init_users():
    client = MongoClient('mongodb://db:27017/')
    db = client.mydatabase
    users_collection = db.users
    for user in init_users:
        users_collection.insert_one(user)
    client.close()

if __name__ == '__main__':
    insert_init_users()

