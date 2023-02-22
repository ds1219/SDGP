import React, { useState } from "react";


export default function(){
     const [pdfFile, setPdfFile] = useState(null);

  const handleFileSelect = event => {
    setPdfFile(event.target.files[0]);
  };

  return (
  <div className="flex  justify-center items-center h-screen bg-black">
    <div>
       <input type="text"></input>
    </div>
    <div className="flex  justify-center items-center h-screen bg-black">
    
      <div className="flex flex-col justify-center items-center p-5 bg-slate-400 w-3/4 h-1/3">
      <div className="w-2/3  ">
        <input
          className="bg-gray-200 appearance-none border-2
           border-ring-blue-500 rounded w-full py-2 px-4 text-bg-blue-500 leading-tight focus:outline-none
            focus:bg-white focus:border-ring-blue-500 "
          type="file"
          onChange={handleFileSelect}
          accept="application/pdf"
        />
      </div>
      {pdfFile && (
        <embed
          className="w-64 h-64 mt-5"
          src={URL.createObjectURL(pdfFile)}
          type="application/pdf"
        />
      )}
    </div>
  </div>
  </div>
  );

}