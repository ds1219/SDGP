let jsondata;
const ENDPOINT = "http://34.135.125.228";
fetch(ENDPOINT + "/login")
  .then(function (u) {
    return u.json();
  })
  .then(function (json) {
    jsondata = json;
    console.log(jsondata);
    console.log("runnnnn");
  });
