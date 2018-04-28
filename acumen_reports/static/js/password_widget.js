$(document).ready(function () {

  function myFunction() {
      var x = document.getElementById("form.password");
      if (x.type === "password") {
          x.type = "text";
      } else {
          x.type = "password";
      }
  } 
});