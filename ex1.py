  <h2>Contagem Regressiva</h2>
  <p>Digite um número inteiro positivo:</p>
  <input type="number" id="numberInput" min="1" step="1" placeholder="Ex: 10" />
  <br />
  <button id="startBtn">Iniciar Contagem</button>
  <div id="output"></div>
</div>
<script>
  const numberInput = document.getElementById('numberInput');
  const startBtn = document.getElementById('startBtn');
  const output = document.getElementById('output');
  startBtn.addEventListener('click', () => {
    let x = parseInt(numberInput.value, 10);
    if (isNaN(x) || x < 1) {
      alert('Por favor, digite um número inteiro positivo válido.');
      return;
    }
    output.textContent = '';
    // Contagem regressiva usando while
    while (x >= 0) {
      output.textContent += x + '\n';
      x--;
    }
  });
</script>
</body>
</html>