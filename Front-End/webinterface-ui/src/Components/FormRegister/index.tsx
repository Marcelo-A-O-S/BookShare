import {ChangeEvent, useState} from 'react'
import RegisterView from '../../ViewModel/RegisterView'
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
export default function FormRegister(){
    const [register, setRegister] = useState<RegisterView>({
        firstname: "",
        lastname: "",
        email: "",
        password: "",
        passwordConfirm: "",
      });


    const OnChangeRegister = (event:ChangeEvent<HTMLInputElement>) =>{
        const { value, name } = event.target;
        if(name === "firstname"){
            setRegister(prevState =>({
                ...prevState,
                firstname: value
            }));
        }
        else if(name === "lastname"){
            setRegister(prevState =>({
                ...prevState,
                lastname: value
            }));
        }else if(name === "email"){
            setRegister(prevState =>({
                ...prevState,
                email: value
            }));
        }else if(name === "password"){
            setRegister(prevState =>({
                ...prevState,
                password: value
            }));
        }
        else if(name === "passwordConfirm"){
            setRegister(prevState =>({
                ...prevState,

                passwordConfirm: value
            }));
        }

    }
    async function Register(e:any){
        e.preventDefault();
        console.log(register);
        const response =  await fetch("http://127.0.0.1:5000//Register", {
            method:"POST",
            headers: {
                "Content-Type": "application/json",
              },
            body: JSON.stringify(register),
         })
        const result = await response.json();
        console.log(result)
        console.log(result.status)
    }
    return(
        <>
        <Form onSubmit={Register}>
            <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
            <Form.Label column sm="2">
                First Name
            </Form.Label>
            <Col sm="10">
                <Form.Control type={"text"}
                onChange={(e) => setRegister(prevLogin =>
                            ({
                                ...prevLogin,
                                firstname: e.target.value

                            }))}

                value={register.firstname}
                placeholder=''/>
            </Col>
            </Form.Group>

            <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
            <Form.Label column sm="2">
                Last Name
            </Form.Label>
            <Col sm="10">
                <Form.Control type={"text"}
                onChange={(e) => setRegister(prevLogin =>
                            ({
                                ...prevLogin,
                                lastname: e.target.value

                            }))}

                value={register.lastname}
                placeholder=''/>
            </Col>
            </Form.Group>

            <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
            <Form.Label column sm="2">
                Email
            </Form.Label>
            <Col sm="10">
                <Form.Control type={"email"}
                onChange={(e) => setRegister(prevLogin =>
                            ({
                                ...prevLogin,
                                email: e.target.value

                            }))}

                value={register.email}
                placeholder='email@example.com'/>
            </Col>
            </Form.Group>

            <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
            <Form.Label column sm="2">
                Password
            </Form.Label>
            <Col sm="10">
                <Form.Control type={"password"}
                onChange={(e) => setRegister(prevLogin =>
                            ({
                                ...prevLogin,
                                password: e.target.value

                            }))}

                value={register.password}
                placeholder=''/>
            </Col>
            </Form.Group>
            <Form.Group as={Row} className="mb-3" controlId="formPlaintextEmail">
            <Form.Label column sm="2">
                Confirm Password
            </Form.Label>
            <Col sm="10">
                <Form.Control type={"password"}
                onChange={(e) => setRegister(prevLogin =>
                            ({
                                ...prevLogin,
                                passwordConfirm: e.target.value

                            }))}

                value={register.passwordConfirm}
                placeholder=''/>
            </Col>
            </Form.Group>
            <Button type="submit">Registrar</Button>
        </Form>

        </>
    )
}
