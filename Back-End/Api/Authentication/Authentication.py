from functools import wraps
from flask import request, jsonify, make_response
def admin_required(f):
    @wraps(f)
    def validarPapel(*args, **kwargs):
        auth = request.authorization
        if auth != None:
            if auth.papelAtribuido == "Adiministrador":
                return f(*args, **kwargs)
            else:
                return make_response("Acesso negado!",401);
        else:
            return make_response("Acesso negado!",401);

    return validarPapel

def usuario_required(f):
    @wraps(f)
    def validarPapel(*args, **kwargs):
        auth = request.authorization;
        if auth != None:
            if auth.papelAtribuido == "Usuario":
                return f(*args, **kwargs)
            else:
                return make_response("Acesso negado!",401)
        else:
                return make_response("Acesso Negado",401)

    return validarPapel

class Authentication:
    def __init__(self) -> None:
        pass
    @staticmethod
    def acess_authenticated(roles):
        def decorator_func(f):
            @wraps(f)
            def validarPapel(*args, **kwargs):
                auth = request.authorization;
                roleCurrent = auth.__str__().replace(' ','');
                if auth != None:
                    papelValido = False;
                    for role in roles:
                        if roleCurrent == role:
                            papelValido = True;

                    if papelValido == True:
                        return f(*args, **kwargs)
                    else:
                        return make_response("Acesso negado!",401)
                else:
                        return make_response("Acesso Negado",401)

            return validarPapel
        return decorator_func

