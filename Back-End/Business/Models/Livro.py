from dataclasses import dataclass

@dataclass
class Livro:
    def __init__(self):
        self.id = 0;
        self.nome = "";
        self.descricao = "";
        self.livro: str = "";
