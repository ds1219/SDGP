import React, { useState } from "react";
import UserS from "../images/AdminS.png";
import UserT from "../images/AdminT.png";


const ENDPOINT = "http://127.0.0.1:5000";
 function AddDetails(){
     const [userType, setUserType] = useState(null);
     const [email, setEmail] = useState("");
     const [firstName, setFirstName] = useState("");
     const [lastName, setLastName] = useState("");
     const [subjectIDs, setsubjectIDs] = useState("");
     const [hashedPass, sethashedPass] = useState("");
     function handleFormSubmit(event) {
    event.preventDefault();
    const data = {
      email,
      firstName,
      lastName,
      subjectIDs,
      hashedPass,
      userType,
    };
    fetch(ENDPOINT + "/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          // handle successful response
          console.log("pass")
        } else {
          // handle error response
            console.log("fail")
        }
      })
      .catch((error) => {
        // handle network error
      });
  }

  const handleUserTypeClick = (type) => {
    var lec = document.getElementById("lec");
    var stu = document.getElementById("stu");
    setUserType(type);
    console.log(type);
    if (type === "student") {
      stu.style.scale = "1.3";
      lec.style.scale = "1";
      lec.style.opacity = "0.7";
      stu.style.opacity = "1";
    } else if (type === "lecturer") {
      lec.style.scale = "1.3";
      stu.style.scale = "1";
      stu.style.opacity = "0.7";
      lec.style.opacity = "1";
    }
  };


    return(
    <div className="flex flex-col justify-center items-center h-screen bg-black">

         {/* <div className="half md:w-1/2 flex  justify-around  items-center"> */}
        <div className="flex justify-around  w-1/4  my-8">
          <div
            id="stu"
            className="md:w-1/2 flex flex-col   md:w-1/2 mx-12 items-center justify-center items-center cursor-pointer "
            onClick={() => handleUserTypeClick("student")}
          >
            <img src={UserS}></img>
            <h1 className="text-cyan-50 font-bold">Student</h1>
          </div>
          <div
            id="lec"
            className="md:w-1/2 flex flex-col md:items-center justify-center items-center cursor-pointer"
            onClick={() => handleUserTypeClick("lecturer")}
          >
          <img src={UserT}></img>
            <h1 className="text-cyan-50 font-bold">Lecturer</h1>
          </div>
        </div>
      {/* </div> */}

             
            
     <form
            method="POST"
            className="flex flex-col "
            onSubmit={handleFormSubmit}>
    
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          Email
          <input
            name="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
            type="email"
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          FirstName
          <input
            name="lirstName"
            value={firstName}
            onChange={(event) => setFirstName(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          LastName
          <input
            name="lastName"
            value={lastName}
            onChange={(event) => setLastName(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          subjectIDs
          <input
            name="subjectIDs"
            value={subjectIDs}
            onChange={(event) => setsubjectIDs(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>

       <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          Password
          <input
            name="hashedPass"
            value={hashedPass}
            type="password"
            onChange={(event) => sethashedPass(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mb-4">
          Enter
        </button>
      </form>
        </div>
    )

}

export default AddDetails;