from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time
import pyautogui as pg
import sys


# WEB
# --------------------------------------------------------------
class WBrowser:
    '''
    Classe que contém as funções de navegação do navegador
    ----
     chrome_browser():

        - Faz a configuração do Browser para ser utilizado, abrindo o navegador através da passagem do caminho do chrome e chromedriver.

        - Requere a passagem por parâmetro do site à ser aberto, opção de rodar em segundo plano com headless e a opção de abrir maximizado (padrão), através do maximized.

        - Retorna o ~driver~ para navegação.

     open_tab():

        - Abre uma aba no navegador.
        
        - Requer a passagem por parâmtro do driver, e um "url" caso desejado (abre em branco por padrão).
        
        - Retorna o ~driver~ para navegação.

     change_tab():

        - Altera entre as abas do navegador.
        
        - Requer a passagem por parâmetro do driver e a aba desejada (ordem das abas correspondem à ordem em que foram abertas, primeira aba é zero, segunda é um...).
        
        - Retorna o ~driver~ para navegação.
        '''
    def chrome_browser(site='chrome://newtab', headless=False, maximized=True):
        '''
        chrome_browser():

            - Faz a configuração do Browser para ser utilizado, abrindo o navegador através da passagem do caminho do chrome e chromedriver.

            - Requere a passagem por parâmetro do site à ser aberto, opção de rodar em segundo plano com headless e a opção de abrir maximizado (padrão), através do maximized.

            - Retorna o ~driver~ para navegação.
            '''
        chrome_options = webdriver.ChromeOptions()
        if (maximized == True):
            chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--enable-chrome-browser-cloud-management')
        if (headless == True):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("window-size=1920,1080");       
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.binary_location = r"chrome-win64\chrome.exe"
        chrome_driver_path = r"chromedriver-win64\chromedriver.exe"
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(options=chrome_options, service=service_options)

        driver.get(site)

        return (driver)

    def open_tab(driver, url=''):
        '''
        open_tab():

            - Abre uma aba no navegador.
            
            - Requer a passagem por parâmtro do driver, e um "url" caso desejado (abre em branco por padrão).
            
            - Retorna o ~driver~ para navegação.
            '''
        driver.execute_script('window.open("' + str(url) + '");')
        time.sleep(1)
        return driver

    def change_tab(driver, tab):
        '''
        change_tab():

            - Altera entre as abas do navegador.
            
            - Requer a passagem por parâmetro do driver e a aba desejada (ordem das abas correspondem à ordem em que foram abertas, primeira aba é zero, segunda é um...).
            
            - Retorna o ~driver~ para navegação.
            '''
        driver.switch_to.window(driver.window_handles[tab])
        time.sleep(1)
        return driver

class WForms:
    '''
    Classe de elementos de formulários
    ---
    select():

        - Seleciona uma opção em uma lista (select) da página, utilizando a função visible para achar o elemento, da classe Waits.

        - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor, as tentativas, se buscará a opção por texto (True ou False), opção (caso busque pelo index) e o texto desejado pra busca.

        - Retorna a seleção do elemento. 
    '''
    def select(driver, by_tipe, selector, tries=5, by_text=False, option=0, text=''):
        '''
        select():

            - Seleciona uma opção em uma lista (select) da página, utilizando a função visible para achar o elemento, da classe Waits.

            - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor, as tentativas, se buscará a opção por texto (True ou False), opção (caso busque pelo index) e o texto desejado pra busca.

            - Retorna a seleção do elemento. 
            
            '''
        select = Select(Waits.visible(driver, by_tipe, selector, tries))
        if by_text == True:
            return select.select_by_visible_text(text)
        else:
            return select.select_by_index(option)

class WWaits:
    '''
    Classe de agurdar elementos no navegador
    ---
    clickable():
        
        - Faz uma busca de um elemento clicável no navegador, durante um determinado tempo.

        - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor e a quantidade de tentativas (tempo em segundos) que serão realizadas.

        - Retorna o elemento.
            
    visible():
        
        - Faz uma busca de um elemento visível no navegador, durante um determinado tempo.

        - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor e a quantidade de tentativas (tempo em segundos) que serão realizadas.

        - Retorna o elemento.

    title():

        - Aguarda o título da aba do naegador se alterar

        - Requer a passagem por parâmetro do driver, o título desejado e a quantidade de tentatvias (tempo em segundos) que serão realizadas.

        - Retorna o título.
    
    '''

    def clickable(driver, by_tipe, selector, tries=5):
        '''
        clickable():
        
            - Faz uma busca de um elemento clicável no navegador, durante um determinado tempo.

            - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor e a quantidade de tentativas (tempo em segundos) que serão realizadas.

            - Retorna o elemento.
        '''
        return WebDriverWait(driver,tries).until(EC.element_to_be_clickable((by_tipe, selector)))
    
    def visible(driver, by_tipe, selector,tries=5):
        '''
        visible():
        
            - Faz uma busca de um elemento visível no navegador, durante um determinado tempo.

            - Requer a passagem por parâmetro do driver, o tipo do elemento, o seletor e a quantidade de tentativas (tempo em segundos) que serão realizadas.

            - Retorna o elemento.
        '''
        return WebDriverWait(driver,tries).until(EC.visibility_of_element_located((by_tipe, selector)))
    def title(driver, title, tries=5):
        '''
        title():

            - Aguarda o título da aba do naegador se alterar

            - Requer a passagem por parâmetro do driver, o título desejado e a quantidade de tentatvias (tempo em segundos) que serão realizadas.

            - Retorna o título.
        '''
        return WebDriverWait(driver,tries).until(EC.title_is(title))
    
# DESKTOP
# --------------------------------------------------------------
class Desktop:
    def open_program():
        return

    def max(window_name):
        pg.getWindowsWithTitle(window_name)[0].maximize()

    def min(window_name):
        pg.getWindowsWithTitle(window_name)[0].minimize()
    
class Screen:
    def locate_ons(image_path):
        try:
            position = pg.locateOnScreen(image_path, confidence=0.7)
        except Exception as error:
            print(error)
        print(f"Seletor localizado em: {position}")
        return position

    def try_locate_image(imagePath, try_count=0, tries=5):
        while try_count >= 0:
            position = pg.locateOnScreen(imagePath)
            time.sleep(1)
            try_count += 1
            print(try_count)
            if try_count >= tries or position is not None:
                break
        try:
            if position is not None:
                print(f"position = {position}")
                return position
            else:
                raise Exception(f'Imagem: "{imagePath}", não localizada')
        except Exception as error:
            print(error)
            pg.screenshot(r'assets\images\ERROR_screenshot.png')
            sys.exit()