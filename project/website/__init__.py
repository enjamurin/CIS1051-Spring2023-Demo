from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask import current_app
import os
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'extremelysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Closet, Item
    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))     
    
    #print_table(db, 'item')

    return app

def print_table(db, table_name):
    engine = db.create_engine('sqlite:///database.db')
    connection = engine.connect()
    metadata = db.MetaData()
    table_info = db.Table(table_name, metadata, autoload=True, autoload_with=engine)

    print(table_info.columns.keys())
    print(repr(metadata.tables[table_name]))

def create_database(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Created Database!')

        #abs_path = os.path.abspath("website/" + DB_NAME)
        #print("Database path:", abs_path)



