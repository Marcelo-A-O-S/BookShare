import { Outlet, Navigate } from 'react-router-dom'
import { useContext } from 'react';
import AuthContext from './AuthContext';

export const AuthAdmin= () => {
    const {signed, user } = useContext(AuthContext)
    return(
        user?.papelAtribuido === 'Adiministrador'? <Outlet/>:
        <Navigate to="/Login" replace/>
    );
}
