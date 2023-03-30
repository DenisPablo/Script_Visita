from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os

# obtener la ruta absoluta del archivo del driver
driver_path = os.path.abspath("chromedriver")

# Configuración del navegador
options = webdriver.ChromeOptions()

# Ejecutar en segundo plano (sin abrir ventana del navegador)
options.add_argument('--headless')

# Crear instancia del objeto Service
service = Service(executable_path=driver_path)

# Crear instancia del controlador
driver = webdriver.Chrome(service=service, options=options)

# Función para visitar el sitio web


def visit_website():
    driver.get("https://denispablo-portfolio.onrender.com/")
    print("Sitio web visitado.")


# Loop principal que visita el sitio cada hora
while True:
    visit_website()
    time.sleep(3600)  # Esperar 1 hora
