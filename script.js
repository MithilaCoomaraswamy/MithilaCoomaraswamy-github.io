document.body.addEventListener('click', (e) => {
  // Create fart image
  const img = document.createElement('img');
  img.src = 'https://emoji.slack-edge.com/T01234567/fart/abc123.png'; // OR your own fart image URL
  img.className = 'fart';
  img.style.left = `${e.clientX - 50}px`;
  img.style.top = `${e.clientY - 50}px`;
  document.body.appendChild(img);

  // Remove image after 1 second
  setTimeout(() => {
    img.remove();
  }, 1000);

  // Play sound
  const fartSound = new Audio('fart.mp3');
  fartSound.play();
});
