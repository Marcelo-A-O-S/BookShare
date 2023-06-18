import { Link, useNavigate, Outlet } from 'react-router-dom'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import  {useContext } from 'react';
import AuthContext from '../../Context/AuthContext';
import DropdowUsuario from '../Dropdows/DropdownUsuario';
import DropdowAdministrador from '../Dropdows/DropdownAdmin';





export default function Header(){
    const {user, signed} = useContext(AuthContext)
    function DropdowUser(){
      if(user?.papelAtribuido === "Usuario"){
        return <DropdowUsuario/>
      }else if(user?.papelAtribuido === "Administrador"){
        return <DropdowAdministrador/>
      }else{
        return<>
            <Nav.Link eventKey={2} href="#memes">
            <Link style={{textDecoration: 'none', color: "white"}} to="/Login"> Log In</Link>
            </Nav.Link>
        </>
      }
    }
    return signed === false?(
    <>
    <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="#home">Book Share</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto" >
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to="/Home" > Home</Link></Nav.Link>
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to="/About"> About </Link></Nav.Link>

          </Nav>
          <Nav>
            {DropdowUser()}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    <main>
      <Outlet/>
    </main>
    </>

    ):(
      <>
      <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
      <Container>
        <Navbar.Brand href="/Signed">Book Share</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto" >
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to={"/Signed/Home"} > Home</Link></Nav.Link>
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to='/Signed/Timeline'> TimeLine </Link></Nav.Link>
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to="/Signed/Ebooks"> Ebooks </Link></Nav.Link>
            <Nav.Link ><Link style={{textDecoration: 'none', color: "white"}} to="/Signed/Create"> Create </Link></Nav.Link>
          </Nav>
          <Nav>
            {DropdowUser()}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    <main>
    <Outlet/>
    </main>
      </>
    );
}
