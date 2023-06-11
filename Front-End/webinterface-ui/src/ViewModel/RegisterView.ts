class RegisterView {
    public firstname: string;
    public lastname: string;
    public email: string;
    public password: string;
    public passwordConfirm: string;
    public constructor(_firstname = "", _lastname = "", _email = "", _password = "", _passwordConfirm = ""){
        this.firstname = _firstname;
        this.lastname = _lastname;
        this.email = _email;
        this.password = _password;
        this.passwordConfirm = _passwordConfirm;
    };

}
export default RegisterView
