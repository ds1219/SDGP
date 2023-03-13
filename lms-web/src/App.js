import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import Login from './Component/Login'
import Location from './Component/Location';
import FileInput from './Component/FileInput';
import{Route,Routes,Link,RouterProvider,createBrowserRouter} from "react-router-dom";
import QrScanner from './Component/QrScanner';
import Question from './Component/Quiz';


function App() {
  return <Routes>
    <Route path="/" element= {<Login/>} />
    <Route path="/lecturer" element={<FileInput/>}/>
    <Route path='/student' element={<QrScanner/>}/>
    <Route path='/quiz' element={<Question/>}/>
    <Route path='/location' element={<Location/>}/>
  </Routes>
}

export default App;
