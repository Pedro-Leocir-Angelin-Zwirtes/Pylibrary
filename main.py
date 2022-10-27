from datetime import datetime
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier
import os


#Iniciador da bilbioteca responsavel por não abrir o navegador
crhome_options = Options()
crhome_options.add_argument("--headless")
#options=crhome_options

#Iniciador da biblioteca responsavel por exibir notificações no computador
toast = ToastNotifier()

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=crhome_options)
 
link = 'https://biblioteca.ifrs.edu.br/pergamum_ifrs/biblioteca_s/php/login_usu.php?flag=index.php'
navegador.get(url=link)

def verify_login():
    #Função responsavel por verificar se os dados de login foram adicionados dentro do arquivo

    arquivo = 'arquivo.txt'
    
    if os.path.isfile(arquivo):

        arquivo = open("arquivo.txt", "r")
        conteudo = arquivo.readline()

        login = conteudo[0:10]
        senha = conteudo[10:16]

        return [login,senha]

    else:

        arquivo = open("arquivo.txt", "a")

        login = input("Digite sua matricula: ")
        senha = input("Digite sua senha: ")

        acesso = list()
        acesso.append(login)
        acesso.append(senha)

        arquivo.writelines(acesso)

        arquivo.close()

        return [login,senha]

#Desenvolver uma etapa que ira verificar se tem um arquivo com email e senha, se tiver acessa o site, do contrario pede ao usuario e adiciona
#Em um arquivo txt

def preencher_campos_login(login,senha):
    #Função que faz o login no site do IFRS

    campo_email = navegador.find_element(By.ID, 'id_login')
    campo_email.send_keys(login)
 
    campo_senha = navegador.find_element(By.ID, 'id_senhaLogin')
    campo_senha.send_keys(senha)

    botao_entrar = navegador.find_element(By.ID, "button")
    botao_entrar.click()

    print("Conectado!!")

def click_renovar():
    #Botão que renova o livro

    click_button = navegador.find_element(By.CLASS_NAME, "btn_renovar")
    click_button.click()

    print("Renovando livro")

def captu_infos():
    #Função que captura as informações do livro

    titulo = navegador.find_element(By.XPATH, "//*[@id='Accordion1']/div[1]/div[2]/table/tbody/tr[2]/td[2]/a").text
    toast.show_toast("Livro", "{}".format(titulo), duration=5)

    
    print("Infos livro")

def infos_att():
    #Captura informações já atualizadas do livro - Data para próxima renovação

    navegador.execute_script("window.history.go(-1)")

    data = navegador.find_element(By.XPATH, "//*[@id='Accordion1']/div[1]/div[2]/table/tbody/tr[2]/td[3]").text

    data = datetime.strptime(data, '%d/%m/%Y').date()

    toast.show_toast("Próxima renovação no dia", "{}".format(data), duration=5)

    print("Finalizado")

valores = verify_login()
preencher_campos_login(valores[0], valores[1])
click_renovar()
captu_infos()
infos_att()