import time
import pyautogui as pg
import sys
import time


class Desktop:
    def open_program

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
