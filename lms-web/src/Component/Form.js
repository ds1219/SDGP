import Location from './Location';
import '../App.css';
import Logo from '../images/logo.png';
import { Route,Routes,Link } from 'react-router-dom';
import React, { useState } from "react";


export default function(){


   
    return(
      <div className="login flex flex-col items-center justify-center h-screen">
  <img src={Logo} alt="Lms" className="mb-8 w-40" />

  <form  className="w-full max-w-md">
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

    )
    }
