import React, { useState, useEffect } from 'react';
const API_KEY = 'YOUR_API_KEY_HERE';
export default function(){
    const [location, setLocation] = useState({});
  const [address, setAddress] = useState('');

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

  
  return (
    <div>
      <button onClick={handleClick}>Get Location</button>
      <br />
      {location.lat ? (
        <div>
          <p>
            Latitude: {location.lat}
            <br />
            Longitude: {location.lng}
          </p>
          <p>Address: {address}</p>
        </div>
      ) : (
        <p>Location not found</p>
      )}
    </div>
  );
  
};
