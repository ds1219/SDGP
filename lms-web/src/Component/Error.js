import { Button } from "@material-ui/core";
import React from "react";
import {
  useSearchParams,
  createSearchParams,
  useNavigate,
} from "react-router-dom";

const ErrorPage = () => {
  const [searchparams] = useSearchParams();
  const lectureSessionID = searchparams.get("lectureSessionID");
  const userSessionID = searchparams.get("userSessionID");
  const email = searchparams.get("email");
const navigate = useNavigate();
  function naviQuiz(){
         navigate({
                pathname: "/quiz",
                search: createSearchParams({
                  userSessionID: userSessionID,
                  lectureSessionID:lectureSessionID,
                  email: email,
                }).toString(),
              });

  }
  return (
    <div className="flex flex-col justify-center items-center h-screen bg-gray-900 text-white">
      <div className="flex items-center mb-4">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-6 w-6 mr-2"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8"
          />
        </svg>
        <h1 className="text-3xl font-bold">Oops!</h1>
      </div>
      <div className="flex flex-col items-center mb-4">
        <p className="text-lg">Loading Quiz....</p>
        <p className="text-lg">Please see in a while</p>
      </div>
        <Button
        onClick={naviQuiz}>
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          Back to Home
        </Button>

      </div>

  );
};

export default ErrorPage;
