import User from './User';
import '../App.css';
import UserS from '../images/AdminS.png';
import UserT from '../images/AdminT.png';
import Form from './Form';
import React from 'react';

export default function(){
    const [nextpage,setNextPage]=React.useState(true);

    return(
 <div className= " flex h-screen ">
     
     <div  className="half" >
       {/* <h1 className="text-black text-2xl absolute right-96 top-64 font-bold  ">Login as</h1> */}
        <div className=" flex flex-col items-center  absolute left-1/4 top-72 " >
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
    )
}
