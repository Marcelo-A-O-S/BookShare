from Api import app
from Business.Models.Usuario import Usuario
from Business.Services.UsuarioServices import UsuarioServices
from flask import jsonify, json

@app.route("/")
def index():
    return "Api funcionando";

@app.route("/salvarUsuarioTeste")
def salvarUsuarioTeste():
        userService = UsuarioServices();
        usuario = Usuario();
        resultado = userService.VerificarExisteEmailUsuario("usuarioteste@gmail.com")
        if resultado == False:
            usuario.primeironome = "Usuario";
            usuario.ultimonome = "Teste";
            usuario.email = "usuarioteste@gmail.com";
            usuario.papelAtribuido = "Usuario"
            usuario.criarSenhaHash("12345678");
            userService.SalvarUsuario(usuario)
            return json.dumps(usuario.__dict__)
        elif resultado == True:
            return "Valor existente"
        else:
            return resultado

@app.route("/BuscarUsuario")
def BuscarrUsuarioTeste():
        userService = UsuarioServices();
        usuario = Usuario();
        usuario = userService.BuscarUsuarioPorEmail("teste@gmail.com")
        if usuario.id != 0:
            resultado = usuario.VerificarSenhaHash("12345678")
            if resultado == True:
                return "O teste foi um sucesso"
            else:
                return "Fracasso"
        else:
            return "Derrota"

@app.route("/AtualizarUsuario")
def AtualizarUsuario():
    userService = UsuarioServices();
    usuario = userService.BuscarUsuarioPorEmail("usuarioteste@gmail.com")
    if usuario.id != 0:
        usuario.primeironome = "UsuarioAlterado"
        return userService.SalvarUsuario(usuario);


@app.route("/ListarUsuario")
def ListarUsuario():
    userService = UsuarioServices();
    listusuario = userService.ListarUsuario()
    result = json.dumps(listusuario, default=lambda obj: obj.__dict__);
    return jsonify(result);



