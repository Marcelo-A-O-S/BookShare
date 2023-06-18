from Business.Models.Livro import Livro
from Business.Repository.LivroRepository import LivroRepository
from Business.CustomServices.LivroCustom import LivroCustom
from typing import List

class LivroServices:
    def __init__(self) -> None:
        self.livroRepository = LivroRepository();
        self.livroCustom = LivroCustom();
    def SalvarBook(self, livro:Livro) -> Livro:
        try:
            if livro.id == 0:
                self.livroRepository.Insert(livro)
                return "Salvo com sucesso!";
            else:
                self.livroRepository.Update(livro)
                return "Atualizado com sucesso";
        except Exception as e:
            return e;
    def ListarBook(self)-> List[Livro]:
        try:
            livro = Livro()
            listalivro = self.livroRepository.List(livro);
            return listalivro;
        except Exception as e:
            return e;

    def BuscarBookPorId(self, id):
        try:
            livro = Livro()
            livro = self.livroRepository.FindById(livro, id=id)
            if livro != None:
                return livro;
            else:
                return livro;
        except Exception as e:
            return e;
    def DeletarBook(self, id) :
        try:
            livro = Livro();
            self.livroRepository.Delete(livro, id=id)
        except Exception as e:
            return e;

    def VerificarSeExisteBook(self, livroNome: str):
        try:
            resultado = self.livroCustom.VerificarSeExisteBook(livroNome)
            if resultado != None:
                return resultado;
            else:
                return resultado;
        except Exception as e:
            return e;

    def BuscarBookPorNome(self, livroNome: str):
        try:
            livro = Livro();
            livro = self.livroCustom.BuscarLivroPorNome(livro, livroNome)
            if livro.id != 0:
                return livro;
            else:
                return livro;
        except Exception as e:
            return e;

