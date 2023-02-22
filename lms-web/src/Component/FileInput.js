import React, { useState } from "react";


export default function(){
     const [pdfFile, setPdfFile] = useState(null);

  const handleFileSelect = event => {
    setPdfFile(event.target.files[0]);
  };

  return (
<div className="flex justify-center items-center h-screen bg-black">
  <div className="w-11/12 md:w-2/3 lg:w-1/2">
    <input
      className="w-full py-2 px-4 bg-gray-200 appearance-none border-2 border-ring-blue-500 rounded text-bg-blue-500 leading-tight focus:outline-none focus:bg-white focus:border-ring-blue-500"
      type="text"
    />
  </div>
  <div className="flex justify-center items-center h-screen bg-black">
    <div className="w-11/12 md:w-2/3 lg:w-1/2 flex flex-col justify-center items-center p-5 bg-slate-400">
      <div className="w-11/12 md:w-3/4">
        <input
          className="w-full py-2 px-4 bg-gray-200 appearance-none border-2 border-ring-blue-500 rounded text-bg-blue-500 leading-tight focus:outline-none focus:bg-white focus:border-ring-blue-500"
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