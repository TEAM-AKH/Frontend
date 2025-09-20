document.addEventListener('DOMContentLoaded', function() {
  const sliderWrapper = document.getElementById('slider-wrapper');
  
  // Check if the slider wrapper exists before proceeding
  if (!sliderWrapper) {
    console.log('Slider wrapper not found, skipping image slider initialization');
    return;
  }
  
  const images = sliderWrapper.querySelectorAll('img');
  
  // Check if there are any images to slide
  if (images.length === 0) {
    console.log('No images found in slider wrapper');
    return;
  }
  
  let currentIndex = 0;
  const imageCount = images.length;
  let isTransitioning = false;

  function showImage(index) {
    if (isTransitioning) return; // Prevent changes during animation

    isTransitioning = true;

    // Set all images to initial state (opacity 0, hidden position)
    images.forEach(image => {
      image.style.opacity = 0; // Set opacity to 0 for all images
      image.style.transition = 'opacity 1s ease-in-out, transform 1s ease-in-out'; // Smooth opacity and sliding transition
      image.style.transform = 'translateX(100%)'; // Start position for sliding out (to the right)
      image.style.display = 'none'; // Hide all images initially
    });

    // Show the current image and apply fade-in and sliding effect
    const currentImage = images[index];
    currentImage.style.display = 'block'; // Display the current image
    currentImage.style.opacity = 1; // Fade in the current image
    currentImage.style.transform = 'translateX(0)'; // Slide in the current image to its original position

    // Wait for the transition to finish before allowing another change
    setTimeout(() => {
      isTransitioning = false;
    }, 1000); // Match the transition duration
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % imageCount;
    showImage(currentIndex);
  }

  // Initialize the first image
  showImage(currentIndex);

  // Auto transition between images every 3.5 seconds
  setInterval(nextImage, 3500);
});