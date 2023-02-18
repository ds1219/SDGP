import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import Login from './Component/Login'
import Location from './Component/Location';
import FileInput from './Component/FileInput';
import{Route,Routes,Link} from "react-router-dom";



function App() {

  return <Routes>
    <Route path="/" element= {<Login/>} />
    <Route path="/lecturer" element={<FileInput/>}/>
    <Route/>
  </Routes>
  

}

export default App;
