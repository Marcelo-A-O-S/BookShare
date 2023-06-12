import hashlib
import os

class Usuario:
    def __init__(self):
        self.id = 0;
        self.primeironome = "";
        self.ultimonome = "";
        self.email = "";
        self.papelAtribuido = "";
        self.senhaHash: str = "";
        self.senhaSalt: str = "";

    def criarSenhaHash(self, password):
        salt = os.urandom(16);
        self.senhaSalt = salt.hex();
        data_with_salt = password + self.senhaSalt;
        hasher = hashlib.sha256();
        hasher.update(data_with_salt.encode("utf-8"));
        self.senhaHash = hasher.hexdigest();
        return

    def VerificarSenhaHash(self, password):

        data_with_salt = password + self.senhaSalt;
        hasher = hashlib.sha256();
        hasher.update(data_with_salt.encode("utf-8"));
        hash_create = hasher.hexdigest()
        if self.senhaHash == hash_create:
            return True
        else:
            return False
