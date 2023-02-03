from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhh"
app.config['SECRET_KEY'] = 'secret!'
DATABASE = "rps"