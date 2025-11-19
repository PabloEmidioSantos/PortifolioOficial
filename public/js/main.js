// animação de fade-in ao rolar a página
const faders = document.querySelectorAll('.fade-in');

// === Sistema de Tema Claro/Escuro ===
const toggleBtn = document.getElementById("theme-toggle");
const root = document.documentElement;

// se já tiver um tema salvo
if (localStorage.getItem("theme") === "dark") {
  document.documentElement.classList.add("dark-mode");
  toggleBtn.textContent = "☀️";
}

toggleBtn.addEventListener("click", () => {
  document.documentElement.classList.toggle("dark-mode");

  if (document.documentElement.classList.contains("dark-mode")) {
    toggleBtn.textContent = "☀️";
    localStorage.setItem("theme", "dark");
  } else {
    toggleBtn.textContent = "🌙";
    localStorage.setItem("theme", "light");
  }
});


const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.2 });

faders.forEach(fade => observer.observe(fade));
