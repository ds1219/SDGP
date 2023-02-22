import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import Login from './Component/Login'
import Location from './Component/Location';
import FileInput from './Component/FileInput';
import{Route,Routes,Link} from "react-router-dom";
import QrScanner from './Component/QrScanner';



function App() {

<<<<<<< HEAD
  return (
<<<<<<< HEAD
   <Location/>
=======
   <FileInput/>
>>>>>>> 9680c085321d3a5424fb6d42efa09d76e5f3b7ce
    )
=======
  return <Routes>
    <Route path="/" element= {<Login/>} />
    <Route path="/lecturer" element={<FileInput/>}/>
    <Route path='/student' element={<QrScanner/>}/>
  </Routes>
>>>>>>> 3c5fdd5a3d91e35b10887d7401800f6b8a133e51
  

}

export default App;
