import React, { useState } from "react";

const Question = () => {
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleAnswerSelect = (event) => {
    setSelectedAnswer(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setIsSubmitted(true);
  };

  const correctAnswer = 'b'; 

  return(
       <div className="flex flex-col items-center justify-center h-screen bg-black">
      <div>
        <h1 className="text-3xl font-bold mb-4 text-blue-700 ">What is the capital of France?</h1>
      </div>
      <div>
        <form onSubmit={handleSubmit}>
          <div className="flex flex-col space-y-4">
            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="a"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              Paris
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="b"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              Marseille
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="c"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              Lyon
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="d"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              Toulouse
            </label>
          </div>
          <br />
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            type="submit"
            disabled={isSubmitted}
          >
            Submit
          </button>
        </form>
      </div>
       
      {isSubmitted && selectedAnswer === correctAnswer && (
        <p className=" text-white"> You got it right!</p>
      )}
      {isSubmitted && selectedAnswer !== correctAnswer && (
        <p className=" text-white">You got it wrong.</p>
      )}
    </div>

  ) ;
};

export default Question;
