from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time




def buscar_por_ref(referencia):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #ESTO "minimiza" LA VENTANA CHROME
    driver.minimize_window()
    
    # Mandamos el input a buscar, establecemos busqueda de prueba...

    driver.get(f"https://www.elcorteingles.es/search-nwx/1/?s={referencia}&stype=text_box")
    #driver.get("https://www.elcorteingles.es/search-nwx/1/?s=15215500693&stype=text_box")
    driver.implicitly_wait(5)
    # time.sleep(35)
    # # Esperamos a que aparezca el div d elas cookies
    div_cookies = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.ID, "onetrust-accept-btn-handler"))
    )
    div_cookies[0].click()
    # # Espera....
    # #time.sleep(2005)

    #DEBEMOS CHEQUEAR SI EXISTE RESPUESTA O NO....

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
    #print(url_producto)
    driver.close()

    #TENEMOS URL DEL PRODUCTO ESPECIFICO, pero ¿tenemos que volvera repetir todo el proiceso????? USO DE SESIONES...
    driver = webdriver.Chrome(
        
    )

    driver.set_window_size(1920,1080)
            
    #ESTO "OCULTA" LA VENTANA CHROME
    driver.minimize_window()
    driver.get(url_producto)

    # # Esperamos a que aparezca el div d elas cookies
    div_cookies = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.ID, "onetrust-accept-btn-handler"))
    )
    div_cookies[0].click()

    #Obtenemos foto del producto, nombre completo y descripcion, Y SI HAY E.T EN POZUELO... ESTO ES LO QUE DEVOLVEMOS AL BOT...
    class_img_producto = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"carousel-elements__item_img"))
    )
    imagen_producto = class_img_producto[0].get_attribute("src")

    class_nom_producto= WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"product_detail-title"))
    )
    nombre_producto = class_nom_producto[0].text

    #time.sleep(2005)
    #Buscamos el Click en "caracteristicas"

    caracteristicas = WebDriverWait(driver,20).until(     
        EC.presence_of_all_elements_located((By.CLASS_NAME,"pdp-list-item__text"))
    )
    driver.implicitly_wait(5)
    #print(caracteristicas[0])
    caracteristicas[0].click()
    #caracteristicas[0].click()
    class_descripcion_producto = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME,"composition__value"))
    )
    caracteristicas_producto = class_descripcion_producto[0].text
    driver.implicitly_wait(5)
    #Cerrando el DRIVER
    driver.close()
    #print(f"Descripcion del producto: {class_descripcion_producto[0].text}")
    # print(f"Imagen del Producto: {imagen_producto}")
    # print(f"Nombre del producto: {nombre_producto}")
    # print(f"Caracteristicas del producto: {caracteristicas_producto}")
    #time.sleep(2005)
    return imagen_producto,nombre_producto,caracteristicas_producto

#CODIGO PARA COMPROBAR EXISTENCIA DEL PRODUCTO EN TIENDA
def existencia_centro():
    # #DEBEMOS CERRAR VENTA DE CARACTERISTICAS
    # boton_cerrar_caracteristicas = WebDriverWait(driver,10).until(
    #     EC.presence_of_all_elements_located((By.ID,"modal-close"))
    # )
    # #print(boton_cerrar_caracteristicas)
    # boton_cerrar_caracteristicas[0].click()

    #time.sleep(10)
    #CHEQUEAMOS EXISTENCIA TEORICA EN POZUELO
    # class_disponibilidad = WebDriverWait(driver,10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME,"product_detail-aside--search_in_shop-text"))
    # )
    # #print(class_disponibilidad)
    # class_disponibilidad[0].click()
    # #Ya estamos en la sub pantalla de seleccionar provincia y tienda
    # #listbox_9597a02c-d311-3e8f-83ab-8d31efe5b95a
    # class_provincia = WebDriverWait(driver,10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME,"dropdown-input_text"))
    # )
    # time.sleep(2)
    # print(class_provincia[0].text)


    # # time.sleep(10)
    # boton_provincia = WebDriverWait(driver,10).until(
    #     EC.presence_of_all_elements_located((By.CLASS_NAME,"dropdown-icon"))
    # )
    # boton_provincia[0].click()
    time.sleep(5005)