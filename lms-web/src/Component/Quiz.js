import React, { useState } from "react";

const Question = () => {
  const [selectedAnswer, setSelectedAnswer] = useState(null);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer);
  };

  return (
    <div className="max-w-md mx-auto p-4">
      <h2 className="text-2xl font-bold mb-4">
        What is the capital of France?
      </h2>
      <ul className="space-y-4">
        <li
          className={`py-2 px-4 rounded-md ${
            selectedAnswer === "Paris"
              ? "bg-green-500 text-white"
              : "bg-gray-200"
          }`}
          onClick={() => handleAnswerSelect("Paris")}
        >
          Paris
        </li>
        <li
          className={`py-2 px-4 rounded-md ${
            selectedAnswer === "Madrid"
              ? "bg-red-500 text-white"
              : "bg-gray-200"
          }`}
          onClick={() => handleAnswerSelect("Madrid")}
        >
          Madrid
        </li>
        <li
          className={`py-2 px-4 rounded-md ${
            selectedAnswer === "Berlin"
              ? "bg-red-500 text-white"
              : "bg-gray-200"
          }`}
          onClick={() => handleAnswerSelect("Berlin")}
        >
          Berlin
        </li>
        <li
          className={`py-2 px-4 rounded-md ${
            selectedAnswer === "Rome" ? "bg-red-500 text-white" : "bg-gray-200"
          }`}
          onClick={() => handleAnswerSelect("Rome")}
        >
          Rome
        </li>
      </ul>
    </div>
  );
};

export default Question;
