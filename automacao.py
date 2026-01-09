# sistema com os dados fornecidos pelo curso
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> serve para escrever texto
# pyautogui.press -> pressiona uma tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> varias teclas (tipo ctrl + c)
pyautogui.PAUSE = 0.3

#nessa parte do código é aberto o navegador, no caso o edge
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Fazendo login, selecionando campos como email e senha
# selecionar o campo de email
pyautogui.click(x=648, y=362)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=694, y=521) # clique no botao de login
time.sleep(3)

# Importando a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Cadastramento de um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=836, y=243)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # subir a pagina pra cadastrar o próximo produto
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim