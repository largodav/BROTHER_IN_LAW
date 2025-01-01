from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



driver = webdriver.Chrome()

driver.get('https://www.elcorteingles.es/search-nwx/')
#Esperamos a que aparezca el div d elas cookies
div_cookies = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"onetrust-accept-btn-handler")))
div_cookies[0].click()
#Buscamos el input de buscar
boton_buscar = driver.find_element(by=By.CLASS_NAME, value="search-bar__input")
boton_buscar.click()


boton_buscar.send_keys("hola")












