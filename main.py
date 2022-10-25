from pydoc import classname
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from win10toast import ToastNotifier

#Iniciador da bilbioteca responsavel por não abrir o navegador
crhome_options = Options()
crhome_options.add_argument("--headless")

#Iniciador da biblioteca responsavel por exibir notificações no computador
toast = ToastNotifier()

navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=crhome_options)
 
link = 'https://biblioteca.ifrs.edu.br/pergamum_ifrs/biblioteca_s/php/login_usu.php?flag=index.php'
navegador.get(url=link)
 
email = '2022002041'
senha = '231001'
 
sleep(5)

def preencher_campos_login(email,senha):
    campo_email = navegador.find_element(By.ID, 'id_login')
    campo_email.send_keys(email)

    sleep(1)
 
    campo_senha = navegador.find_element(By.ID, 'id_senhaLogin')
    campo_senha.send_keys(senha)

    sleep(1)

    botao_entrar = navegador.find_element(By.ID, "button")
    botao_entrar.click()

    print("Conectado!!")

#def click_renovar():
#    click_button = navegador.find_element(By.CLASS_NAME, "btn_renovar")
#    click_button.click()

def captu_infos():

    titulo = navegador.find_element(By.XPATH, "//*[@id='Accordion1']/div[1]/div[2]/table/tbody/tr[2]/td[2]/a").text
    toast.show_toast("Livro", "{}".format(titulo), duration=90)

preencher_campos_login(email,senha)
#click_renovar()
captu_infos()