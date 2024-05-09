import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

# Abre o Internet Explorer
pyautogui.hotkey('win', 'r')  # Abre o Executar
pyautogui.typewrite("iexplore http://ibbca.topdown.com.br")
pyautogui.press('enter')
time.sleep(10)  # Espere um

# Clique para fechar a caixa x: X=959, Y=517
pyautogui.click(x=959, y=517)
time.sleep(10)  # Espere um segundo

# Função para obter o nome de usuário e a senha usando uma caixa de diálogo
def get_credentials():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Solicita o nome de usuário
    username = simpledialog.askstring("Input", "Digite seu nome de usuário:")
    if username is None:
        exit()  # Se o usuário pressionar Cancelar, encerre o programa

    # Solicita a senha (o texto será oculto)
    password = simpledialog.askstring("Input", "Digite sua senha:", show='*')
    if password is None:
        exit()  # Se o usuário pressionar Cancelar, encerre o programa

    return username, password

# Obtenha o nome de usuário e a senha usando a caixa de diálogo
username, password = get_credentials()

# Clique no campo de usuário nas coordenadas X=281, Y=373
pyautogui.click(x=281, y=373)
pyautogui.write(username)
time.sleep(3)  # Espere um segundo

# Clique no campo de senha nas coordenadas X=292, Y=400
pyautogui.click(x=292, y=400)
pyautogui.write(password)
time.sleep(1)  # Espere um segundo

# Clique Entrar x: X=338, Y=427
pyautogui.click(x=338, y=427)
time.sleep(5)  # Espere um segundo

# Clique no botão de comissões  X=31, Y=207
pyautogui.click(x=31, y=207)
time.sleep(4)  # Espere um segundo

# Clique no botão de Consultas e relatórios  X=45, Y=267
pyautogui.click(x=45, y=267)
time.sleep(4)  # Espere um segundo

# Clique no botão Extrato do produtor X=63, Y=316
pyautogui.click(x=63, y=316)
time.sleep(4)  # Espere um segundo

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

root = tk.Tk()
root.withdraw()
data_inserida = simpledialog.askstring("Data de Corte", "Insira a data no formato DD/MM/AAAA:")

data_corte = None  # Declare a variável fora do bloco try

try:
    data_corte = datetime.strptime(data_inserida, "%d/%m/%Y").strftime("%d/%m/%Y")
    # Insira a data na caixa de seleção
    pyautogui.write(str(data_corte))  # Certifique-se de que a data seja tratada como string
except ValueError:
    print("Data inserida em formato incorreto.")

root.destroy()
time.sleep(5)  # Aguarde 5 segundos

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

# Clique no quadrado Aumentar a Janela X=621, Y=54
pyautogui.click(x=1521, y=15)
time.sleep(4)  # Espere um segundo

# Clique no Produtor 19121620000107-A CASA DO CORRETOR X=1131, Y=425
pyautogui.click(x=1131, y=425)
time.sleep(5)  # Espere um segundo


# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Salvar o arquiv :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(4)  # Espere um segundo

############################################################################################################


# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

# Clique no Produtor 03194869000102-ABC - 3852 - FECHADO - X=1121, Y=443
pyautogui.click(x=1121, y=443)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################################################################################

# Clique no Produtor 33293226000187-AEB  - X=1129, Y=479 
pyautogui.click(x=1129, y=479)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################################################################################

# Clique no Produtor 05207622000109-ACCOUNT CONSULTORIA - X=1121, Y=460
pyautogui.click(x=1121, y=460)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo


###########################################################################################################

# Clique no Produtor 19055127000136-AFENAFUP  - X=1124, Y=495  
pyautogui.click(x=1124, y=495)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 13530870000114-AFENPROLIB  - X=1127, Y=514  
pyautogui.click(x=1127, y=514)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 47525340000108-AGERIP-ASSOCIAÇÃO GERONTO-GERIATRICA DE SAO JOSE DO RIO PRETO  -  X=1122, Y=531 
pyautogui.click(x=1122, y=531)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 24132030000110-AGP CONSULTORIA  - X=1116, Y=545 
pyautogui.click(x=1116, y=545)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 52912581362-AGP CONSULTORIA  -	X=1121, Y=563 
pyautogui.click(x=1121, y=563)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 40916627810-ALERRANDRO GOMIERO  - X=1122, Y=581
pyautogui.click(x=1122, y=581)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 26743677000103-ALLCROSS RIO DE JANEIRO  - X=1126, Y=600
pyautogui.click(x=1126, y=600)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 02209275709-ANDRE LUIZ DA SILVA FARIAS  - X=1118, Y=617
pyautogui.click(x=1118, y=617)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 09807591880-ANDRÉ ROBERTO GARCIA  - X=1122, Y=637 
pyautogui.click(x=1122, y=637)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################################

# Clique no Produtor 09608057000142-ANEC  -  X=1124, Y=651
pyautogui.click(x=1124, y=651)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)

# Clique no Produtor 40669347000146-APLAMED SAUDE  -  X=1132, Y=633
pyautogui.click(x=1132, y=651)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)

# Clique no Produtor 06031886000117_5-ATIVUS LIFE CORRETORA  -  X=1125, Y=649
pyautogui.click(x=1125, y=649)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)

# Clique no Produtor 06031886000117_2-ATIVUS LIFE CORRETORA - ASSIM SAUDE E UNIMED RIO - X=1119, Y=663
pyautogui.click(x=1119, y=663)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)

# Clique no Produtor 31437507000130-BLUE LIGHT CORRETORA -  X=1121, Y=645
pyautogui.click(x=1121, y=645)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""


# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)



# Clique no Produtor 41139882000158-CAAPB -  X=1126, Y=662
pyautogui.click(x=1126, y=662)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo


# Clique no Produtor 87093092000180-CAARS - X=1125, Y=639
pyautogui.click(x=1125, y=639)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#############################################"""""""""###################################"""""""""""""""

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo


# Clique no Produtor 22831072000113-CAMPO BELO CORRETORA - Y=1121, Y=660
pyautogui.click(x=1121, y=660)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 11770560000141_5-CASULO PLATAFORMA - X=1124, Y=411
pyautogui.click(x=1124, y=411)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 08613161000162_5-CONGELADOS DS MARTINS - X=1123, Y=429
pyautogui.click(x=1123, y=429)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo


#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 21776597000130-CORRETORA DE SEGUROS RJMID - X=1131, Y=447
pyautogui.click(x=1131, y=447)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 09298037000112_1-CORRETORA NAO CADASTRADA - X=1130, Y=461
pyautogui.click(x=1130, y=461)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundos

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 04653113000147-DELFHI CORRETORA - X=1131, Y=482
pyautogui.click(x=1131, y=482)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundos

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 21706308000127-DHEUZA SEGUROS  - X=1131, Y=498
pyautogui.click(x=1131, y=498)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 31708627000125-DM SAÚDE CORRETORES LTDA  -  X=1132, Y=515
pyautogui.click(x=1132, y=515)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 08613161000162_0-DS MARTINS PLATAFORMA - X=1132, Y=533
pyautogui.click(x=1132, y=533)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 08613161000162_7-DS MARTINS PLATAFORMA - RETENÇÃO - X=1131, Y=550
pyautogui.click(x=1131, y=550)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 02907471000103-FADESP - X=1130, Y=567 
pyautogui.click(x=1130, y=567)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

#####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 21939379000170-GERAÇÃO SAÚDE CORRETORA - X=1126, Y=587 
pyautogui.click(x=1126, y=587)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 19231283000100-GOMES CORRETORA - X=1130, Y=601
pyautogui.click(x=1130, y=601)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 35266698000176-GOMIERO & SOUZA CORRETORA - CARLOS ALBERTO - X=1131, Y=619
pyautogui.click(x=1131, y=619)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 26710808000156-HUDSON RODRIGUES - MDR CONSULTORIA - X=1129, Y=636
pyautogui.click(x=1129, y=636)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz


####################################################################################################################################
#####################################################################################################################################
######################################################################################################################################       

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(3)  # Espere um segundo



# Clique no Produtor 21659312000181_5-IDI INTERMEDIAÇÃO PLATAFORMA - X=1130, Y=653
pyautogui.click(x=1130, y=653)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundoz

##################################################################
##################################################################
##################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 21659312000181_7-IDI INTERMEDIAÇÃO PLATAFORMA - RETENÇÃO  X=1117, Y=406
pyautogui.click(x=1117, y=406)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################
##############################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 10685429000113-INOVAR PLATAFORMA - X=1122, Y=422
pyautogui.click(x=1122, y=422)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################
##############################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 17354919000186-J GARCIA CORRETORA - X=1129, Y=439
pyautogui.click(x=1129, y=439)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################
##############################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 08056902000151-JAB CONSULTORIA CORRETORA - X=1124, Y=460
pyautogui.click(x=1124, y=460)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###########################################################################################
##############################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 17082050000168_1-JANAINA F & CUNHA CORRETAGENS DE SEGUROS  X=1128, Y=477
pyautogui.click(x=1128, y=477)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 4234408484300-JANE KELLY SILVA SA - SEM TAXA - X=1121, Y=493
pyautogui.click(x=1121, y=493)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 14324635000159-JC LUZ CORRETORA - X=1125, Y=506
pyautogui.click(x=1125, y=506)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo
##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 37119905000195_0-JL SAÚDE - X=1122, Y=528
pyautogui.click(x=1122, y=528)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 04232785000189-JP&B INTERMEDIAÇÃO - X=1127, Y=547
pyautogui.click(x=1127, y=547)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 09443643000184-JV BRASILIA SERVICOS - X=1122, Y=560
pyautogui.click(x=1122, y=560)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 9443643000184_3-JV BRASILIA SERVICOS - ELITE RIO - X=1122, Y=579
pyautogui.click(x=1122, y=579)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 48226552885-KARINE GANDINE DE ARAUJO - X=1125, Y=597
pyautogui.click(x=1125, y=597)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 46887532000193-KM - SAUDE SEGURO E ODONTO - X=1128, Y=614
pyautogui.click(x=1128, y=614)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 32256529000167-LIFE SAUDE PLATAFORMA - X=1128, Y=634
pyautogui.click(x=1128, y=634)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################
###########################################################################################################
############################################################################################
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 24455143000156-LIGA BENEFICIOS CORRETORA - X=1130, Y=648
pyautogui.click(x=1130, y=648)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##################################################################
##################################################################
##################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 20922275000190-LIGAMAR CORRETORA - X=1131, Y=400 
pyautogui.click(x=1131, y=400)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##################################################################
##################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 22787890000166-LIGUE SAUDE CORRETORA - X=1131, Y=419
pyautogui.click(x=1131, y=419)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 10405516000170-LM&A RISK SERVICES CORRETORA - X=1130, Y=435
pyautogui.click(x=1130, y=435)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 11965952000166-LMC CORRETORA - X=1131, Y=453
pyautogui.click(x=1131, y=453)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 11403002703-LUIZ PAULO DE OLIVEIRA - X=1131, Y=471
pyautogui.click(x=1131, y=471)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 27796431000162-MADREPEROLA CORRETORA - X=1132, Y=485
pyautogui.click(x=1132, y=485)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 98417177604_0-MARCOS ANTONIO MARCAL DA SILVA - X=1130, Y=505
pyautogui.click(x=1130, y=505)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 04141965707-MARIA DE FATIMA DUARTE - X=1131, Y=521
pyautogui.click(x=1131, y=521)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

###############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 15050678000156-MASTER INTERMEDIAÇÃO E CONSULTORIA - X=1131, Y=538
pyautogui.click(x=1131, y=538)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 28667912000130-MEDCLASS CORRETORA - X=1130, Y=556
pyautogui.click(x=1130, y=556)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 09560523000167-MF SAUDE - MARCELO RANGEL VIANNA PLANOS DE SAUDE - X=1131, Y=573
pyautogui.click(x=1131, y=573)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 24653431000115-MM SAUDE CORRETORES - X=1129, Y=592
pyautogui.click(x=1129, y=592)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 03028103000158-MQ CORRETORA DE SEGUROS - UNIMED RIO - X=1130, Y=609
pyautogui.click(x=1130, y=609)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 21753010000178-MS BUSINESS CORRETORA - X=1131, Y=626
pyautogui.click(x=1131, y=626)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################
###############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 23625946000149-MULTIPLA CORRETORA - X=1131, Y=641
pyautogui.click(x=1131, y=641)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##############################################################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo

# Clique no Produtor 13843895000178-NOVA AFFINITY CORRETORA - X=1130, Y=660
pyautogui.click(x=1130, y=660)
time.sleep(3)  # Espere um segundo

# Clique Para Transpor pagina X=105, Y=636
pyautogui.click(x=105, y=636)
time.sleep(4)  # Espere um segundo

# Clique Para Salvar o arquivo X=1105, Y=837
pyautogui.click(x=1105, y=837)
time.sleep(4)  # Espere um segundo 

# Clique Para Fechar janela :X=1265, Y=839
pyautogui.click(x=1265, y=839)
time.sleep(4)  # Espere um segundo

# Clique ir extrato do produtor X=63, Y=307
pyautogui.click(x=63, y=307)
time.sleep(4)  # Espere um segundo : X=1105, Y=837

# Clique no quadro "Data corte" X=643, Y=287
pyautogui.click(x=643, y=287)
time.sleep(4)  # Espere um segundo

pyautogui.write(data_corte)
time.sleep(1)  # Espere um segundo

# Clique no quadrado "Executar" X=387, Y=154
pyautogui.click(x=387, y=154)
time.sleep(4)  # Espere um segundo

##################################################################

# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
# Seta para baixo X=1597, Y=647
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo
pyautogui.click(x=1597, y=647)
time.sleep(1)  # Espere um segundo