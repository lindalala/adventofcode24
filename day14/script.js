let currentStep = 0;
let coords = []; // Array to store coordinates from JSON
let WIDTH = 101
let HEIGHT = 103
let intervalId = null; // Variable to hold the interval ID

// Function to create the 101x103 grid
function createGrid() {
  const gridContainer = document.getElementById('grid-container');
  gridContainer.innerHTML = ""; // Clear previous cells
  for (let i = 0; i < HEIGHT; i++) {
    for (let j = 0; j < WIDTH; j++) {
      const cell = document.createElement('div');
      cell.className = 'grid-item';
      cell.id = `cell-${j}-${i}`;
      gridContainer.appendChild(cell);
    }
  } 
}

// Function to fetch JSON data
async function fetchData() {
  const response = await fetch('starts.json');
  coords = await response.json();
}

// Function to calculate new positions based on currentStep
function calculateNewPositions() {
  const newCoords = coords.map(point => {
    const newX = ((point.x + currentStep * point.vX) % WIDTH + WIDTH) % WIDTH; 
    const newY = ((point.y + currentStep * point.vY) % HEIGHT + HEIGHT) % HEIGHT;
    return { x: newX, y: newY };
  });
  return newCoords;
}

// Function to visually update the grid based on the calculated positions
function updateGrid() {
  const newCoords = calculateNewPositions();

  // First, clear all cells
  for (let i = 0; i < HEIGHT; i++) {
    for (let j = 0; j < WIDTH; j++) {
      const cell = document.getElementById(`cell-${j}-${i}`);
      if (cell) {
        cell.style.backgroundColor = "white";
      } else {
        console.log(`Invalid clearing for cell (${i},${j})`)
      }
    }
  }
  // Update only the active cells to green
  newCoords.forEach(coord => {
    const cell = document.getElementById(`cell-${coord.x}-${coord.y}`);
    if (cell) {
      cell.style.backgroundColor = "green";
    } else {
      console.log(`Invalid green for cell (${coord.x},${coord.y})`)
    }
  });
}

// Function to set the step from input field
function setStep() {
  const stepInput = document.getElementById('step-input');
  const value = parseInt(stepInput.value, 10);
  currentStep = value;
  document.getElementById('step-display').innerText = currentStep;
  updateGrid();
}

// Function to dynamically adjust the slider step
function updateSlider() {
  const slider = document.getElementById('step-slider');
  currentStep = parseInt(slider.value, 10);
  document.getElementById('step-display').innerText = currentStep;
  updateGrid();
}

// Handle right arrow key press for incrementing the step
document.addEventListener('keydown', (event) => {
  if (event.key === "ArrowRight") { 
    incrementStepOnce();
  }
  if (event.key === "ArrowLeft") { 
    decrementStepOnce();
  }
});

// Function to increment the step by 1
function incrementStepOnce() {
  currentStep += 1;
  document.getElementById('step-display').innerText = currentStep;
  document.getElementById('step-slider').value = currentStep;
  updateGrid();
}

// Function to decrement the step by 1
function decrementStepOnce() {
  currentStep -= 1;
  document.getElementById('step-display').innerText = currentStep;
  document.getElementById('step-slider').value = currentStep;
  updateGrid();
}

// Function to increment the step by 1
function incrementStep() {
  const button = document.getElementById('increment');
  if (intervalId === null) {
    // Start the interval
    intervalId = setInterval(incrementStepOnce, 1000); // Call incrementStep every 1 second
    button.innerText = "Stop"; // Update button text
  } else {
    // Stop the interval
    clearInterval(intervalId);
    intervalId = null;
    button.innerText = "Start"; // Update button text
  }
}

// Initialize the grid when the page is first loaded
async function initialize() {
  await fetchData();
  createGrid();
  updateGrid();
}

initialize();