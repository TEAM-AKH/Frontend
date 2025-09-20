// Function to detect if an element is 100px from the bottom of the viewport
function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) + 100 &&
        rect.bottom >= 0
    );
}

// Add scroll event listener
window.addEventListener('scroll', function() {
    // Get all the sections you want to animate
    const sections = document.querySelectorAll('.section-content');

    sections.forEach(function(section) {
        if (isElementInViewport(section)) {
            section.classList.add('visible'); // Add class when in view
        }
    });
});

// Trigger scroll event on page load to apply animation if already in view
document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.section-content');
    sections.forEach(function(section) {
        if (isElementInViewport(section)) {
            section.classList.add('visible');
        }
    });
});
