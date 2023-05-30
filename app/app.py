from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db


app = Flask(__name__)

#only for show text temporally with library flash
app.secret_key = 'mysecretkey'
#------

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mypassword@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa la instancia de SQLAlchemy con la aplicación Flask

app.register_blueprint(contacts)


#Comands for use docker container mysql
#docker run --name mymysql -e MYSQL_ROOT_PASSWORD=mypassword -p 3306:3306 -d mysql:latest
#docker exec -it mymysql bash
#mysql -u root -p
#create database contactsdb;

