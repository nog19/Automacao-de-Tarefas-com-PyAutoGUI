# Automação de Tarefas com PyAutoGUI

Pequeno conjunto de scripts para automatizar tarefas na sua máquina usando PyAutoGUI (interação com mouse/teclado) e Pandas (leitura de CSV). Baseado no README do projeto de automação, este documento descreve rapidamente cada arquivo, dependências e cuidados ao usar os scripts.

## O que tem aqui
- automacao.py — automatiza o cadastro de produtos em uma interface web lendo `produtos.csv`. (usa Pandas)
- assistente.py — utilitário que exibe a posição do mouse para coletar coordenadas (útil para ajustar cliques).
- produtos.csv — base de dados com os produtos a cadastrar.
- "abridor do mine.py" — abre o TLauncher/Minecraft e faz um pequeno fluxo de craft (arrastar itens no inventário para criar uma crafting table).
  - Observação: o nome do arquivo contém espaços; considere renomeá-lo para `abridor_do_mine.py`.
- pequeno_teste — script simples que abre o navegador e navega até o YouTube (exemplo de teste/prática com PyAutoGUI).

## Requisitos
- Python 3.8+
- Bibliotecas:
  - pyautogui
  - pandas (necessário apenas para `automacao.py`)

Instalação rápida:
```bash
pip install pyautogui pandas
```

Em alguns sistemas (macOS, Linux) pode ser necessário permitir permissões de acessibilidade/automação para que PyAutoGUI controle o mouse/teclado.

## Como usar (resumido)
1. Coletar coordenadas:
   - Execute `assistente.py` (python assistente.py) e mova o mouse sobre os elementos para anotar X e Y.
   - Atualize as coordenadas nos scripts (`automacao.py`, `abridor_do_mine.py`, `pequeno_teste`) conforme sua resolução, escala e posição das janelas.
2. Ajustar credenciais:
   - Nunca deixe senhas em texto no repositório.
   - Para `automacao.py`, prefira solicitar a senha em tempo de execução (`input()`), usar variáveis de ambiente ou um cofre de segredos.
3. Testar com cuidado:
   - Teste cada script passo a passo (ex.: comentar loops, rodar apenas uma iteração).
   - Deixe a janela correta em foco e não mova o mouse durante a execução.
4. Executar:
```bash
python automacao.py       # cadastra produtos (após ajustar coordenadas e credenciais)
python "abridor do mine.py"   # abre TLauncher/Minecraft e executa craft (ajuste tempos e coords)
python pequeno_teste.py   # abre navegador e vai ao YouTube (exemplo rápido)
```

## Boas práticas e riscos
- PyAutoGUI controla o mouse e teclado — movimentos inesperados podem causar ação indesejada. Use com cuidado.
- Habilite a proteção de emergência:
  - pyautogui.FAILSAFE = True  # mover o mouse para o canto superior esquerdo interrompe a execução
- Ajuste `pyautogui.PAUSE` e tempos (`time.sleep`) para garantir que a interface esteja pronta antes de cada ação.
- Coordenadas são dependentes de resolução, escala (DPI) e layout — valide sempre antes de usar em produção.
- Para tarefas web robustas, prefira automação baseada em navegador (Selenium, Playwright) em vez de automação por tela.
- Cuidado com launchers de terceiros (ex.: TLauncher) — verifique confiabilidade e tempos de carregamento.

## Observações específicas
- automacao.py:
  - Lê `produtos.csv` com Pandas e realiza o loop de cadastro usando cliques e tabs.
  - Ajuste as coordenadas e aumente os sleeps se a página demorar para carregar.
- "abridor do mine.py":
  - Executa sequência para abrir o launcher, iniciar o jogo e arrastar itens no inventário para realizar um craft.
  - Tem tempos longos (esperas) que dependem do desempenho da sua máquina; ajuste conforme necessário.
- pequeno_teste:
  - Script simples para abrir o navegador e ir ao YouTube — bom para validar se PyAutoGUI está funcionando.

## Licença
Sinta-se livre para usar e adaptar este material para fins de estudo. Use em ambiente de teste antes de rodar em larga escala — nenhuma garantia é oferecida.
