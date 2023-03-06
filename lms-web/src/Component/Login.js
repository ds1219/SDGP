
import User from './User';
import '../App.css';
import UserS from '../images/AdminS.png';
import UserT from '../images/AdminT.png';
import Form from './Form';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Logo from '../images/logo.png';




 function Login(props){
 const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [userType, setUserType] = useState(null);
  const navigate=useNavigate();

  const handleSubmit = (formData) => {
    // Check if the user's login details are correct using Flask
    // If the details are correct, navigate to the appropriate page
    if (userType === 'student') {
      // Navigate to the student page
      navigate('/student');
    } else if (userType === 'lecturer') {
      // Navigate to the lecturer page
      navigate('/lecturer');
    }
  }

  const handleUserTypeClick = (type) => {
    var lec=document.getElementById('lec')
    var stu=document.getElementById('stu')
    setUserType(type);
    console.log(type)
     if (type === 'student') {
      stu.style.scale="1.3"
      lec.style.scale="1"
      lec.style.opacity="0.7"
      stu.style.opacity="1"
      
    } else if (type === 'lecturer') {
      lec.style.scale="1.3"
      stu.style.scale="1"
      stu.style.opacity="0.7"
       lec.style.opacity="1"
    }
    
    
    //  if (type === 'student') {
    //   // Navigate to the student page
    //   navigate('/user.js');
    // } else if (type === 'lecturer') {
    //   // Navigate to the lecturer page
    //   navigate('/lecturer');
    // }
  }

    return(
<div className="flex flex-col md:flex-row h-screen">
  <div className="half md:w-1/2 flex  justify-around  items-center">
    <div className="flex justify-around   w-full ">
      <div id='stu' className="md:w-1/2 flex flex-col   md:items-center justify-center items-center "
      onClick={() => handleUserTypeClick('student')}
      >
        <User photo={UserS} />
        <h1 className="text-cyan-50 font-bold">Student</h1>
      </div>
      <div id='lec' className="md:w-1/2 flex flex-col md:items-center justify-center items-center"
       onClick={() => handleUserTypeClick('lecturer')}
      >
        <User photo={UserT} />
        <h1 className="text-cyan-50 font-bold">Lecturer</h1>
      </div>
    </div>
  </div>

  <div className="md:w-1/2 bg-white">
    <div className="flex items-center justify-center h-full">
      <div className="w-full md:w-3/4 lg:w-1/2">
        {/* <Form onSubmit={handleSubmit}/> */}
          <div className="login flex flex-col items-center justify-center h-screen">
           <img src={Logo} alt="Lms" className="mb-8 w-40" />

  <form onSubmit={handleSubmit}  className="w-full max-w-md">
    <div className="mb-4">
      <label htmlFor="email" className="block mb-2 font-bold">Email</label>
      <input 
        name="email"
        type="email"
        placeholder="Email"
        className="w-full px-3 py-2 placeholder-gray-400 border rounded-lg appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      />
    </div>

    <div className="mb-4">
      <label htmlFor="password" className="block mb-2 font-bold">Password</label>
      <input 
        name="password"
        type="password"
        placeholder="Password"
        className="w-full px-3 py-2 placeholder-gray-400 border rounded-lg appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
      />
      <a href="" className="text-blue-500 text-sm hover:underline">Forgot Password?</a>
    </div>

    <button
   
     
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mb-4"
    >
      Submit
    </button>
  </form>
</div>
      </div>
    </div>
  </div>
</div>


    )
}
export default Login;;