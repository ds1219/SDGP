import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import Login from './Component/Login'
import Location from './Component/Location';
import FileInput from './Component/FileInput';
import{Route,Routes} from "react-router-dom";



function App() {

  return <Routes>
    <Route path="/" element= {<Login/>} />
    <Route/>
    <Route/>
  </Routes>
  

}

export default App;
