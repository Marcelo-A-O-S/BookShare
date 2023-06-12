from Business.Models.Usuario import Usuario
from Business.Repository.UsuarioRepository import UsuarioRepository
from Business.CustomServices.UserCustom import UserCustom
from typing import List

class UsuarioServices:
    def __init__(self) -> None:
        self.usuarioRepository = UsuarioRepository()
        self.usuarioCustom = UserCustom()
    def SalvarUsuario(self, user:Usuario) -> Usuario:
        try:
            if user.id == 0:
                self.usuarioRepository.Insert(user)
                return "Salvo com sucesso!";
            else:
                self.usuarioRepository.Update(user)
                return "Atualizado com sucesso";
        except Exception as e:
            return e;
    def ListarUsuario(self)-> List[Usuario]:
        try:
            usuario = Usuario()
            listausuario = self.usuarioRepository.List(usuario);
            return listausuario;
        except Exception as e:
            return e;
    def VerificarExisteEmailUsuario(self, email: str):
        try:
            result = self.usuarioCustom.VerificarExisteEmailUsuario(email);
            return result;
        except Exception as e:
            return e;
    def BuscarUsuarioPorEmail(self, email:str) -> Usuario:
        try:
            usuario = Usuario()
            resultado = self.usuarioCustom.BuscarPorEmailUsuario(email)
            if resultado == []:
                return usuario
            else:
                for linha in resultado:

                    usuario.id = int(linha['id']);
                    usuario.primeironome = linha['primeironome'];
                    usuario.ultimonome = linha['ultimonome'];
                    usuario.email = linha['email'];
                    usuario.papelAtribuido = linha['papelAtribuido'];
                    usuario.senhaHash = linha['senhaHash'];
                    usuario.senhaSalt = linha['senhaSalt'];
                    return usuario
        except Exception as e:
            return e;
