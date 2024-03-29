import React, { useState } from "react";
import {
  useLocation,
  useNavigate,
  Link,
  json,
  createSearchParams,
  useSearchParams,
} from "react-router-dom";

const ENDPOINT = "https://api.cs11-ai-avs.live";
export default function () {
  const [lecturerID, setLecturerID] = useState("");
  const [sessionStartOnly, setsessionStart] = useState("");
  const [sessionEndOnly, setsessionEnd] = useState("");
  const [subjectID, setSubjectID] = useState("");
  const [questionSource, setquestionSource] = useState("");
  const [date, setDate] = useState("");

  const [searchparams] = useSearchParams();
  const userSessionID = searchparams.get("userSessionID");
  let lectureSessionID = "";

  const navigate = useNavigate();

  function handleFormSubmit(event) {
   
   var newdate = date.split("/").reverse().join("-");
   const sessionStart=newdate+" "+sessionStartOnly;
   const sessionEnd=newdate+" "+sessionEndOnly;
   console.log(sessionStart+" "+sessionEnd)
    event.preventDefault();
    const data = {
      lecturerID,
      sessionStart,
      sessionEnd,
      subjectID,
      questionSource,
      userSessionID,
    };
    fetch(ENDPOINT + "/startSession", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then(async (response) => {
        if (response.ok) {
          // handle successful response
          const res = await response.text();
          lectureSessionID = JSON.parse(res)["lectureSessionID"];
          console.log("lec  " +lectureSessionID);
          navigate({
            pathname: "/generateqr",
            search: createSearchParams({
              lectureSessionID: lectureSessionID,
            }).toString(),
          });

          console.log(lectureSessionID);
        } else {
          // handle error response
          console.log("fail");
        }
      })
      .catch((error) => {
        // handle network error
      });
  }

  return (
    <div className="flex justify-center items-center h-screen bg-black">
      <form
        method="POST"
        className="flex flex-col  w-4/5 max-w-md"
        onSubmit={handleFormSubmit}
      >
        {/* <select className="w-full p-2.5 text-gray-500 bg-white border rounded-md shadow-sm outline-none appearance-none focus:border-indigo-600">

       <option value="fruit">Client Server Architecture</option>

       <option value="vegetable">Module2</option>

       <option value="meat">Module3</option>

     </select> */}

        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          lecturerID
          <input
            name="lecturerID"
            value={lecturerID}
            onChange={(event) => setLecturerID(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          sessionStart
          <input
            name="sessionStartOnly"
            type="time"
            value={sessionStartOnly}
            onChange={(event) => setsessionStart(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          sessionEnd
          <input
            name="sessionEndOnly"
            type="time"
            value={sessionEndOnly}
            onChange={(event) => setsessionEnd(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
         <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          sessionDate
          <input
            name="date"
            type="date"
            value={date}
            onChange={(event) => setDate(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        {/* <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          sessionDate
          <input
            name="sessionDate"
            type="date"
            value={sessionDate}
            onChange={(event) => setSessionDate(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label> */}
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          subjectID
          <input
            name="subjectID"
            value={subjectID}
            onChange={(event) => setSubjectID(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>

        <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          Lecture Notes
          <textarea
            value={questionSource}
            onChange={(event) => setquestionSource(event.target.value)}
            className="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            name="postContent"
            rows={8}
            cols={60}
          />
        </label>
        <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg mb-4">
          Generate Quiz
        </button>
      </form>

      {/* <div className="w-11/12 md:w-2/3 lg:w-1/2">
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
  </div> */}
    </div>
  );
}
