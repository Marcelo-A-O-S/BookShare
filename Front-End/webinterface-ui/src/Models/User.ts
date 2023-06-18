import IUser from '../Interfaces/IUser'


class User implements IUser{
    public id: number;
    public nome: string;
    public email: string;
    public papelAtribuido: string;
    public constructor(){
        this.id = 0;
        this.nome = '';
        this.email = '';
        this.papelAtribuido = "";
    }

}
export default User
