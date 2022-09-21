from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getData')
def getdata():
    return {'yee': 'haw'}