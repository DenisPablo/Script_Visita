from selenium import webdriver
import time
import os

# obtener la ruta absoluta del archivo del driver
driver_path = os.path.abspath("chromedriver")

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Ejecutar en segundo plano (sin abrir ventana del navegador)
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Función para visitar el sitio web
def visit_website():
    driver.get("https://denispablo-portfolio.onrender.com/")
    print("Sitio web visitado.")

# Loop principal que visita el sitio cada hora
while True:
    visit_website()
    time.sleep(3600)  # Esperar 1 hora