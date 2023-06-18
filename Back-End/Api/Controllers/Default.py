from Api import app
from Business.Models.Usuario import Usuario
from Business.Models.Livro import Livro
from Business.Models.Post import Post
from Business.Services.UsuarioServices import UsuarioServices
from Business.Services.LivroServices import LivroServices
from Business.Services.PostServices import PostServices
from flask import jsonify, json, request
from Api.Authentication.Authentication import  Authentication
from datetime import datetime

@app.route("/")
def index():
    return "Api funcionando";

@app.route("/salvarUsuarioTeste")
@Authentication.acess_authenticated(["Usuário", "Adimistrador"])
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

@app.route("/BuscarPorId")
def BuscarPorId():
    userService = UsuarioServices();
    usuario = userService.BuscarUsuarioPorId(2)
    if usuario != None:
        return usuario;
    else:
        return "O usuario não foi encontrado"

@app.route("/SalvarPost", methods = ['POST'])
@Authentication.acess_authenticated(["Usuario", "Adimistrador"])
def SalvarPost():
    try:
        data = json.loads(request.data);
        livroServices = LivroServices();
        postServices = PostServices();
        retorno = livroServices.VerificarSeExisteBook(data['livro']['nome']);
        livro = Livro();
        post = Post();
        if retorno > 0:
            livro.nome =  "{}({})".format(data['livro']['nome'], retorno + 1 );
        else:
            livro.nome = data['livro']['nome'];


        livro.descricao = data['livro']['descricao'];
        livro.livro = data['livro']['livro'];
        livroServices.SalvarBook(livro);
        livro = livroServices.BuscarBookPorNome(livro.nome);
        post.idLivro = livro.id;
        post.idUsuario = data['idUsuario'];
        postServices.SalvarPost(post)
        return jsonify("Publicação feita com sucesso")
    except Exception as e:
        return jsonify(e);
