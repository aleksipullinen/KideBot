from multiprocessing.connection import wait
from selenium.webdriver.support.select import Select
from tkinter import *
from requests import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait            
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import subprocess


#Avaa ohjelman aina samassa selaimessa ja tietyllä välilehdellä
# Aja terminaaliin Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
# Ei muita välilehtiä auki

class Botti:
        def __init__(self):
                self.chrome_options = ""
                self.chrome_driver = ""         
                self.browser = ""

        def alusta_botti(botti):
                botti.chrome_options = webdriver.ChromeOptions()
                botti.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")        
                botti.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=botti.chrome_options)

        def paivita(botti):
                ostettu = False
                while True:
                        try:
                                lippu = WebDriverWait(botti.browser, 0.1, 0.001
                                ).until(EC.element_to_be_clickable((
                                By.XPATH,
                                '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[2]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[3]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[4]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[5]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[6]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[7]/o-accent'                    
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[8]/o-accent'
                                or '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[9]/o-accent'
                                )))
                                lippu.click()
                                ostettu = True
                                try:
                                        while True:
                                                try:
                                                        muuttuja = Select(botti.browser.find_element(By.XPATH,'/html/body/o-dialog__container/o-dialog/form/o-dialog__content/o-input-container/select'))
                                                        valinta = muuttuja.options                             
                                                        maara = str(len(valinta))
                                                        muuttuja.select_by_visible_text(maara)
                                                        break
                                                except:
                                                        
                                                        continue
                                                        

                                        #SIIRTÄÄ LIPUN OSTOSKORIIN
                                        while True:
                                                
                                                try:
                                                        koriin = WebDriverWait(botti.browser, 0.1, 0.001).until(EC.element_to_be_clickable((By.XPATH,
                                                        '/html/body/o-dialog__container/o-dialog/form/o-dialog__footer/o-dialog__footer__content/button[1]')))
                                                        koriin.click()
                                                        break
                                                except:
                                                        continue
                                except:
                                        break



                        except:                            
                                if ostettu == False:
                                        try:             
                                                WebDriverWait(botti.browser,0.1 ,0.001).until(EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[2]/button'))).click()
                                                continue
                                        except:
                                                continue

                                break

        
class Selain:
        def selain(botti):
                subprocess.Popen('Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"', 
                shell=True)
                Botti.alusta_botti(botti)



















            
            
  

# #Siirtää lipun ostoskoriin.
#     def ostoskoriin(self):
#         while True:
#          try:
#   WebDriverWait(self.browser, 60, 0.001).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-dialog__container/o-dialog/form/o-dialog__footer/o-dialog__footer__content/button[1]'))).click()
#             finally:
#                 break

# class Selain:
#     def avaaSelain():
#         subprocess.Popen(
#             'Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"',
#             shell=True,
#         )

#KIRJAUTUMISOSUUS
# browser.implicitly_wait(6)
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/header/o-toolbar/o-toolbar__controls/o-menu[2]/o-menu-button/o-action-chip'))).click()
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-menu-container/o-menu-content/o-menu-item[6]'))).click()
# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-menu-container/o-menu-content/o-menu-item[6]'))).click()
# sposti = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/o-input-container[1]/label'))).click()
# sposti = browser.find_element(By.XPATH,'/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/o-input-container[1]/input')
# sposti.send_keys("aleksi.pullinen@hotmail.fi")

# salasana = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/o-input-container[2]/label'))).click()
# salasana = browser.find_element(By.XPATH,'/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/o-input-container[2]/input')
# salasana.send_keys("salasana")

# kirjaudu = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/o-dialog__container/o-dialog/o-dialog__content[1]/form/button'))).click()
# sleep(2)
# browser.refresh()



#WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list'))).click()