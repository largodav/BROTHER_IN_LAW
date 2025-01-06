# Se sigue https://github.com/lkuffo/web-scraping/tree/master/NIVEL%203
"""
OBJETIVO: 
    - Selenium en 2023: Objeto service y ChromeDriverManager
    - Selenium en Headless mode (sin navegador)
CREADO POR: LEONARDO KUFFO
ULTIMA VEZ EDITADO: 16 ENERO 2024
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
#opts.add_argument("--headless") # Headless Mode
# Agregar a todos sus scripts de selenium para que no aparezca la ventana de seleccionar navegador por defecto: (desde agosto 2024)
opts.add_argument("--disable-search-engine-choice-screen")

# Ahora podemos utilizar Selenium sin configurar el chromedriver (Julio 2023, Chrome > 115)
# Aunque en Mac esto tiene problemas
# driver = webdriver.Chrome(options=opts)

# Descarga automática del ChromeDriver
# Recomiendo esta forma de instanciar el ChromeDriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# Alternativamente:
# driver = webdriver.Chrome(
#     service=Service('./chromedriver'),
#     options=opts
# )

driver.get('https://cuenta.elcorteingles.es/oauth/authorize?response_type=code&scope=openid%20profile%20plans&client_id=rjx5snOWlh40SgcE0dg2guk4YnXhECYd&redirect_uri=https%3A%2F%2Fwww.elcorteingles.es%2Fecivuestore%2Fsession%2Fcallback%3Fto%3D%252F&back_to=https%3A%2F%2Fwww.elcorteingles.es%252F&locale=es&_gl=1*so84cg*_gcl_aw*R0NMLjE3MzU5MDEyOTcuQ2owS0NRaUFzdDY3QmhDRUFSSXNBS0tkV09tc3V1UEt3ZnNqcEE5N2xyUjlsRUhXd0o5Z3ZQdDFzUW5DY05ZdHByWHl5dVUwTlZTYXZWd2FBblRURUFMd193Y0I.*_gcl_dc*R0NMLjE3MzU5MDEyOTcuQ2owS0NRaUFzdDY3QmhDRUFSSXNBS0tkV09tc3V1UEt3ZnNqcEE5N2xyUjlsRUhXd0o5Z3ZQdDFzUW5DY05ZdHByWHl5dVUwTlZTYXZWd2FBblRURUFMd193Y0I.*_gcl_au*ODM5OTM4MjMyLjE3MzU4NjEzNzM.*_ga*MzA1OTEzODMxLjE3MzU4NjEzNjk.*_ga_XG9L1L3E0D*MTczNTkwMDQ3MC4yLjEuMTczNTkwMjIyMC41OS4wLjA.')

sleep(300)

# titulos_anuncios = driver.find_elements(By.XPATH, '//div[@data-testid="listing-card-title"]')
# for titulo in titulos_anuncios:
#     print(titulo.text)

# sleep(300)   
