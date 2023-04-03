import logo from "./logo.svg";
import "./App.css";
import Back from "./images/BG.jpg";
import Login from "./Component/Login";
import Location from "./Component/Location";
import FileInput from "./Component/FileInput";
import AddDetails from "./Component/AddDetails";
import ForgotPassword from "./Component/ForgetPassword";
import GenerateQRCode from "./Component/GenerateQr";
import {
  Route,
  Routes,
  Link,
  RouterProvider,
  createBrowserRouter,
} from "react-router-dom";
import QrScanner from "./Component/QrScanner";
import Question from "./Component/Quiz";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/lecturer" element={<FileInput />} />
      <Route path="/student" element={<QrScanner />} />
      <Route path="/quiz" element={<Question />} />
      <Route path="/location" element={<Location />} />
      <Route path="/addDetails" element={<AddDetails />} />
      <Route path="/forgetPassword" element={<ForgotPassword />} />
       <Route path="/generateqr" element={<GenerateQRCode />} />
    </Routes>
  );
}

export default App;
