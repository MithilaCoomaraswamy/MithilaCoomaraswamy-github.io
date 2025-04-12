document.addEventListener('click', (e) => {  // Change this to `document` for clicks anywhere
  // Create fart image
  const img = document.createElement('img');
  img.src = 'farting.png'; // Ensure 'farting.png' is in the same folder as index.html
  img.className = 'fart';
  img.style.left = `${e.clientX - 50}px`;  // Centers the image based on the click
  img.style.top = `${e.clientY - 50}px`;   // Centers the image based on the click
  document.body.appendChild(img);

  // Remove image after 1 second
  setTimeout(() => {
    img.remove();
  }, 1000);

  // Play fart sound
  const fartSound = new Audio('Cute Pop Sound Effects.mp3'); // Ensure 'Cute Pop Sound Effects.mp3' is in the same folder
  fartSound.play().catch((error) => {
    console.error("Audio play error:", error);
  });
});
