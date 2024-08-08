import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# Inicializamos el navegador
driver = webdriver.Chrome()  # Reemplaza con el navegador que desees

# Navegamos a la página web
driver.get("https://www.idealista.com/news/euribor/historico-diario/")

# Esperamos a que el contenido se cargue
driver.implicitly_wait(10)  # Espera 10 segundos

# Parseamos el HTML con BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontramos la tabla que contiene los datos del Euribor
table = soup.find('table', {'class': 'component-table table'})

if table:
    # Encontramos la primera fila de la tabla
    row = table.find('tr', {'class': 'table__row'})

    if row:
        # Encontramos las celdas de la fila
        cells = row.find_all('td', {'class': 'table__cell'})

        if cells:
            # Extraemos los valores de las celdas
            year = cells[0].text.strip()
            month = cells[1].text.strip()
            euribor = cells[2].text.strip()
            print("Año:", year)
            print("Mes:", month)
            print("Euribor:", euribor)
        else:
            print("No se encontraron las celdas que contienen los valores del Euribor")
    else:
        print("No se encontró la fila que contiene los datos del Euribor")
else:
    print("No se encontró la tabla que contiene los datos del Euribor")

# Cerramos el navegador
driver.quit()

# Mantener la ventana abierta hasta que el usuario decida cerrarla
input("Presiona Enter para salir...")