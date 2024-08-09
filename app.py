import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# Inicializamos el navegador
driver = webdriver.Chrome()  # Reemplaza con el navegador que desees

# Navegamos a la página web
driver.get("https://www.euribordiario.es/euribor-mensual")

# Esperamos a que el contenido se cargue
driver.implicitly_wait(10)  # Espera 10 segundos

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontramos la tabla que contiene los datos del Euribor
table = soup.find('table', {'class': 'table_eurdi'})

if table:
    # Iteramos sobre todas las filas de la tabla (excluyendo la primera fila de encabezado)
    rows = table.find_all('tr')[1:]

    for row in rows:
        # Encontramos las celdas de la fila
        cells = row.find_all('td')

        # Extraemos los valores de las celdas
        month = cells[0].text.strip()
        values = [cell.text.strip() for cell in cells[1:]]

        # Imprimimos el mes y los valores del Euribor de cada año
        print(f"Mes: {month}")
        for i, value in enumerate(values, start=2013):
            print(f"Año {i}: {value}")
        print("-" * 50)
else:
    print("No se encontró la tabla que contiene los datos del Euribor")

# Cerramos el navegador
driver.quit()

# Mantener la ventana abierta hasta que el usuario decida cerrarla
input("Presiona Enter para salir...")
