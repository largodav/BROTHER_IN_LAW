from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


# driver = webdriver.Chrome()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Mandamos el input a buscar, establecemos busqueda de prueba...
producto = "15215594357"

driver.get(f"https://www.elcorteingles.es/search-nwx/1/?s={producto}&stype=text_box")
driver.implicitly_wait(10)
# time.sleep(35)

# # Esperamos a que aparezca el div d elas cookies
div_cookies = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.ID, "onetrust-accept-btn-handler"))
)
div_cookies[0].click()
# # Espera....
# #time.sleep(2005)

# Nos da el resultado de la busqueda....
resultado = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "card"))
)
#DEEBEMOS OBTENER INFORMACION DE LA URL DEL PRODUCTO PARA CONTINUAR...
href_producto = WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"product_link"))
)
#TEnemos la URL del producto
url_producto= href_producto[0].get_attribute("data-url")
print(url_producto)



time.sleep(2005)

