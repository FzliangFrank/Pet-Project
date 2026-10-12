function rgbToHsl(r, g, b) {
  r /= 255;
  g /= 255;
  b /= 255;

  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  let h, s, l = (max + min) / 2;

  if (max === min) {
    h = s = 0;
  } else {
    const d = max - min;
    s = l > 0.5 ? d / (2 - max - min) : d / (max + min);

    switch (max) {
      case r: h = (g - b) / d + (g < b ? 6 : 0); break;
      case g: h = (b - r) / d + 2; break;
      case b: h = (r - g) / d + 4; break;
    }

    h /= 6;
  }

  return [h * 360, s * 100, l * 100];
}

function createFlippedBackground(image) {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  
  // Set canvas size to match image
  canvas.width = image.width;
  canvas.height = image.height;
  
  // Save the current context
  ctx.save();
  
  // Translate to the center of the canvas
  ctx.translate(canvas.width/2, canvas.height/2);
  
  // Rotate 180 degrees (upside down)
  ctx.rotate(Math.PI);
  
  // Scale horizontally by -1 (mirror)
  ctx.scale(-1, 1);
  
  // Draw the image
  ctx.drawImage(image, -canvas.width/2, -canvas.height/2);
  
  // Restore the context
  ctx.restore();
  
  return canvas.toDataURL('image/jpeg');
}

function calculateLuminance(r, g, b) {
  // Convert RGB to relative luminance
  const [rs, gs, bs] = [r, g, b].map(c => {
    c = c / 255;
    return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
  });
  return 0.2126 * rs + 0.7152 * gs + 0.0722 * bs;
}

function getColorFromImage(image) {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  canvas.width = image.width;
  canvas.height = image.height;
  context.drawImage(image, 0, 0);
  
  const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
  const data = imageData.data;
  
  // Create color frequency map
  const colorMap = new Map();
  let mostFrequentColor = null;
  let maxCount = 0;
  
  // Find most vibrant color
  let mostVibrantColor = null;
  let maxSaturation = 0;
  
  // Sample colors from the image
  const sampleSize = 1000;
  const step = Math.floor(data.length / 4 / sampleSize);
  
  for (let i = 0; i < data.length; i += 4 * step) {
    const r = data[i];
    const g = data[i + 1];
    const b = data[i + 2];
    
    // Skip very dark or very light colors
    if (r + g + b < 30 || r + g + b > 750) continue;
    
    // Create color key
    const colorKey = `${r},${g},${b}`;
    
    // Update frequency map
    const count = (colorMap.get(colorKey) || 0) + 1;
    colorMap.set(colorKey, count);
    
    // Update most frequent color
    if (count > maxCount) {
      maxCount = count;
      mostFrequentColor = {r, g, b};
    }
    
    // Check for vibrant color
    const [h, s, l] = rgbToHsl(r, g, b);
    if (s > maxSaturation && l > 20 && l < 80) {
      maxSaturation = s;
      mostVibrantColor = {r, g, b};
    }
  }
  
  return {
    dominant: mostFrequentColor ? `rgba(${mostFrequentColor.r}, ${mostFrequentColor.g}, ${mostFrequentColor.b}, 0.7)` : 'rgba(0, 0, 0, 0.7)',
    vibrant: mostVibrantColor ? `rgba(${mostVibrantColor.r}, ${mostVibrantColor.g}, ${mostVibrantColor.b}, 0.7)` : 'rgba(255, 255, 255, 0.7)',
    isLight: mostFrequentColor ? calculateLuminance(mostFrequentColor.r, mostFrequentColor.g, mostFrequentColor.b) > 0.5 : false
  };
}

function updateCaptionBackground(img, caption) {
  const colors = getColorFromImage(img);
  const flippedBackground = createFlippedBackground(img);
  
  caption.style.background = `linear-gradient(${colors.dominant}, ${colors.vibrant}), url(${flippedBackground})`;
  caption.style.backgroundSize = 'cover';
  caption.style.backgroundPosition = 'center';
  
  // Set text color based on background brightness
  if (colors.isLight) {
    caption.style.color = '#000';
  } else {
    caption.style.color = '#fff';
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  const carouselItems = document.querySelectorAll('.carousel-item');
  
  carouselItems.forEach(item => {
    const img = item.querySelector('img');
    const caption = item.querySelector('.carousel-caption-custom');
    
    img.addEventListener('load', function() {
      updateCaptionBackground(this, caption);
    });
    
    if (img.complete) {
      updateCaptionBackground(img, caption);
    }
  });
}); 