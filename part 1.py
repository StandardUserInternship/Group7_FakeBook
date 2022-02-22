import flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
## under MAIN config for heavy lifting 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'