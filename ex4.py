<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Menu Interativo</title>
<style>
  body {
    background: #121212;
    color: #eee;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    height: 100vh;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  #container {
    background: #1e1e1e;
    padding: 2rem;
    border-radius: 10px;
    width: 320px;
    box-shadow: 0 5px 20px rgba(29, 185, 84, 0.75);
    text-align: center;
  }
  h2 {
    margin-bottom: 1.5rem;
    color: #1db954;
  }
  button {
    background: #1db954;
    color: #121212;
    font-weight: 700;
    border: none;
    border-radius: 8px;
    padding: 0.75rem 0;
    font-size: 1.1rem;
    cursor: pointer;
    width: 100%;
    margin: 0.4rem 0;
    transition: background-color 0.25s ease;
  }
  button:hover {
    background: #13943d;
  }
  #output {
    margin-top: 1.25rem;
    min-height: 3rem;
    font-size: 1.2rem;
    color: #1db954;
  }
</style>
</head>
<body>
  <div id="container">
    <h2>Menu</h2>
    <button data-option="1">[1] Olá</button>
    <button data-option="2">[2] Ajuda</button>
    <button data-option="3">[3] Sair</button>
    <div id="output" aria-live="polite"></div>
  </div>

<script>
  (function(){
    const buttons = document.querySelectorAll('button[data-option]');
    const output = document.getElementById('output');
    let running = true;

    function processOption(option) {
      switch(option) {
        case '1':
          output.textContent = 'Olá! Seja muito bem-vindo(a)!';
          break;
        case '2':
          output.textContent = 'Esta é a ajuda: Escolha uma opção do menu.';
          break;
        case '3':
          output.textContent = 'Saindo do programa... Até a próxima!';
          running = false;
          // Disable buttons on exit
          buttons.forEach(btn => btn.disabled = true);
          break;
        default:
          output.textContent = 'Opção inválida. Tente novamente.';
          break;
      }
    }

    buttons.forEach(button => {
      button.addEventListener('click', () => {
        if (!running) return;
        const option = button.getAttribute('data-option');
        processOption(option);
      });
    });
  })();
</script>
</body>
</html>
