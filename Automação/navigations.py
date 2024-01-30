from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pg
import sys
import time


class Browser:
    def chrome_browser(site, headless=False, maximized=True):
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
        driver.execute_script('window.open("' + str(url) + '");')
        time.sleep(1)
        return driver

    def change_tab(driver, position):
        driver.switch_to.window(driver.window_handles[position])
        time.sleep(1)
        return driver



# Espera identificar um elemento na tela    
class Waits:
    def clickable(driver, by_tipe, selector, tries=5):
        return WebDriverWait(driver,tries).until(EC.element_to_be_clickable((by_tipe, selector)))
    def visible(driver, by_tipe, selector,tries=5):
        return WebDriverWait(driver,tries).until(EC.visibility_of_element_located((by_tipe, selector)))
    def title(driver, title, tries=5):
        return WebDriverWait(driver,tries).until(EC.title_is(title))


#---------------------------------------

class Desktop:
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
