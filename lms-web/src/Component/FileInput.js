import React, { useState } from "react";
import axios from "axios";

const ENDPOINT = "http://127.0.0.1:3669";
export default function () {
  const [lecturerID, setLecturerID] = useState("");
  const [sessionTime, setSessionTime] = useState("");
  const [sessionDate, setSessionDate] = useState("");
  const [subjectID, setSubjectID] = useState("");
  const [questionSource, setquestionSource] = useState("");

  function handleFormSubmit(event) {
    event.preventDefault();
    const data = {
      lecturerID,
      sessionTime,
      sessionDate,
      subjectID,
      questionSource,
    };
    fetch(ENDPOINT + "/startSession", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          // handle successful response
        } else {
          // handle error response
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
        className="flex flex-col "
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
          sessionTime
          <input
            name="sessionTime"
            type="time"
            value={sessionTime}
            onChange={(event) => setSessionTime(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
        <label className=" block mb-2 text-sm font-medium text-gray-900 dark:text-white ">
          sessionDate
          <input
            name="sessionDate"
            type="date"
            value={sessionDate}
            onChange={(event) => setSessionDate(event.target.value)}
            className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ></input>
        </label>
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