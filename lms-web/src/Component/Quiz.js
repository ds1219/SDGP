import React, { useState } from "react";

const Question = () => {
  const [selectedAnswer, setSelectedAnswer] = useState(null);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer);
  };

  return(
     <div className="  flex justify-center align-middle bg-black w-full">
       <form  
       onSubmit={handleAnswerSelect}>
         
        <h1>What's your name?</h1>
        <input 
         className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"></input>





       </form>
     </div>


  ) ;
};

export default Question;
