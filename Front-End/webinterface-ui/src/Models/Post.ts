import Book from "./Book";

class Post{
    public id: number | undefined;
    public idUsuario: number | undefined;
    public idBook: number | undefined;
    public livro: Book;
    public constructor(){
        this.id = 0;
        this.idUsuario = 0;
        this.idBook = 0;
        this.livro = new Book();
    }

}
export default Post
