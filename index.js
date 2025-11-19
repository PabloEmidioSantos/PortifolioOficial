const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

// servir arquivos estáticos
app.use(express.static(path.join(__dirname, 'public')));

// rota principal
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Servidor rodando: http://localhost:${PORT}`);
});
