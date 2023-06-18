from Database.Generics.Generic import BaseGeneric
from Business.Models.Livro import Livro
from typing import TypeVar
T = TypeVar("T");
class PostRepository(BaseGeneric):
    def __init__(self) -> None:
        super().__init__()
