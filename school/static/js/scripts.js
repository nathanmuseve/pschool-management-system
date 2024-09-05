// Optional: Adding JavaScript to handle click events for better mobile support
document.addEventListener("DOMContentLoaded", function () {
  var dropdownContainer = document.querySelector(".dropdown-container");

  dropdownContainer.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default anchor behavior
    this.querySelector(".dropdown").classList.toggle("show");
  });

  // Close the dropdown if the user clicks outside of it
  document.addEventListener("click", function (event) {
    if (!dropdownContainer.contains(event.target)) {
      dropdownContainer.querySelector(".dropdown").classList.remove("show");
    }
  });
});
