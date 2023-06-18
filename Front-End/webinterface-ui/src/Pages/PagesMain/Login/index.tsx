
import FormLogin from "../../../Components/FormLogin"
import FormRegister from "../../../Components/FormRegister"
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Stack from 'react-bootstrap/Stack';

export default function Login(){

    return(
        <Container>

            <Row>
                    <Col>
                        <FormLogin/>
                    </Col>

                <Col>
                    <FormRegister/>
                </Col>
            </Row>

        </Container>

        // <>

        // <form onSubmit={SubmitLogin}>
        //     <div>
        //         <label>Email</label>
        //         <input type="text" name="email" id=""
        //         value={login.email}
        //         onChange={(e) => setLogin(prevLogin =>
        //         ({
        //             ...prevLogin,
        //             email: e.target.value

        //          }))} required/>
        //     </div>
        //     <div>
        //         <label>Password</label>
        //         <input type={"text"} name="password" id=""
        //         value={login.password}
        //         onChange={(e) => setLogin(prevLogin =>
        //             ({
        //                 ...prevLogin,
        //                 password: e.target.value

        //              }))} required/>
        //     </div>

        //     <button type={"submit"} >Logar</button>
        //     <button type={"button"} onClick={LogOut}>Log Out</button>
        //     <button type={"button"}  onClick={CheckUser}>Check User</button>
        // </form>
        // </>
    )
}
