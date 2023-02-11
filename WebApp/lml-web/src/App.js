import logo from './logo.svg';
import './App.css';
import Back from'./images/BG.jpg';
import User from './Component/User';
import UserS from './images/AdminS.png';
import UserT from './images/AdminT.png';
import Form from './Component/Form';


function App() {
  return (
    <div className= "flex">
     <div  className="half" >
       {/* <h1 className="text-black text-2xl absolute right-96 top-64 font-bold  ">Login as</h1> */}
      <div className=" flex flex-col items-center  absolute left-1/4 top-72 ">
         <User photo={UserS}  />
          <h1 className=" text-cyan-50 font-bold">Student</h1>
      </div>
      <div className="flex flex-col items-center absolute left-2/3 top-72">
         <User photo={UserT}  />
         <h1 className=" text-cyan-50 font-bold">Lecturer</h1>
      </div>
     
  
     </div>
     <div className="log" >
       <Form/>
         
     </div>
    </div>
  );
}

export default App;
