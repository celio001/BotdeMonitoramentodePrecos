from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager(version='114.0.5735.90').install()), options=chrome_options)

    return driver

#Iniciar o driver e abrir o site Amazon
driver = iniciar_driver()
driver.get('https://www.amazon.com.br/s?k=Celular&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1YIHDLNNPWJHI&sprefix=celular%2Caps%2C190&ref=nb_sb_noss_2')

#Descer para o final da pagina para carregar todos os produtos 
sleep(20)
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)

#Pegar o titulo dos produtos
titulos = driver.find_elements(
    By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]//span')

#Pegar o preço de cada produto
precos = driver.find_elements(
    By.XPATH, '//span[@class="a-price"]//span[@class="a-price-whole"]') #//span[@class="a-price"]//span #//span[@class="a-price"]//span[@class="a-price-whole"]


#Pegar o link de cada produto
links = driver.find_elements(
    By.XPATH, '//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]//a')

for titulo, preco, link in zip(titulos, precos, links):
    with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
        link_processado = link.get_attribute('href')
        arquivo.write(
            f'{titulo.text};{preco.text};{link_processado}{os.linesep}')

input('digite para fechar')

driver.close()