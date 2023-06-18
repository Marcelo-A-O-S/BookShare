from Business.Models.Post import Post
from Business.Repository.PostRepository import PostRepository
from Business.CustomServices.UserCustom import UserCustom
from typing import List

class PostServices:
    def __init__(self) -> None:
        self.postRepository = PostRepository();
    def SalvarPost(self, post:Post) -> Post:
        try:
            if post.id == 0:
                self.postRepository.Insert(post)
                return "Salvo com sucesso!";
            else:
                self.postRepository.Update(post)
                return "Atualizado com sucesso";
        except Exception as e:
            return e;
    def ListarPost(self)-> List[Post]:
        try:
            post = Post()
            listapost = self.postRepository.List(post);
            return listapost;
        except Exception as e:
            return e;

    def BuscarPostPorId(self, id):
        try:
            post = Post()
            post = self.postRepository.FindById(post, id=id)
            if post != None:
                return post;
            else:
                return post;
        except Exception as e:
            return e;
    def DeletarPost(self, id):
        try:
            post = Post();
            self.postRepository.Delete(post, id=id)
        except Exception as e:
            return e;

