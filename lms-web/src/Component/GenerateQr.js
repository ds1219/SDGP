
import React, { useState, useEffect } from "react";
import qrcode from "qrcode";


const GenerateQRCode=()=>{
   const [imageQR, setImageQR] = useState();
   const [qrValue, setQRValue] = useState("");
   const [text, setText] = useState("");
  

   const generateQRCode = async () => {

  setQRValue(text); // store the current QR code value
  if(text!=""){
   const image = await qrcode.toDataURL(text);
    setImageQR(image);
   
  }
  else{
    console.log("fill the text field")
  }

  setTimeout(() => {
    setQRValue(""); // clear the QR code value after 30 seconds
  }, 30000);
};

// If qrValue is empty, display an empty QR code
// Otherwise, display the generated QR code
const qrCode = qrValue ? (
  <img src={imageQR} alt="QR code" />
) : (
  <div className="empty-qr-code">QR code will be generated after entering text</div>
);


return (
  <div className=" bg-black h-screen">
  <div className="flex flex-col lg:flex-row items-center justify-center container   ">
    <div  id="inn" className="flex flex-col lg:flex-row justify-center items-center m-12">
      <h3 className="text-white mr-0 lg:mr-9 text-center lg:text-right mb-4 lg:mb-0">
        Enter text for QR code
      </h3>
      <input
       
        type="text"
        className="bg-blue-500 border border-blue-500 text-white dark:text-white placeholder-blue-700 dark:placeholder-blue-500 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full lg:w-1/3 p-2.5 dark:bg-blue-500 dark:border-blue-500 mb-4 lg:mb-0"
        value={text}
        onChange={(e) => {if(e.target.value!=""){
            setText(e.target.value)
        }}
    }
      />
       {/* <h3 className="text-white mr-0 lg:mr-9 text-center lg:text-right mb-4 lg:mb-0">
        Enter Session Code
      </h3> */}
         {/* <input
       
        type="text"
        className="bg-blue-500 border border-blue-500 text-white dark:text-white placeholder-blue-700 dark:placeholder-blue-500 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full lg:w-1/3 p-2.5 dark:bg-blue-500 dark:border-blue-500 mb-4 lg:mb-0"
        value={text}
      
      /> */}
      <button
        className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mx-auto lg:mx-8 mb-4 lg:mb-0"
        onClick={generateQRCode}
      >
        Generate QR Code
      </button>
    </div>
     {/* <div className="mr-0 lg:mr-12 mb-4 lg:mb-0">
          <h3 className=" text-white badges bg-secondary rounded text-center text-light">
            QR code image
          </h3>
          <div className="text-center">
            {imageQR && (
              <a href={imageQR} className="w-32" download>
                <img src={imageQR} width="90%" alt="qr code pic is here" />
              </a>
            )}
          </div>
        </div> */}
   
  </div>
   <div className="qr-code-container  flex justify-center items-center  ">{qrCode}</div>
  </div>
);






}

export default GenerateQRCode