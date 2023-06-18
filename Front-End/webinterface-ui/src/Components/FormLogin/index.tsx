import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import {ChangeEvent, useState, useContext} from 'react'
import LoginView from '../../ViewModel/LoginView';
import AuthContext from '../../Context/AuthContext';
import User from '../../Models/User';
import Button from 'react-bootstrap/Button';
import {useNavigate} from 'react-router-dom';
export default function FormLogin(){
    const [login, setLogin] = useState<LoginView >({
        email: "",
        password: "",
      });
    const navigate = useNavigate();
    const { SignIn, VerificarUsuario, SignOut } = useContext(AuthContext)
    async function LogOut(){
        await SignOut();
    }
    async function CheckUser(){
        VerificarUsuario();
    }

    async function SubmitLogin(e:any){
        e.preventDefault();
        console.log(login);
        const response =  await fetch("http://127.0.0.1:5000//Login", {
            method:"POST",
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify(login),
         })
        const result = await response.json();
        console.log(result)
        const BodyUser = new User();
        BodyUser.id = result.id;
        BodyUser.nome = result.nome;
        BodyUser.email = result.email;
        BodyUser.papelAtribuido = result.papelAtribuido
        await SignIn(BodyUser)
        navigate("/Signed")
    }
    return(
        <Form onSubmit={SubmitLogin}>
        <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
          <Form.Label column sm="2">
            Email
          </Form.Label>
          <Col sm="10">
            <Form.Control type={"email"}
             onChange={(e) => setLogin(prevLogin =>
                        ({
                            ...prevLogin,
                            email: e.target.value

                         }))}

            value={login.email}
            placeholder='email@example.com'/>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formPlaintextPassword">
          <Form.Label column sm="2">
            Password
          </Form.Label>
          <Col sm="10">
            <Form.Control type="password"
            onChange={(e) => setLogin(prevLogin =>
                ({
                    ...prevLogin,
                    password: e.target.value

                 }))}
            value={login.password}
            placeholder="Password" />
          </Col>
        </Form.Group>
        <Button type="submit">Entrar</Button>
        <Button onClick={CheckUser} type="button">Verificar Usuario</Button>
      </Form>


    )
}
