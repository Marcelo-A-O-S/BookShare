from Database.Generics.Generic import BaseGeneric
from Business.Models.Usuario import Usuario
from typing import TypeVar
T = TypeVar("T");
class UsuarioRepository(BaseGeneric):
    def __init__(self) -> None:
        super().__init__()
