from flask_app.config.mysqlconnection import connectToMySQL
# user.py
# model class is called on by the controller to deal with the database
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in users_from_db:
            users.append(cls(u))
        return users

    @classmethod
    def save(cls,data):
        query = "Insert INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        user_id = connectToMySQL('users_schema').query_db(query,data)
        return user_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        print(result)
        #Use class to turn it into a class
        return cls(result[0])

    @classmethod
    def remove(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
