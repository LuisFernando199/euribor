import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# # Hacemos una solicitud GET a la página web
# url = "https://www.bde.es/webbe/es/estadisticas/temas/tipos-interes.html"
# response = requests.get(url)
# print(response.status_code)

# # Parseamos el HTML con BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')

# # Encontramos el elemento que contiene el valor del Euribor a un año
# euribor_element = soup.find('p', {'class': 'block-card-indicator__value'})

# print(response.text)

# if euribor_element:
#     # Extraemos el valor del Euribor a un año
#     euribor_value = euribor_element.text.strip()
#     print("Euribor a un año:", euribor_value)
# else:
#     print("No se encontró el elemento que contiene el valor del Euribor a un año")



# Inicializamos el navegador
driver = webdriver.Chrome()  # Reemplaza con el navegador que desees

# Navegamos a la página web
driver.get("https://www.bde.es/webbe/es/estadisticas/temas/tipos-interes.html")

# Esperamos a que el contenido se cargue
driver.implicitly_wait(10)  # Espera 10 segundos

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontramos el elemento que contiene el valor del Euribor a un año
euribor_element = soup.find('p', {'class': 'block-card-indicator__value'})

if euribor_element:
    # Extraemos el valor del Euribor a un año
    euribor_value = euribor_element.text.strip()
    print("Euribor a un año:", euribor_value)
else:
    print("No se encontró el elemento que contiene el valor del Euribor a un año")

# Cerramos el navegador
driver.quit()
