document.addEventListener("DOMContentLoaded", () => {
  console.log("Got here: ");
  // Get the canvas element and its context

  canvas = document.getElementById("canvas");
  ctx = canvas.getContext("2d");

  const width = 1200;
  const height = 1000;

  let mouseY = 0;
  let mouseX = 0;
  
  let bullets = [];

  canvas.addEventListener("mousemove", (event) => {
    const rect = canvas.getBoundingClientRect();
    mouseX = event.clientX - rect.left;
    mouseY = event.clientY - rect.top;
  });

  // Set the background
  
  function drawScene() {
    canvas.style.cursor = 'none'
    ctx.fillStyle = "#000"; // Black color for space background
    ctx.fillRect(0, 0, width, height); // Fill the canvas with black
  }

  function drawCannon() {
    ctx.fillStyle = "#333"; // Dark grey color
    ctx.fillRect(width / 2 - 50, height - 100, 100, 100); // Draw a rectangle for the base

    // Draw the cannon barrel
    ctx.fillStyle = "#555"; // Lighter grey color
    ctx.fillRect(width / 2 - 5, height - 120, 10, 70); // Draw a smaller rectangle for the barrel

    // Draw the cannon's muzzle
    ctx.beginPath();
    ctx.arc(width / 2, height - 120, 5, 0, Math.PI, true); // Half-circle for the muzzle
    ctx.fill();

    // Optionally add some details
    ctx.fillStyle = "#999"; // Even lighter grey for details
    ctx.fillRect(width / 2 - 40, height - 50, 10, 10); // Control panel
    ctx.fillRect(width / 2 + 30, height - 50, 10, 10); // Power unit

    // Draw the outline of the cannon for better visibility
    ctx.strokeStyle = "red"; // Black color for the outline
    ctx.lineWidth = 2;
    ctx.strokeRect(width / 2 - 5, height - 120, 10, 70); // Outline for the barrel
    ctx.beginPath();
    ctx.arc(width / 2, height - 120, 5, 0, Math.PI, true); // Outline for the muzzle
    ctx.stroke();
  }

  function drawCrosshair() {
    ctx.beginPath();
    ctx.moveTo(mouseX - 15, mouseY);
    ctx.lineTo(mouseX + 15, mouseY);
    ctx.moveTo(mouseX, mouseY - 15);
    ctx.lineTo(mouseX, mouseY + 15);
    ctx.strokeStyle = "red";
    ctx.lineWidth = 1;
    ctx.stroke();
  }

// Modified shoot function that calculates the bullet's trajectory based on mouse position
function shoot() {
  const angle = Math.atan2(mouseY - (height - 120), mouseX - (width / 2));
  const velocity = {
    x: Math.cos(angle) * 5,
    y: Math.sin(angle) * 5
  };

  const bullet = {
    x: width / 2,
    y: height - 120,
    radius: 5,
    color: 'red',
    velocity: velocity
  };

  bullets.push(bullet);
}

function drawBullets() {
  bullets.forEach((bullet, index) => {
    ctx.beginPath();
    ctx.arc(bullet.x, bullet.y, bullet.radius, 0, Math.PI * 2);
    ctx.fillStyle = bullet.color;
    ctx.fill();

    // Update bullet's position based on its velocity
    bullet.x += bullet.velocity.x;
    bullet.y += bullet.velocity.y;

    // Remove bullet if it goes off screen
    if (bullet.x + bullet.radius < 0 || bullet.x - bullet.radius > canvas.width ||
        bullet.y + bullet.radius < 0 || bullet.y - bullet.radius > canvas.height) {
      bullets.splice(index, 1);
      }
    });
  }

  function loop() {
    drawScene();
    drawCannon();
    drawCrosshair();
    drawBullets();
    requestAnimationFrame(loop)
  }

  window.addEventListener('mousedown', () => {
    shoot()
  });

  loop();

});
