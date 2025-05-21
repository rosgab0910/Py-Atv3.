<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Processar Números</title>
<style>
  body {
    background-color: #121212;
    color: #eee;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    height: 100vh;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  #container {
    background-color: #1f1f1f;
    padding: 2rem;
    border-radius: 12px;
    width: 320px;
    box-shadow: 0 6px 25px rgba(29, 185, 84, 0.7);
    text-align: center;
  }
  input[type="number"] {
    width: 80%;
    padding: 0.55rem 1rem;
    font-size: 1rem;
    border-radius: 6px;
    border: none;
    margin: 0.5rem 0;
    background-color: #121212;
    color: #eee;
    outline: none;
  }
  input[type="number"]::placeholder {
    color: #666;
  }
  button {
    margin-top: 1rem;
    padding: 0.75rem 1.4rem;
    font-size: 1.1rem;
    font-weight: 700;
    color: #121212;
    background-color: #1db954;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    width: 100%;
  }
  button:hover {
    background-color: #13943d;
  }
  #result {
    margin-top: 1.5rem;
    text-align: left;
    font-size: 1rem;
    color: #1db954;
    white-space: pre-wrap;
  }
</style>
</head>
<body>
  <div id="container">
    <h2>Digite 3 Números Inteiros</h2>
    <input type="number" id="num1" placeholder="Número 1" step="1" />
    <input type="number" id="num2" placeholder="Número 2" step="1" />
    <input type="number" id="num3" placeholder="Número 3" step="1" />
    <button id="processBtn">Processar</button>
    <div id="result" aria-live="polite" role="region"></div>
  </div>

<script>
  const inputs = [
    document.getElementById('num1'),
    document.getElementById('num2'),
    document.getElementById('num3')
  ];
  const processBtn = document.getElementById('processBtn');
  const result = document.getElementById('result');

  processBtn.addEventListener('click', () => {
    let numeros = [];
    for (let i = 0; i < inputs.length; i++) {
      const val = inputs[i].value.trim();
      if (val === '') {
        alert(`Por favor, preencha o Número ${i+1}.`);
        inputs[i].focus();
        return;
      }
      if (!Number.isInteger(Number(val))) {
        alert(`Número ${i+1} não é um inteiro válido.`);
        inputs[i].focus();
        return;
      }
      numeros.push(parseInt(val, 10));
    }

    const numerosMultiplicados = numeros.map(n => n * 2);
    const somaOriginal = numeros.reduce((acc, cur) => acc + cur, 0);
    const somaMultiplicados = numerosMultiplicados.reduce((acc, cur) => acc + cur, 0);

    result.textContent = 
      `Números originais: [${numeros.join(', ')}]\n` +
      `Números multiplicados por 2: [${numerosMultiplicados.join(', ')}]\n\n` +
      `Soma dos números originais: ${somaOriginal}\n` +
      `Soma dos números multiplicados por 2: ${somaMultiplicados}`;
  });

  // Also allow pressing Enter on last input to trigger processing
  inputs[2].addEventListener('keypress', e => {
    if (e.key === 'Enter') {
      processBtn.click();
    }
  });
</script>
</body>
</html>
