from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

import time, sys, os, win32com.client
import pyautogui as pg
import pandas as pd

# -- Para automação sicredi
from win32com.client import Dispatch
from selenium.webdriver.chrome.service import Service

# region WEB
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
            
    close_tab():
        
        - Fecha a abas do navegador.

        - Requer a passagem por parâmetro do driver e a quantidade de abas que vão ser fechadas.

    quit_browser():
        
        - Fecha o navegador.

        - Requer a passagem por parâmetro do driver.
        '''
    def chrome_browser(site='chrome://newtab', headless=False, maximized=True):
        '''
        chrome_browser():

            - Faz a configuração do Browser para ser utilizado, abrindo o navegador através da passagem do caminho do chrome e chromedriver.

            - Requere a passagem por parâmetro do site à ser aberto, opção de rodar em segundo plano com headless e a opção de abrir maximizado (padrão), através do maximized.

            - Retorna o ~driver~ para navegação.
            '''
        
        # Configurações do Chrome
        chrome_options = webdriver.ChromeOptions()
        
        # Verifica se inicia maximizado
        if (maximized == True):
            chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--enable-chrome-browser-cloud-management')

        # verifica se inicia em segundo plano
        if (headless == True):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("window-size=1920,1080");       
        
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # Caminho do Chrome e Chromedriver
        chrome_options.binary_location = r"chrome-win64\chrome.exe"
        chrome_driver_path = r"chromedriver-win64\chromedriver.exe"

        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(options=chrome_options, service=service_options)

        # Obtém e retorna o driver
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
    
    def close_tab(driver):
        '''
        close_tab():
        
            - Fecha a aba do navegador.

            - Requer a passagem por parâmetro do driver.
            '''
        driver.close()
        return driver

    def quit_browser(driver):
        '''
        quit_browser():
        
            - Fecha o navegador.

            - Requer a passagem por parâmetro do driver.
            '''
        return driver.quit()
    
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

        select = Select(WWaits.visible(driver, by_tipe, selector, tries))
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

# endregion WEB
    
# region DESKTOP
# --------------------------------------------------------------
class DPrograms:
    def open_program(path):
        '''
        open_program():

            - Abre um programa no computador.

            - Requer a passagem por parâmetro do caminho onde está o programa.
        '''
        os.startfile(path)

    def max(window_name):
        '''
        max():

            - Maximiza uma janela do computador.

            - Requer a passagem por parâmetro do nome da janela.
        '''
        pg.getWindowsWithTitle(window_name)[0].maximize()

    def min(window_name):
        '''
        min():

            - Minimiza uma janela do computador.

            - Requer a passagem por parâmetro do nome da janela.
        '''
        pg.getWindowsWithTitle(window_name)[0].minimize()
    
class DSSheets:

    def windows_excel_refresh_query(path, visible = True):
        '''
        windows_excel_refresh_query():

            - Recarrega a consulta de um arquivo Excel.

            - Requer a passagem por parâmetro do caminho do arquivo e se a operação será visível ou rodada em segundo plano.
        '''
        # Obtém o nome do arquivo Excel
        arquivo = path.split('/')
        arquivo = arquivo[-1]
        print(arquivo)

        # Inicia o Excel
        excel = win32com.client.DispatchEx("Excel.Application")
        
        # Determina se será em segundo plano
        excel.visible = visible
        print('1. excel aberto.')

        # Cria o Workbook
        if excel.Workbooks.Count > 0:
            for i in range(1, excel.Workbooks.Count+1):
                if excel.Workbooks.Item(i).Name is arquivo:
                    wb = excel.Workbooks.Item(i)
                    break

        # Abre o arquivo 
        wb = excel.Workbooks.Open(path)
        print('2. Arquivo selecionado.')

        #Recarrega a A Query
        wb.RefreshAll()
        print('3. Atualizando dados.')

        # Aguarda até ela finalizar
        excel.CalculateUntilAsyncQueriesDone()
        print('4. Consulta finalizada.')

        # Salva e fecha o arquivo
        wb.Save()
        print('5. Arquivo salvo.')
        excel.Quit()
        print('6. Finalizado.')

    def excel_to_csv(path, path_save=''):
        '''
        excel_to_csv():

            - Converte um arquivo Excel para um arquivo .csv

            - Requer a passagem por parâmetro do caminho do arquivo Excel a opção do caminho para salvar caso seja em um local diferente.
        '''
        # Lê o nome do arquivo
        if (path_save != ''):
            arquivoxls = path.split('/')
            arquivoxls = arquivoxls[-1]

            # Altera para '.csv'
            arquivocsv = arquivoxls.split('.')
            arquivocsv = str(arquivocsv[0]) + '.csv'

            # Substitui o antigo pelo novo
            path_save = path.replace(arquivoxls, arquivocsv)

        # Faz a leitura do arquivo com pandas
        print(path)
        arquivo = pd.read_excel(path)
        arquivo.to_csv (path_save, index=None, header=True)
        print('\nArquivo salvo em: ' + path_save)

    def csv(path_csv, row, operation):
        '''
        csv():

            - Realiza operações em arquivos CSV

            - Requer a passagem por parâmtro do caminho e a linha à ser escrita ou adicionada, assim como a operação.
                ---
            Operações: 

            a > append > Adiciona uma linha no arquivo CSV

            w >  write > Escreve uma linha no arquivo CSV, limpando o que continha antes
        '''
        # Append (Adiciona uma linha)
        if operation == 'a':
            # Abre o arquivo no modo append e cria um objeto dele
            with open(path_csv, 'a') as csv:
                # Cria um writer para adiocnar informações
                csv_writer = writer(csv)
                # Passa a linha à ser adicionada
                csv_writer.writerow(row)
                # Fecha o arquivo
                csv.close()
        # Write (Escreve uma linha)
        if operation == 'w':
            # Abre o arquivo no modo append e cria um objeto dele
            with open(path_csv, 'w') as csv:
                # Cria um writer para adiocnar informações
                csv_writer = writer(csv)
                # Passa a linha à ser adicionada
                csv_writer.writerow(row)
                # Fecha o arquivo
                csv.close()


class DScreen:
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
# endregion DESKTOP
