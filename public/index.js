// Efeito simples de animação de scroll
const sections = document.querySelectorAll('section');
const options = { threshold: 0.3 };

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if(entry.isIntersecting){
      entry.target.classList.add('show');
    }
  });
}, options);

sections.forEach(section => {
  section.classList.add('hidden');
  observer.observe(section);
});
