window.addEventListener('load', function() {
  document.getElementById('pic').addEventListener('change', function() {
      if (this.files && this.files[0]) {
          var img = document.querySelector('img'); 
           // $('img')[0]
          img.src = URL.createObjectURL(this.files[0]); 
          // set src to blob url
          img.onload = imageIsLoaded;
      }
  });
});

function imageIsLoaded() { 
  alert("Image uploaded successfully!!!");  // blob url
  // update width and height ...
}

