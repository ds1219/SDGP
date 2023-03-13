import User from "./User";
import "../App.css";
import UserS from "../images/AdminS.png";
import UserT from "../images/AdminT.png";
import Form from "./Form";
import React from "react";

export default function () {
  const [nextpage, setNextPage] = React.useState(true);

  return (
    <div class="flex flex-col md:flex-row h-screen">
      <div class="half md:w-1/2 flex  justify-around  items-center">
        <div class="flex justify-around   w-full ">
          <div class="md:w-1/2 flex flex-col   md:items-center justify-center items-center">
            <User photo={UserS} />
            <h1 class="text-cyan-50 font-bold">Student</h1>
          </div>
          <div class="md:w-1/2 flex flex-col md:items-center justify-center items-center">
            <User photo={UserT} />
            <h1 class="text-cyan-50 font-bold">Lecturer</h1>
          </div>
        </div>
      </div>

      <div class="md:w-1/2 bg-white">
        <div class="flex items-center justify-center h-full">
          <div class="w-full md:w-3/4 lg:w-1/2">
            <Form />
          </div>
        </div>
      </div>
    </div>
  );
}
