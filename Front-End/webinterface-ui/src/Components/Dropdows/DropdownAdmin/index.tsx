import {  useNavigate } from 'react-router-dom';

import NavDropdown from 'react-bootstrap/NavDropdown';
import  {useContext } from 'react';
import AuthContext from '../../../Context/AuthContext';

const DropdowAdministrador = (props:any) => {
    const {SignOut} = useContext(AuthContext)
    const navigate = useNavigate()
      async function DeslogarAdm(){
        await SignOut()
        return navigate("/Login");
      }
      return(
          <NavDropdown title={props.nome} id="collasible-nav-dropdown">
                <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                <NavDropdown.Item href="#action/3.2">
                  Another action
                </NavDropdown.Item>
                <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item onClick={DeslogarAdm}>
                  Logout
                </NavDropdown.Item>
          </NavDropdown>
      )
  }
export default DropdowAdministrador;
