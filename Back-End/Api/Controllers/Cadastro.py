from Api import app
from Business.Models.Usuario import Usuario
from flask import request, jsonify
import json

@app.route("/Login")
def login():
    return "Login";

@app.route("/Register", methods = ['POST'])
def registrar():
    data = json.loads(request.data);
    usuario = Usuario();
    usuario.firstname = data['firstname'];
    usuario.lastname = data['lastname'];
    usuario.password = data['password'];
    usuario.email = data['email'];
    print()
    return jsonify("Teste Finalizado Com sucesso");
