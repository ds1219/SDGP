

    let jsondata;   
    const ENDPOINT = "http://127.0.0.1:5000";
    fetch(ENDPOINT + "/login").then(
        function(u){ return u.json();}
      ).then(
        function(json){
          jsondata = json;
           console.log(jsondata) 
           console.log("runnnnn")
        }
       
      )
      

