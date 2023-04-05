import React, { useRef, useState } from "react";
import qrcode from "qrcode";
import QrReader from "react-qr-reader";
import { useLocation } from "react-router-dom";

const QRCodeEx = () => {
  const qrRef = useRef(null);
  const [fileResult, setFileResult] = useState();
  const [webcamResult, setwebcamResult] = useState();
  const location = useLocation();
  const userSessionID = location.state.userSessionID;
  console.log(userSessionID);



    // event.preventDefault();
    //        const dataMark = {
    //         email,
    //         lectureSessionID,
    //       };
    //        fetch(ENDPOINT + "/markAttendance", {
    //         method: "POST",
    //         headers: {
    //           "Content-Type": "application/json",
    //         },
    //         body: JSON.stringify(data),
    //         })
 
  

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
  const webcamScan = (result) => {
    if (result) {
      setwebcamResult(result);
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
              <a
                href={webcamResult}
                className=" cursor-pointer  text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mx-auto lg:mx-8 mb-4 lg:mb-0 "
              >
                <b>Link</b>
              </a>
            </h5>
          </div>
        </div>
      </div>
    </div>
  );
};
export default QRCodeEx;
