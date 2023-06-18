from dataclasses import dataclass
from datetime import date

@dataclass
class Post:
    id: int;
    idUsuario:int;
    idLivro: int;
    def __init__(self):
        self.id = 0;
        self.idUsuario = 0;
        self.idLivro = 0
