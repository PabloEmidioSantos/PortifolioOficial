const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 8998;

// Middlewares
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// Rotas
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'index.html'));
});

app.get('/contato', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'contato.html'));
});

// Rota POST para receber formulário
app.post('/contato', (req, res) => {
  const { nome, email, mensagem } = req.body;
  console.log('Formulário recebido:', nome, email, mensagem);
  res.send(`<h1>Obrigado, ${nome}! Sua mensagem foi enviada.</h1><a href="/">Voltar para Home</a>`);
});

// Rota para projetos (opcional)
app.get('/projetos', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'projetos.html'));
});

// Servidor
app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
