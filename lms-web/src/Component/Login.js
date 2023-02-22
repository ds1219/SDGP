import User from './User';
import '../App.css';
import UserS from '../images/AdminS.png';
import UserT from '../images/AdminT.png';
import Form from './Form';
import React from 'react';


export default function(){
    const [nextpage,setNextPage]=React.useState(true);

    return(
<div className= "flex flex-col md:flex-row h-screen">
     
  <div className="half ">
    {/* <h1 className="text-black text-2xl absolute right-96 top-64 font-bold  ">Login as</h1> */}
    <div className="flex flex-row md:flex-row items-center  justify-center h-full">
      <div className="md:w-1/2 flex flex-col  items-center md:items-start justify-center">
        <User photo={UserS} />
        <h1 className="text-cyan-50 font-bold">Student</h1>
      </div>
      <div className="md:w-1/2 flex flex-col items-center md:items-end justify-center">
        <User photo={UserT} />
        <h1 className="text-cyan-50 font-bold">Lecturer</h1>
      </div>
    </div>
  </div>
    
  <div className="md:w-1/2 bg-white">
    <div className="flex items-center justify-center h-full">
      <div className="w-full md:w-3/4 lg:w-1/2">

        <Form />
      </div>
    </div>
  </div>

</div>

    )
}
