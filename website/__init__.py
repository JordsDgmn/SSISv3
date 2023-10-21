from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////C:/Users/Jords/Desktop/SSISv3/SSIS-v.3-WebApp/SSISv3.db'
db = SQLAlchemy(app)

from app import routes