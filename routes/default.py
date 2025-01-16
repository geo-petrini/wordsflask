from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import current_app
import io

app = Blueprint('default', __name__)


@app.route('/')
def home():
    return render_template('index.html')
