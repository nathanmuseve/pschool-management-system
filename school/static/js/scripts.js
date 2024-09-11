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

// toggle menu 
let head = document.getElementById('head');
let nav = document.getElementById('nav1');
let menu = document.getElementById('menu');

menu.addEventListener('click', function() {
  if (nav.style.display == 'none') {
    nav.style.display = "flex";
  } else {
    nav.style.display = "none";
  }
  if (head.style.height == '75px') {
    head.style.height = "300px";
  } else {
    head.style.height = "75px";
  }
});

// make active link with different color 
function makeLinkActive(link) {
  // Remove the 'active' class from all links
  const alllinks = document.querySelectorAll('a');
  alllinks.forEach(link => link.classList.remove('active'));

  // Add the 'active' class to the clicked link
  link.classList.add('active');
}

// Add an event listener to all links
const links = document.querySelectorAll('a');
links.forEach(link => link.addEventListener('click', () => makeLinkActive(link)));