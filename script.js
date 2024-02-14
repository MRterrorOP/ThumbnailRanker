
document.getElementsByClassName('container-md')[0].addEventListener('click', function() {
  console.log('hello')
  document.getElementById('file').click();
});

document.getElementById('file').addEventListener('change', function() {
  // Handle the file selection here
  var selectedFile = this.files[0];
  console.log("Selected file:", selectedFile);
});