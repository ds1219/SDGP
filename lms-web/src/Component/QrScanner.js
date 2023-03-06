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
<<<<<<< Updated upstream
    return  <div className="container mx-auto mt-10 px-4 sm:px-6 lg:px-8">
=======
//     return <div className="container mx-auto mt-10">
   
//   <div className="flex justify-center items-center">
//     <h3 className=" mr-9">Enter text for QR code</h3>
//     <input type="text" className="bg-blue-500 border border-blue-500 text-white-900 dark:text-white-900 placeholder-blue-700 dark:placeholder-blue-500 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-1/3 p-2.5 dark:bg-blue-500 dark:border-blue-500" value={text} onChange={(e)=>setText(e.target.value)} />
//     <button className="text-white  bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mx-8 " onClick={generateQRCode}>Generate QR Code</button>
//   </div>
//   <div className="flex  justify-center  mt-16 ">
//     <div className=" mr-12">
      
//         <h3 className="badges bg-secondary rounded text-center text-light">QR code image</h3>
      
//       <div className=" text-center w-32">
//         {imageQR &&(<a href={imageQR} className="w-32" download><img src={imageQR} width="80%" alt="qr code pic is here"/></a>)}
//       </div>
//     </div>
//     <div className="">
//       <div className=" m-1 rounded text-center">
//         <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={openDialog}>Open QR code file</button>
//       </div>
//       <div className="text-center p-4 w-60 ">
//         <QrReader ref={qrRef} delay={300} onError={fileError} onScan={fileScan} legacyMode={true} />
//       </div>
//       <div className="card-footer rounded mb-1">
//         <h5>Image result:{fileResult}</h5>
//       </div>
//     </div>
//     <div className=" w-60 mx-11">
//       <div className=" m-1 rounded">
//         <h3 className="badges bg-secondary rounded text-center text-light">Webcam image</h3>
//       </div>
//       <div className=" text-center">
//         <QrReader delay={300} onError={webcamError} onScan={webcamScan} legacyMode={false} facingMode={"user"} />
//       </div>
//       <div className="rounded mb-1">
//        {/* <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center mr-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
//        <svg aria-hidden="true" class="w-5 h-5 mr-2 -ml-1" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"></path></svg>
//         Buy now
//        </button> */}
//         <h5>Web cam result: {webcamResult}</h5>
//       </div>
//     </div>
//   </div>
// </div>
return <div className="container mx-auto mt-10 px-4 sm:px-6 lg:px-8">
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    {/* <div className="mb-4 lg:mb-0">
=======
    <div className="mb-4 lg:mb-0">
>>>>>>> Stashed changes
      <div className="m-1 rounded text-center">
        <button className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" onClick={openDialog}>Open QR code file</button>
      </div>
      <div className="text-center p-4 sm:p-8 lg:p-12">
        <QrReader ref={qrRef} delay={300} onError={fileError} onScan={fileScan} legacyMode={true} />
      </div>
      <div className="card-footer rounded mb-1">
        <h5>Image result:{fileResult}</h5>
      </div>
<<<<<<< Updated upstream
    </div> */}
=======
    </div>
>>>>>>> Stashed changes
    <div className="mx-auto lg:mx-0 mb-4 lg:mb-0">
      <div className="m-1 rounded text-center">
        <h3 className="badges bg-secondary rounded text-center text-light">Webcam image</h3>
      </div>
<<<<<<< Updated upstream
      <div className="text-center p-4 sm:p-8 lg:p-12 w-64">
=======
      <div className="text-center p-4 sm:p-8 lg:p-12">
>>>>>>> Stashed changes
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
