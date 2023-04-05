import React, { useState } from "react";
import {
  useSearchParams,
  createSearchParams,
  useNavigate,
} from "react-router-dom";

const Question = () => {
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [questions,setquestion]=useState("");
  const [answers,setanswer]=useState("");
  const [wronganswer1,setwronganswer1]=useState("");
  const [wronganswer2,setwronganswer2]=useState("");
  const [wronganswer3,setwronganswer3]=useState("");
  const ENDPOINT = "https://api.cs11-ai-avs.live";

  const [searchparams] = useSearchParams();
  const lectureSessionID = searchparams.get("lectureSessionID");
  const userSessionID = searchparams.get("userSessionID");
  const email = searchparams.get("email");
  var questionID="";
  var question=""
  var answer="";
  var wronganswer="";
  // var wronganswer1="";
  // var wronganswer2="";
  // var wronganswer3="";
  var result="";


      const data = {
      lectureSessionID,
      userSessionID,
   
      };

      fetch(ENDPOINT + "/getQuestion", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
     .then(async (response) => {
        if (response.ok) {
          // handle successful response
         ;
          const res = await response.text();
          questionID = JSON.parse(res)["questionID"];
          //  console.log("Question Id "+questionID);
          question = JSON.parse(res)["question"];
          setquestion(question);
          // console.log("Question  "+questions);
          answer = JSON.parse(res)["answer"];
          setanswer(answer);
          //  console.log("answr  "+answer);
          wronganswer = JSON.parse(res)["wronganswer"];
          var newWronganswer=wronganswer.split("|");
          setwronganswer1(newWronganswer[0]);
          setwronganswer2(newWronganswer[1]);
          // console.log(newWronganswer[1])
          setwronganswer3(newWronganswer[2]);
          

        }
         else {
          // handle error response
          console.log("fail, invalid Quiz data");
        }
      })
      .catch((error) => {
        // handle network error
      });

  const handleAnswerSelect = (event) => {
    setSelectedAnswer(event.target.value);
    if(selectedAnswer==answer){
        result="Pass"
    }
    else{
      result="Fail"
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    setIsSubmitted(true);
      const data = {
      questionID,
      email,
      result,
   
    };

      fetch(ENDPOINT + "/submitAnswer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
     
     .then(async (response) => {
        if (response.ok) {
      console.log("Results passed");
     }
     else{
      console.log("results fail");
     }
     })

     .catch((error) => {
        // handle network error
      });

  };

  const correctAnswer = answer; 

  return(
       <div className="flex flex-col items-center justify-center h-screen bg-black">
      <div>
        <h1 className="text-3xl font-bold mb-4 text-blue-700 ">{questions}</h1>
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
              {answers}
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="b"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
             {wronganswer1}
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="c"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              {wronganswer2}
            </label>

            <label className="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded cursor-pointer">
              <input
                type="radio"
                name="answer"
                value="d"
                onChange={handleAnswerSelect}
                disabled={isSubmitted}
              />
              {wronganswer3}
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
