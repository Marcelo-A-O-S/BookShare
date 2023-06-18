import { Outlet, Navigate } from 'react-router-dom'
import { useContext } from 'react';
import AuthContext from './AuthContext';

export const AuthUsuario = () => {
    const { user } = useContext(AuthContext)
    return(
        user?.papelAtribuido === 'Usuario'? <Outlet/>:
        <Navigate to="/Login"replace/>
    );
}
