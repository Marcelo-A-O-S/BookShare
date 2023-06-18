import { Link, Navigate, useNavigate } from 'react-router-dom'

import NavDropdown from 'react-bootstrap/NavDropdown';
import  {useContext } from 'react';
import AuthContext from '../../../Context/AuthContext';
const DropdowUsuario = (props:any) => {
    const {SignOut, user} = useContext(AuthContext)
    const navigate = useNavigate()
    async function Perfil(){
      return navigate("/Signed/Usuario")
    }
      async function DeslogarUsuario(){
        await SignOut()
        return navigate("/Login");
      }
      return(
          <NavDropdown title={user?.nome} id="collasible-nav-dropdown">
                <NavDropdown.Item onClick={Perfil}>Perfil</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item onClick={DeslogarUsuario}>
                  Logout
                </NavDropdown.Item>
          </NavDropdown>
      )
  }
export default DropdowUsuario;
