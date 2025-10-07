document.getElementById("dogButton").addEventListener("click",getDog)

function getDog(){
    fetch("http://localhost:5000/api/dog")
    .then(response=> response.json())//Convert resonse to Json
    .then (data=> {
        document.getElementById("dogImage").src= data.message;
    })
    .catch(error=>console.error("Error fetching dog:",error))
}