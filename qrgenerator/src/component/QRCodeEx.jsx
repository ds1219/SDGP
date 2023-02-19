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
    return <div  classname="container mx-auto mt-4">
        <div className="row">
            <h2 className="col-sm-12 badges bg-danger text-center">Qr Code Generator</h2>
        </div>
        <div className="row">
            <h3 className="col-sm-12 ">
                Enter text for QR code</h3> 
        </div>
        <div className="row">
            <input type="text" className="col-sm-5 m-2" value={text} onChange={(e)=>setText(e.target.value)}
            />
            <button className="col-sm-2 btn btn-primary m-2" onClick={generateQRCode}>Generate QR Code</button>
        </div>
        <div className="row">
            <div className="card col-sm-4">
                <div className="card-header m-1 rounded">
                    <h3 className="badges bg-secondary rounded text-center text-light">
                        QR code image
                    </h3>
                </div>
                <div className="card-body text-center">
                    {imageQR &&(<a href= {imageQR}download> <img src={imageQR}width="70%" alt="qr code pic is here"/></a>)}
                </div>
            </div>
            <div className="card col-sm-4">
                <div className="card-header m-1 rounded text-center">
                    <button className="btn btn-warning rounded text-center text-light" onClick={openDialog}>
                        Open QR code file
                    </button>
                </div>
                <div className="card-body text-center">
                    <QrReader 
                    ref={qrRef} 
                    delay={300} 
                    onError={fileError} 
                    onScan={fileScan}
                    legacyMode={true}
                     />
                </div>
                <div className="card-footer rounded mb-1">
                    <h5>Image result:{fileResult}</h5>
                </div>
            </div>
            <div className="card col-sm-4">
                <div className="card-header m-1 rounded">
                    <h3 className="badges bg-secondary rounded text-center text-light">
                        Webcam image
                    </h3>
                </div>
                <div className="card-body text-center">
                <QrReader  
                    delay={300} 
                    onError={webcamError} 
                    onScan={webcamScan}
                    legacyMode={false}
                    facingMode={"user"}
                     />
                </div>
                <div className="card-footer rounded mb-1">
                    <h5>Web cam result: {webcamResult}</h5>
                </div>
            </div>
        </div>
    </div>
    
};
export default QRCodeEx;