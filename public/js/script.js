const projetos = [
  { nome: 'Portfólio Pessoal', descricao: 'Meu portfólio desenvolvido em HTML, CSS e JS', link: '#' },
  { nome: 'Site da Pizzaria', descricao: 'Projeto de estudo, site de pizzaria responsivo', link: '#' },
  { nome: 'BlckFit', descricao: 'Loja de roupas com Node.js e pagamentos', link: '#' },
];

const grid = document.getElementById('projetos-grid');

projetos.forEach(projeto => {
  const div = document.createElement('div');
  div.classList.add('projeto');
  div.innerHTML = `
    <h3>${projeto.nome}</h3>
    <p>${projeto.descricao}</p>
    <a href="${projeto.link}" target="_blank">Ver Projeto</a>
  `;
  grid.appendChild(div);
});

// Formulário simples
document.getElementById('form-contato').addEventListener('submit', e => {
  e.preventDefault();
  alert('Mensagem enviada!');
});
