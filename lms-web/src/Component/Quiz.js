import React, { useState } from "react";

const Question = () => {
  const [selectedAnswer, setSelectedAnswer] = useState(null);

  const handleAnswerSelect = (answer) => {
    setSelectedAnswer(answer);
  };

  return <div className="max-w-md mx-auto p-4"></div>;
};

export default Question;
