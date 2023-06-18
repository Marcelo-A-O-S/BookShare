import RouteMain from './Routes/RouteMain';
import {useContext, useEffect, useState} from 'react'
import AuthContext, {AuthProvider} from './Context/AuthContext';

import 'bootstrap/dist/css/bootstrap.min.css';


function App() {

  return (
    <div className="App">
      <RouteMain/>
    </div>
  );
}

export default App;
