from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

driver = iniciar_driver()
driver.get('https://www.amazon.com.br/s?k=Celular&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1YIHDLNNPWJHI&sprefix=celular%2Caps%2C190&ref=nb_sb_noss_2')

input('digite para fechar')