import React, { useState } from "react";


export default function(){
     const [pdfFile, setPdfFile] = useState(null);

  const handleFileSelect = event => {
    setPdfFile(event.target.files[0]);
  };

  return (
    <div className="flex flex-col items-center p-5">
      <div className="w-64">
        <input
          className="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500"
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
  );

}