const urlofimg = document.getElementById('urlofimg');
const title = document.getElementById('title');
const img1 = document.getElementById('img1');

document
.getElementById("myform")
.addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent default form submission

  // Collect form data
  const formData = new FormData(this);

  // Send data to Flask backend using Fetch API
  fetch("/submit-form", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle server response
      console.log( data.title);
      console.log( data.url);

      
      
      // Update UI or display success/error message
    })
    .catch((error) => {
      // Handle errors
      console.error("Error:", error);
    });
});

