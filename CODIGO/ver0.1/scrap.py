from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



driver = webdriver.Chrome()

driver.get('https://www.elcorteingles.es/search-nwx/')

# boton_buscar = WebDriverWait(driver,10).until(
#     EC.presence_of_all_elements_located((By.XPATH,"//input[@class='search-bar__input']"))    
# )
text = "mi texto"
# boton_buscar[0].send_keys(text)

#Entramos en la pagina de buscar y obtenemos la "barra de busqueda"
element = driver.find_element(By.CLASS_NAME,"search-bar__input")

#Se detecta que salta una pantalla de "Politica de Cookies".... <div id="onetrust-group-container" class="ot-sdk-twelve ot-sdk-columns">...</div>
#Que detexta un primer uso de la pagina. 
#Debemos "saltarnos dicha pantalla"
#El BOTON DE "ACEPTAR COOKIES" ES id="ontrust-accept-btn-handler".... DENTRO DE UN DIV GENERAL.. id="onetrust-banner-sdk"

element.click()
element.send_keys(text)

driver.quit()








