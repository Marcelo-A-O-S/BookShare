from flask import Flask;
from flask_cors import CORS, cross_origin;


app = Flask(__name__);
CORS(app)
app.config['CORS_HEADERS'] = ['Content-Type', 'Authorization']


from Api.Controllers import Default, Usuario, Cadastro


from Api.ViewModel import UsuarioView

from Api.Authentication import Authentication
