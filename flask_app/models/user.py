
from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import score
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.name = data['name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']


# ===================== RETURNING LIST OF ALL USERS
    @classmethod
    def get_all(cls):
        query = '''
            SELECT *
            FROM users;
        '''
        results = connectToMySQL(DATABASE).query_db(query)    
        all_users = []
        if results:
            for row in results:
                all_users.append(cls(row))
        return all_users

# ===================== RETURNING USER BY ID
    @classmethod
    def get_by_id(cls, data):
        query = '''
            SELECT *
            FROM users
            WHERE id = %(id)s;
        '''
        
        results =  connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])

# ===================== RETURNING USER BY EMAIL
    @classmethod
    def get_by_email(cls, data):
        query = '''
            SELECT *
            FROM users
            WHERE email = %(email)s;
        '''

        results =  connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])

# ===================== RETURNING USER BY username
    @classmethod
    def get_by_username(cls, data):
        query = '''
            SELECT *
            FROM users
            WHERE username = %(username)s;
        '''

        results =  connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1 :
            return False
        return cls(results[0])

# ===================== CREATING A USER AND RETURNING THE ID
    @classmethod
    def create(cls, data):
        query = '''
            INSERT INTO users (name, username, email, password)
            VALUES (%(name)s, %(username)s, %(email)s, %(password)s);
        '''
        user_id_new = connectToMySQL(DATABASE).query_db(query, data)
        score.Score.create({'user_id':user_id_new})
        return user_id_new
        


# ================= VALIDATOR
    @staticmethod
    def validate(data):
        is_valid = True
        
        #name validation
        if len(data['name']) < 2:
            is_valid = False
            flash('Name required to be at least 2 characters','reg')

        #Username validation
        if len(data['username']) < 2:
            is_valid = False
            flash('Username required to be at least 2 characters','reg')
        else:
            username_dict = {
                'username' : data['username']
            }
            potential_user = User.get_by_username(username_dict)
            if potential_user:
                is_valid = False
                flash('username already taken!','reg')

        #Email validation
        if len(data['email']) < 1:
            is_valid = False
            flash('email required','reg')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('invalid email address!','reg')
        else:
            email_dict = {
                'email' : data['email']
            }
            potential_user = User.get_by_email(email_dict)
            if potential_user:
                is_valid = False
                flash('email already taken!','reg')
        
        #Password validation
        if len(data['password']) < 8:
            is_valid = False
            flash('password required to be at least 8 characters','reg')
        elif not data['password'] == data["confirm_password"]:
            is_valid = False
            flash("passwords don't match!",'reg')
        return is_valid