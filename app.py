import os
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import current_app

from models.conn import db
from models.model import *

from flask_migrate import Migrate

from routes.default import app as bp_default

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.register_blueprint(bp_default)      

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #L'opzione SQLALCHEMY_TRACK_MODIFICATIONS è una configurazione per Flask-SQLAlchemy che determina se SQLAlchemy deve o meno tenere traccia delle modifiche sugli oggetti per ogni sessione.

db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    # with app.app_context():
        # init_db()
    app.run(debug=True)
