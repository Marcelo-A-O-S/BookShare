from flask import Flask;
from flask_cors import CORS, cross_origin;


app = Flask(__name__);
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from Api.Controllers import Default
from Api.Controllers import Usuario
from Api.Controllers import Cadastro
