import datetime
from flask import current_app
from flask import abort, redirect, url_for, flash
from sqlalchemy import ForeignKey
from models.conn import db

class Cloud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), unique=False, nullable=True)
    ts_add = db.Column( db.Float(), default=datetime.datetime.now().timestamp() )
    
    
class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(200), unique=False, nullable=True)
    cloud_id = db.Column(db.Integer(), ForeignKey('cloud.id'))