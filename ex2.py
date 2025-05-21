<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Contagem de Vogais</title>
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #121212;
    color: #eee;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }
  #container {
    background: #1e1e1e;
    padding: 2rem;
    border-radius: 10px;
    width: 320px;
    box-shadow: 0 6px 20px rgba(29, 185, 84, 0.7);
    text-align: center;
  }
  input[type="text"] {
    width: 100%;
    padding: 0.6rem 1rem;
    font-size: 1rem;
    border-radius: 6px;
    border: none;
    outline: none;
    margin-bottom: 1rem;
    background-color: #121212;
    color: #eee;
  }
  input[type="text"]::placeholder {
    color: #666;
  }
  button {
    background-color: #1db954;
    border: none;
    color: #121212;
    font-weight: 700;
    padding: 0.75rem 1.2rem;
    font-size: 1rem;
    border-radius: 6px;
    cursor: pointer;
    transition: background-color 0.25s ease;
    width: 100%;
  }
  button:hover {
    background-color: #13943d;
  }
  #result {
    margin-top: 1.5rem;
    font-size: 1.25rem;
    font-weight: 600;
    color: #1db954;
  }
</style>
</head>
<body>
<div id="container">
  <h2>Contagem de Vogais</h2>
  <input type="text" id="wordInput" placeholder="Digite uma palavra" autofocus />
  <button id="countBtn">Contar Vogais</button>
  <div id="result" aria-live="polite"></div>
</div>

<script>
  const wordInput = document.getElementById('wordInput');
  const countBtn = document.getElementById('countBtn');
  const result = document.getElementById('result');

  countBtn.addEventListener('click', () => {
    const word = wordInput.value.trim();
    if (word.length === 0) {
      alert('Por favor, digite uma palavra.');
      return;
    }
    const vowels = ['a', 'e', 'i', 'o', 'u'];
    let count = 0;
    for (let i = 0; i < word.length; i++) {
      const char = word[i].toLowerCase();
      if (vowels.includes(char)) {
        count++;
      }
    }
    result.textContent = `Total de vogais na palavra: ${count}`;
  });

  wordInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      countBtn.click();
    }
  });
</script>
</body>
</html>

