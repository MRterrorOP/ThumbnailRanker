const urlofimg = document.getElementById('urlofimg');
const title = document.getElementById('title');
const img1 = document.getElementById('img1');
const rankDisplayer = document.getElementById('rankDisplayer')

function getDataFromDb(){
fetch('http://127.0.0.1:5000/get-images')
.then(response => response.json())
.then(data => onload(showImage(data)))}
// setInterval(showImage, 5000)}

window.onload = function(){
  getDataFromDb()
  showCampaireImages()
}
function showImage(data ){
  for (let i= 0; i <= data.length ; i++  ){  
  value = data.length
  let image = document.createElement('img')
  image.setAttribute('src' ,data[i][1])
  image.setAttribute('width' , '200')
  image.setAttribute('class', 'responsive-img')
  rankDisplayer.appendChild(image)

  }
}

const image1 = document.getElementById("img1");
const image2 = document.getElementById("img2");
const heading1 = document.getElementById("heading-1");
const heading2 = document.getElementById("heading-2");

async function showCampaireImages() {
  const response = await fetch('http://127.0.0.1:5000/get-compare-images');
  const data = await response.json();
  console.log(data)
  image1.setAttribute("src", data[0][2])
  image2.setAttribute("src", data[1][2])
  image1.onclick = () => createAndSubmitForm(data[0][0], data[1][0])
  image2.onclick = () => createAndSubmitForm(data[1][0], data[0][0])
  heading1.innerText = data[0][1]
  heading2.innerText = data[1][1]
}

// async function handleOnClick(selectedId, remainingId) {
//   const data = new FormData()
//   data.set("selectedId", selectedId)
//   data.set("remainingId", remainingId)

//   const response = await fetch("http://127.0.0.1:5000/post-image-vote", {
//     method: "POST",
//     body: data
//   })

//   if(!response.ok){
//     console.log("error happens", await response.text())
//   }

//   const res = await response.json();
//   console.log(res.status);

// }
function createAndSubmitForm(selectedID, remainingID) {
  // Create a new FormData object
  var formData = new FormData();

  // Add data to the FormData object
  formData.append('selectedID', selectedID); // Example value
  formData.append('remainingID', remainingID); // Example value

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Open a POST request to the server endpoint
  xhr.open('POST', '/post-image-vote');

  // Set up a callback function to handle the response
  xhr.onload = function() {
      if (xhr.status === 200) {
          console.log('Form submitted successfully');
      } else {
          console.error('Form submission failed');
      }
  };

  // Send the FormData object as the request body
  xhr.send(formData);
}
