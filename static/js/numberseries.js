const target = 15000; // Final number
const duration = 1100; // Duration in milliseconds (2 seconds)
const interval = 10; // Update interval in milliseconds
const step = target / (duration / interval); // Calculate increment per step

let currentNumber = 0;

const incrementNumber = setInterval(() => {
  currentNumber += step;
  if (currentNumber >= target) {
    currentNumber = target; // Ensure it stops exactly at 15000
    clearInterval(incrementNumber);
  }
  document.getElementById("number").textContent = Math.floor(currentNumber) + " +";
}, interval);