from Api import app
from Business.Models.Usuario import Usuario
from flask import request, jsonify
import json
from Business.Services.UsuarioServices import UsuarioServices
from Api.ViewModel.UsuarioView import UsuarioView
from flask_cors import cross_origin


@app.route("/Login", methods = ['POST'])
def login():
    try:
        data = json.loads(request.data);

        usuarioAtual = Usuario();
        userService = UsuarioServices();
        usuarioAtual = userService.BuscarUsuarioPorEmail(data['email']);
        if usuarioAtual != 0:
            resultado = usuarioAtual.VerificarSenhaHash(data['password'])
            if resultado == True:
                usuarioview = UsuarioView();
                usuarioview.id = usuarioAtual.id;
                usuarioview.nome = usuarioAtual.primeironome;
                usuarioview.email = usuarioAtual.email;
                usuarioview.papelAtribuido = usuarioAtual.papelAtribuido;
                return json.dumps(usuarioview.__dict__)
            else:
                return jsonify("Password incorreto!")
        else:
            return jsonify("Usuário não cadastrado!")

    except Exception as e:
        return jsonify(e);

@app.route("/Register", methods = ['POST'])
def registrar():
    try:
        data = json.loads(request.data);
        userService = UsuarioServices();
        usuario = Usuario();
        resultado = userService.VerificarExisteEmailUsuario(data['email'])
        if resultado == False:
            usuario.primeironome = data['firstname'];
            usuario.ultimonome = data['lastname'];
            usuario.email = data['email'];
            usuario.papelAtribuido = "Usuario"
            usuario.criarSenhaHash(data['password']);
            userService.SalvarUsuario(usuario);
            return jsonify("Registro realizado com sucesso");
        elif resultado == True:
            return jsonify("O email é invalido")
        else:
            return jsonify(resultado)
    except Exception as e:
        return jsonify(e);

