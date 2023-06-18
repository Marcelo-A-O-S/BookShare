class Book{
    public id: number | undefined;
    public nome: string;
    public descricao: string;
    public livro: string | undefined;
    public constructor(){
        this.id = 0;
        this.nome = '';
        this.descricao = '';
        this.livro = ''
    }

}
export default Book
