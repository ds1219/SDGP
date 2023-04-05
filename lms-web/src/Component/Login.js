import User from "./User";
import "../App.css";
import UserS from "../images/AdminS.png";
import UserT from "../images/AdminT.png";
import Form from "./Form";
import React, { useState, useEffect } from "react";
import { useNavigate, Link, json, createSearchParams } from "react-router-dom";
import Logo from "../images/logo.png";

function Login(props) {
  const [email, setemail] = useState("");
  const [hashedPass, sethashedPassword] = useState("");
  const [userType, setUserType] = useState(null);
  const [datas, setData] = useState();
  const [location, setLocation] = useState({});

  const navigate = useNavigate();
  const API_KEY = "";
  let userSessionID = "";
  const handleClick = () => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        setLocation({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
      },
      (error) => {
        console.error(error);
      },
      { enableHighAccuracy: true, timeout: 20000, maximumAge: 1000 }
    );
  };
  useEffect(() => {
    handleClick();
  }, []);

  useEffect(() => {
    if (!location.lat) {
      return;
    }

    fetch(
      `https://maps.googleapis.com/maps/api/geocode/json?latlng=${location.lat},${location.lng}&key=${API_KEY}`
    ).then((response) => response.json());
  }, [location]);
  var latAdd = location.lat;
  var longAdd = location.lng;

  const ENDPOINT = "https://api.cs11-ai-avs.live";
  function handleSubmit(event) {
    // Check if the user's login details are correct using Flask
    // If the details are correct, navigate to the appropriate page

    if (!validateEmail(email)) {
      // handle invalid email address
      var warn = document.getElementById("warningmail");
      warn.style.opacity = "1";

      return;
    }
    event.preventDefault();
    const data = {
      email,
      hashedPass,
      userType,
    };
    fetch(ENDPOINT + "/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then(async (response) => {
        var locc = document.getElementById("location");

        if (response.ok) {
          // handle successful response
          console.log("pass");
          const res = await response.text();
          userSessionID = JSON.parse(res)["userSessionKey"];
          setData(userSessionID);

          if (userType === "student") {
            if (latAdd == 7.1237632 && longAdd == 80.0620544) {
              // if(true){

              // Navigate to the student page
              console.log(userSessionID);
              navigate({
                pathname: "/student",
                search: createSearchParams({
                  userSessionID: userSessionID,
                  email: email,
                }).toString(),
              });
              warn.style.opacity = 0;
            } else {
              locc.style.opacity = 1;
            }
          }
          if (userType === "lecturer") {
            // Navigate to the lecturer page
            console.log(userSessionID);

            navigate({
              pathname: "/lecturer",
              search: createSearchParams({
                userSessionID: userSessionID,
              }).toString(),
            });

            warn.style.opacity = 0;
          }
        } else {
          // handle error response
          console.log("fail, invalid user");
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

  return (
    <div className="flex flex-col md:flex-row h-screen">
      <div className="half md:w-1/2 flex  justify-around  items-center ">
        <div className="flex justify-around   w-full  ">
          <div
            id="stu"
            className="md:w-1/2 flex flex-col   md:items-center justify-center items-center "
            onClick={() => handleUserTypeClick("student")}
          >
            <User photo={UserS} />
            <h1 className="text-cyan-50 font-bold">Student</h1>
          </div>
          <div
            id="lec"
            className="md:w-1/2 flex flex-col md:items-center justify-center items-center"
            onClick={() => handleUserTypeClick("lecturer")}
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
            <div className="login flex flex-col items-center justify-center ">
              <img
                src={Logo}
                alt="Lms"
                className=" lg:w-60  mb-8  md:w-full md:opacity "
              />

              <form onSubmit={handleSubmit} className="w-full max-w-md">
                <div className="mb-4">
                  <label htmlFor="email" className="block mb-2 font-bold">
                    Email
                  </label>
                  <input
                    name="email"
                    type="email"
                    placeholder="Email"
                    onChange={(event) => setemail(event.target.value)}
                    autoComplete="on"
                    className="w-full px-3 py-2 placeholder-gray-400 border rounded-lg appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                  <p id="warn" className=" text-red-600 opacity-0">
                    Invalid Email
                  </p>
                </div>

                <div className="mb-4">
                  <label htmlFor="password" className="block mb-2 font-bold">
                    Password
                  </label>
                  <input
                    name="password"
                    type="password"
                    placeholder="Password"
                    onChange={(event) => sethashedPassword(event.target.value)}
                    autoComplete="on"
                    className="w-full px-3 py-2 placeholder-gray-400 border rounded-lg appearance-none focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                  <a href="" className="text-blue-500 text-sm hover:underline">
                    Forgot Password?
                  </a>
                </div>

                <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mb-4">
                  Submit
                </button>
              </form>
              <Link
                to="/addDetails"
                className="text-blue-500 text-sm hover:underline"
              >
                {" "}
                create an account?
              </Link>

              <p
                id="location"
                className=" my-4  text-red-600 border-spacing-4 opacity-0 m-5"
              >
                <b>Location Wrong</b>{" "}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
  function validateEmail(email) {
    const re = /\S+@\S+\.\S+/;
    return re.test(email);
  }
}
export default Login;
