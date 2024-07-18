// Grab form and needed tags
form = document.querySelector(".form")
errorDiv = document.getElementById('error')
addressDiv = document.getElementById('address-results')

// Send data to addressparse api
async function sendData() {

  address = document.querySelector("#address").value
 
  url = `http://localhost:8000/api/parse/?address=${address}`
   
  try {
    const response = await fetch(url, {
      method: "GET"
    });

    let data = await response.json()

    if (data.detail) {
      throw new Error(data.detail)
    } else {
      populateTable(data)
    }
   
  } catch(err) {
    displayError(err)
  }

   

}

// Fill table with data from api
function populateTable(data) {
 
   // Hide error div as a precaution

   errorDiv.style.display= 'none'

   // Unhide address div
   let addressDiv = document.getElementById('address-results')
   addressDiv.style = ''

   // Add data to div
   document.getElementById('parse-type').innerHTML = `${data.address_type}`
   let tableBody = document.getElementById('address-Table')
   let htmlToAdd = ``
  
   
   for ( [tag,address] of Object.entries(data.address_components)) {

     htmlToAdd += `<tr>
                       <td> ${address }</td>
                       <td> ${tag }</td>
                    <tr>`
    
   }

   tableBody.innerHTML = htmlToAdd
}

// Hide Table and display error message
function displayError(err) {
   
   addressDiv.style.display= 'none'
   errorDiv.style = ''

   errorDiv.innerHTML = `${err}`
}

// Subsribe function to submit button
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
});