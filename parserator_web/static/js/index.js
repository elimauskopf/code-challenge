/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
// Grab form 
const form = document.querySelector(".form");

console.log("hi")
// Send data to addressparse api
async function sendData() {

  const address = document.querySelector("#address").value
  console.log(address);
  const url = `http://localhost:8000/api/parse/?address=${address}`
   
  try {
    const response = await fetch(url, {
      method: "GET"
    });
    console.log(await response.json());
  } catch(err) {
    console.error(err);
  }

}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
});