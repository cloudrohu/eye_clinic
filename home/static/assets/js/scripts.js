document.addEventListener("DOMContentLoaded", function () {
const menuBtn = document.getElementById("menuBtn");
const sidebar = document.getElementById("sidebar");
const drawer = document.getElementById("drawer");
const closeBtn = document.getElementById("closeBtn");
const overlay = document.getElementById("overlay");

// Open Sidebar
menuBtn.addEventListener("click", () => {
sidebar.classList.remove("hidden");
setTimeout(() => {
    drawer.classList.remove("-translate-x-full");
}, 50);
});

// Close Sidebar function
function closeSidebar() {
drawer.classList.add("-translate-x-full");
setTimeout(() => {
    sidebar.classList.add("hidden");
}, 300); // match transition duration
}

// Close with closeBtn
closeBtn.addEventListener("click", closeSidebar);

// Close with overlay
overlay.addEventListener("click", closeSidebar);
});



// slider
  document.addEventListener("DOMContentLoaded", () => {
    const slider = document.getElementById("slider");
    const slides = slider.children;
    const totalSlides = slides.length;
    let index = 0;
    let interval;

    const dotsContainer = document.getElementById("dots");
    for (let i = 0; i < totalSlides; i++) {
      const dot = document.createElement("div");
      dot.classList = "w-4 h-4 rounded-full bg-gray-300 cursor-pointer transition";
      dot.addEventListener("click", () => goToSlide(i));
      dotsContainer.appendChild(dot);
    }

    function updateDots() {
      [...dotsContainer.children].forEach((dot, i) => {
        dot.classList = i === index 
          ? "w-4 h-4 rounded-full bg-indigo-600 scale-110 transition" 
          : "w-4 h-4 rounded-full bg-gray-300 cursor-pointer transition";
      });
    }

    function goToSlide(i) {
      index = (i + totalSlides) % totalSlides;
      slider.style.transform = `translateX(-${index * 100}%)`;
      updateDots();
    }

    function nextSlide() { goToSlide(index + 1); }
    function prevSlide() { goToSlide(index - 1); }

    document.getElementById("nextBtn").addEventListener("click", nextSlide);
    document.getElementById("prevBtn").addEventListener("click", prevSlide);

    function startAutoSlide() {
      interval = setInterval(nextSlide, 5000); // 5 sec auto-slide
    }
    function stopAutoSlide() {
      clearInterval(interval);
    }

    slider.addEventListener("mouseenter", stopAutoSlide);
    slider.addEventListener("mouseleave", startAutoSlide);

    // Init
    goToSlide(0);
    startAutoSlide();
  });
  document.addEventListener("DOMContentLoaded", () => {
  // Reveal on scroll animation
  const aboutSection = document.getElementById("about");
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        aboutSection.classList.add("animate-fadeInUp");
      }
    });
  }, { threshold: 0.2 });

  observer.observe(aboutSection);
});
 
 
 // Gallery click event
  document.querySelectorAll('#gallery .group').forEach(card => {
    card.addEventListener('click', () => {
      const imgSrc = card.querySelector('img').src;
      document.getElementById('popupImg').src = imgSrc;
      document.getElementById('popup').classList.remove('hidden');
    });
  });

  // Close popup
  document.getElementById('closePopup').addEventListener('click', () => {
    document.getElementById('popup').classList.add('hidden');
  });

  // Close popup on outside click
  document.getElementById('popup').addEventListener('click', (e) => {
    if (e.target.id === 'popup') {
      document.getElementById('popup').classList.add('hidden');
    }
  });
  // Floating Action Box (FAB) Animation

  const fabBox = document.getElementById("fabBox");
  const cube = document.getElementById("cube");
  const boxContent = document.getElementById("boxContent");
  const closeBox = document.getElementById("closeBox");
  const openBox = document.getElementById("openBox");
  const fabItems = document.querySelectorAll(".fab-item");

  const animations = [
    "animate-bounce",
    "animate-shake",
    "animate-pulse",
    "animate-rotate",
    "animate-wiggle",
    "animate-zoom",
    "animate-glow",
    "animate-swing",
    "animate-flip",
    "animate-tada"
  ];

  function randomAnimation(btn) {
    animations.forEach(anim => btn.classList.remove(anim));
    const newAnim = animations[Math.floor(Math.random() * animations.length)];
    btn.classList.add(newAnim);
  }

  // Page load → Cube unfolds into Box
  window.addEventListener("load", () => {
    fabBox.classList.remove("translate-x-full","opacity-0","scale-0");
    fabBox.classList.add("animate-cubeUnfold");
    setTimeout(() => {
      cube.style.display = "none";
      boxContent.classList.remove("hidden");

      // Start infinite random animations
      setInterval(() => {
        fabItems.forEach(btn => randomAnimation(btn));
      }, 3000);

    }, 1000);
  });

  // Close → shrink back to cube
  closeBox.addEventListener("click", () => {
    boxContent.classList.add("hidden");
    cube.style.display = "flex";
    cube.classList.remove("animate-cubeUnfold");
    cube.classList.add("animate-cubeFold");
    setTimeout(() => {
      fabBox.style.display = "none";
      openBox.classList.remove("hidden");
    }, 800);
  });

  // Reopen → Cube reappears then unfold
  openBox.addEventListener("click", () => {
    fabBox.style.display = "block";
    cube.style.display = "flex";
    boxContent.classList.add("hidden");

    cube.classList.remove("animate-cubeFold");
    cube.classList.add("animate-cubeUnfold");

    setTimeout(() => {
      cube.style.display = "none";
      boxContent.classList.remove("hidden");
      openBox.classList.add("hidden");
    }, 1000);
  });

  // Run on page load
  updateCallStatus();
  // Update every 1 min
  setInterval(updateCallStatus, 60000);

const counters = document.querySelectorAll('.counter');
  const speed = 100; // lower = faster

  counters.forEach(counter => {
    const updateCount = () => {
      const target = +counter.getAttribute('data-target');
      const count = +counter.innerText;
      const increment = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + increment);
        setTimeout(updateCount, 20);
      } else {
        counter.innerText = target.toLocaleString(); // formatted number
      }
    };

    // Start animation when in viewport
    const observer = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting) {
        updateCount();
        observer.disconnect();
      }
    });
    observer.observe(counter);
  });

   function openPopup() {
    let modal = document.getElementById("popupModal");
    let box = document.getElementById("popupBox");
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    setTimeout(() => {
      box.classList.remove("scale-95");
      box.classList.add("scale-100");
    }, 50);
  }
  function closePopup() {
    let modal = document.getElementById("popupModal");
    let box = document.getElementById("popupBox");
    box.classList.remove("scale-100");
    box.classList.add("scale-95");
    setTimeout(() => {
      modal.classList.add("hidden");
      modal.classList.remove("flex");
    }, 200);
  }