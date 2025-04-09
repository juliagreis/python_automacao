#utilizando a biblioteca pyautogui para realizar automacao de projetos
import pyautogui
import time
import pandas






pyautogui.PAUSE=0.5  #definindo um delay padrao depois de CADA comando





                    #primeiro passo -> abrir o navegador

print("Abrindo navegador Chrome\n")

pyautogui.moveTo(10, 10)
pyautogui.hotkey("command","space")  #abrindo menu de busca
pyautogui.write('safari')  #buscando chrome no menu
pyautogui.press('enter')   #abrindo chrome

print("Navegador chrome aberto!\n")





                #segundo passo-> entrar no site que deseja utilizar


#nesse caso, um site padrao login de usuario
#feito para fins de estudo (https://dlp.hashtagtreinamentos.com/python/intensivao/login)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#como estamos carregando um site, pode haver uma demora maior para que a pagina carregue
#entao o ideal é termos uma pausa maior para garantir que o site de fato
#esteja carregado quando seguirmos adiante com outros comandos
time.sleep(5)  #definindo uma espera de 3 segundos para que o site carregue




                #terceiro passo ->realizando o login
pyautogui.click(x=481, y=379)  #valores verificados pelo arquivo posicao_cursor.py
pyautogui.write("julia.reis@gmail.com")
pyautogui.press("tab")
pyautogui.write("MinhaSenha")
pyautogui.press("Enter")
time.sleep(3)  #definindo uma espera de 3 segundos para que o site carregue




                #quarto passo-> importar a base de dados

tabelaBaseDeDados = pandas.read_csv("produtos.csv")  #recebe os valores da base de dados

                #quinto passo-> cadastrar 1 produto

for idLinha in tabelaBaseDeDados.index:
    pyautogui.click(x=597, y=263)   #valores verificados pelo arquivo posicao_cursor.py

    pyautogui.write(tabelaBaseDeDados.loc[idLinha,"codigo"])
    pyautogui.press("tab")
    pyautogui.write(tabelaBaseDeDados.loc[idLinha,"marca"])
    pyautogui.press("tab")
    pyautogui.write(tabelaBaseDeDados.loc[idLinha,"tipo"])
    pyautogui.press("tab")
    pyautogui.write(str(tabelaBaseDeDados.loc[idLinha,"Categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabelaBaseDeDados.loc[idLinha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabelaBaseDeDados.loc[idLinha,"custo"]))
    pyautogui.press("tab")

    if str(tabelaBaseDeDados.loc[idLinha,"obs"])!='nan':
        pyautogui.write(str(tabelaBaseDeDados.loc[idLinha,"obs"]))
    
    pyautogui.press("enter")
    pyautogui.scroll(2000)    #retornando ao topo do site
    time.sleep(1)
    






 