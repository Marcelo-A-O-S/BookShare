import {BrowserRouter, Route, Routes, Navigate, RouteProps, RouteObject, createBrowserRouter, RouterProvider} from 'react-router-dom';
import Home from '../Pages/PagesMain/Home';
import HomeServices from '../Pages/PagesServices/Home';
import About from '../Pages/PagesMain/About';
import Header from '../Components/Header';
import Login from '../Pages/PagesMain/Login';
import AuthContext, { AuthProvider  } from '../Context/AuthContext';
import { Component, useContext } from 'react';
import Ebook from '../Pages/PagesServices/Ebooks';
import Timeline from '../Pages/PagesServices/Timeline';
import { AuthSigned } from '../Context/Authsigned';
import { AuthAdmin } from '../Context/AuthAdmin';
import { AuthUsuario } from '../Context/AuthUsuario';
import HomeAdmin from '../Pages/PagesAdmin/Home';
import HomeUsuario from '../Pages/PagesUsuario/Home';
import Create from '../Pages/PagesServices/Create';



export default function RouteMain(){
    return(
    <>
    <BrowserRouter>
    <AuthProvider>
            <Routes >
                <Route path="/" element={<Header/>}>
                    <Route  path='/' element={<Home/>}/>
                    <Route  path='/Home' element={<Home/>}/>
                    <Route  path='/About' element={<About/>}/>
                    <Route  path='/Login' element={<Login/>}/>
                    <Route  path='/*' element={<Home/>}/>
                    <Route path="/Signed" element={<AuthSigned/>}>
                        <Route  path='/Signed' element={<HomeServices/>}/>
                        <Route  path='/Signed/Home' element={<HomeServices/>}/>
                        <Route  path='/Signed/Create' element={<Create/>}/>
                        <Route  path='/Signed/Ebooks' element={<Ebook/>}/>
                        <Route  path='/Signed/Timeline' element={<Timeline/>}/>
                        <Route  path='/Signed/*' element={<HomeServices/>}/>
                        <Route path='/Signed/Admin' element={<AuthAdmin/>}>
                            <Route path='/Signed/Admin' element={<HomeAdmin/>}/>
                        </Route>
                        <Route path='/Signed/Usuario' element={<AuthUsuario/>}>
                            <Route path='/Signed/Usuario' element={<HomeUsuario/>}/>
                        </Route>
                    </Route>
                </Route>
            </Routes>
    </AuthProvider>
    </BrowserRouter>
    </>)
}
