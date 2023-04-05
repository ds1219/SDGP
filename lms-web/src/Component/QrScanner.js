import React, { useRef, useState } from "react";
import qrcode from "qrcode";
import QrReader from "react-qr-reader";
import {
  useSearchParams,
  createSearchParams,
  useNavigate,
} from "react-router-dom";

const QRCodeEx = () => {
  const qrRef = useRef(null);
  const [fileResult, setFileResult] = useState();
  const [webcamResult, setwebcamResult] = useState();
  const [searchparams] = useSearchParams();
  const userSessionID = searchparams.get("userSessionID");
  const email = searchparams.get("email");
  var lectureSessionID = "";
  console.log("User " + userSessionID);
  console.log("lec " + lectureSessionID);
  
  const navigate = useNavigate();
  const ENDPOINT = "https://api.cs11-ai-avs.live";

  const openDialog = () => {
    qrRef.current.openImageDialog();
  };
  const fileError = (error) => {
    if (error) {
      console.log(error);
    }
  };
  const fileScan = (result) => {
    if (result) {
      setFileResult(result);
    }
  };
  const webcamError = (error) => {
    if (error) {
      console.log(error);
    }
  };
  const quizGo = (event) => {
    if (lectureSessionID != "") {
    console.log("its running");
    console.log("LectId" + lectureSessionID);
    event.preventDefault();
    const data = {
      email,
      lectureSessionID,
      userSessionID,
    };
    fetch(ENDPOINT + "/markAttendance", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
     .then(async (response) => {
       if (response.ok) {
           navigate({
             pathname: "/quiz",
             search: createSearchParams({
             lectureSessionID: lectureSessionID,
             userSessionID: userSessionID,
             email:email,
        }).toString(),
       });
      console.log("attendance passed");
     }
     else{
      console.log("attendance fail");
     }
     })

     .catch((error) => {
        // handle network error
      });

   
    }
     else {
      alert("first You need to scan the Qr code");
      console.log("first You need to scan the Qr code");
    }
  };
  const webcamScan = (result) => {
    if (result) {
      // console.log("user" + userSessionID); 
      lectureSessionID = result;
    }
  };
  return (
    <div className="container  px-4 sm:px-6 lg:px-8  bg-black h-screen">
      <div className="flex flex-col lg:flex-row items-center justify-center ">
        <div className="mx-auto lg:mx-0 mb-4 lg:mb-0">
          <div className="m-1 rounded text-center">
            <h3 className=" text-white badges bg-secondary rounded text-center text-light">
              Webcam image
            </h3>
          </div>
          <div className="text-center p-4 sm:p-8 lg:p-12 w-96">
            <QrReader
              delay={300}
              onError={webcamError}
              onScan={webcamScan}
              legacyMode={false}
              facingMode={"user"}
            />
          </div>
          <div className="rounded mb-1">
            <h5 className="text-white">
              Web cam result:{" "}
              <button
                className="cursor-pointer  text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mx-auto lg:mx-8 mb-4 lg:mb-0"
                onClick={quizGo}
              >
                Get Attendance
              </button>
            </h5>
          </div>
        </div>
      </div>
    </div>
  );
};
export default QRCodeEx;
