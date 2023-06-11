import {BrowserRouter, Route, Routes} from 'react-router-dom';
import Home from '../Pages/Home'
import About from '../Pages/About';
import Header from '../Components/Header';
import Register from '../Pages/Register';

export default function Rotas(){
    return(
    <>
    <BrowserRouter>
    <Header/>
        <Routes >
        <Route index path='/' element={<Home/>}/>
        <Route  path='/About' element={<About/>}/>
        <Route  path='/Register' element={<Register/>}/>
        </Routes>
    </BrowserRouter>
    </>)
}
