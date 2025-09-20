document.addEventListener("DOMContentLoaded", () => {
    // Get the current page's filename
    const currentPage = window.location.pathname;
    // Select all nav links
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
  
    navLinks.forEach((link) => {
      // Extract the href filename for comparison
      const linkPage = link.getAttribute("href");
      // Check if the href matches the current page
      if (linkPage === currentPage) {
        // Add the 'active' class to the matching nav link
        link.classList.add("active");
      
      }
      else if(currentPage=="/expertise/" && linkPage=="/service/"){
        link.classList.add("active")
      }
    });
  });
  