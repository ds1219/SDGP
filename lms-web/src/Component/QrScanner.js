import React, { useRef, useState } from "react";
import qrcode from "qrcode";
import QrReader from "react-qr-reader";

const QRCodeEx = () => {
    const qrRef= useRef(null);
    const [fileResult,setFileResult]=useState(); 
    const [webcamResult,setwebcamResult]=useState(); 
    const[text, setText]=useState("")
    const[imageQR, setImageQR]=useState();
    const generateQRCode=async() =>{
        const image= await qrcode.toDataURL(text)
        setImageQR(image);
    };
    const openDialog =()=>{
        qrRef.current.openImageDialog();
    }
    const fileError=(error)=>{
        if(error){
            console.log(error);
        }
    };
    const fileScan = (result)=> {
        if(result){
            setFileResult(result);
            
        }
    };
    const webcamError=(error)=>{
        if(error){
            console.log(error);
        }
    };
    const webcamScan = (result)=> {
        if(result){
            setwebcamResult(result);
        }
    };
    return  <div className="container mx-auto mt-10 px-4 sm:px-6 lg:px-8">
  <div className="flex flex-col lg:flex-row justify-center items-center">
    <h3 className="mr-0 lg:mr-9 text-center lg:text-right mb-4 lg:mb-0">Enter text for QR code</h3>
    <input type="text" className="bg-blue-500 border border-blue-500 text-white dark:text-white placeholder-blue-700 dark:placeholder-blue-500 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full lg:w-1/3 p-2.5 dark:bg-blue-500 dark:border-blue-500 mb-4 lg:mb-0" value={text} onChange={(e)=>setText(e.target.value)} />
    <button className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mx-auto lg:mx-8 mb-4 lg:mb-0" onClick={generateQRCode}>Generate QR Code</button>
  </div>
  <div className="flex flex-col lg:flex-row items-center justify-center mt-16">
    <div className="mr-0 lg:mr-12 mb-4 lg:mb-0">
      <h3 className="badges bg-secondary rounded text-center text-light">QR code image</h3>
      <div className="text-center">
        {imageQR &&(<a href={imageQR} className="w-32" download><img src={imageQR} width="80%" alt="qr code pic is here"/></a>)}
      </div>
    </div>
    {/* <div className="mb-4 lg:mb-0">
      <div className="m-1 rounded text-center">
        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={openDialog}>Open QR code file</button>
      </div>
      <div className="text-center p-4 sm:p-8 lg:p-12">
        <QrReader ref={qrRef} delay={300} onError={fileError} onScan={fileScan} legacyMode={true} />
      </div>
      <div className="card-footer rounded mb-1">
        <h5>Image result:{fileResult}</h5>
      </div>
    </div> */}
    <div className="mx-auto lg:mx-0 mb-4 lg:mb-0">
      <div className="m-1 rounded text-center">
        <h3 className="badges bg-secondary rounded text-center text-light">Webcam image</h3>
      </div>
      <div className="text-center p-4 sm:p-8 lg:p-12 w-64">
        <QrReader delay={300} onError={webcamError} onScan={webcamScan} legacyMode={false} facingMode={"user"} />
      </div>
      <div className="rounded mb-1">
        <h5>Web cam result: {webcamResult}</h5>
      </div>
    </div>
  </div>
</div>

    
};
export default QRCodeEx;
