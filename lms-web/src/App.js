import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import Login from './Component/Login'
import Location from './Component/Location';
import FileInput from './Component/FileInput';
import{Route,Routes,Link} from "react-router-dom";
import QrScanner from './Component/QrScanner';
import Question from './Component/Quiz';


function App() {
<<<<<<< HEAD


=======
>>>>>>> fa2a666911037fb82323b065cc7a1198f6f22b28
  return <Routes>
    <Route path="/" element= {<Login/>} />
    <Route path="/lecturer" element={<FileInput/>}/>
    <Route path='/student' element={<QrScanner/>}/>
    <Route path='/quiz' element={<Question/>}/>
    <Route path='/location' element={<Location/>}/>
<<<<<<< HEAD
  </Routes>

  

=======
  </Routes> 
>>>>>>> fa2a666911037fb82323b065cc7a1198f6f22b28
}

export default App;
