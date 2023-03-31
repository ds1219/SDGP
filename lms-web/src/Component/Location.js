import React, { useState, useEffect } from "react";
const API_KEY = "";
export default function () {
  const [location, setLocation] = useState({});
  const [address, setAddress] = useState("");

  const handleClick = () => {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        setLocation({
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
      },
      (error) => {
        console.error(error);
      },
      { enableHighAccuracy: true, timeout: 20000, maximumAge: 1000 }
    );
  };
  useEffect(() => {
    handleClick();
  }, []);

  useEffect(() => {
    if (!location.lat) {
      return;
    }

    fetch(
      `https://maps.googleapis.com/maps/api/geocode/json?latlng=${location.lat},${location.lng}&key=${API_KEY}`
    )
      .then((response) => response.json())
      .then((data) => {
        setAddress(data.results[0].formatted_address);
      });
  }, [location]);
  var latAdd = location.lat;
  var longAdd = location.lng;
  var Addresss = address;

  return (
    <div>
      {/* <button onClick={handleClick}>Get Location</button> */}
      <br />
      {location.lat ? (
        (console.log(latAdd), console.log(longAdd), console.log(address))
      ) : (
        <p>Location not found</p>
      )}
    </div>
  );
}
