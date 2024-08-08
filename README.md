# Web Scraping Euribor a Un Año

Este proyecto de Python realiza web scraping para obtener el valor del Euribor a un año desde la página web del Banco de España.

## Descripción

El script está dividido en dos partes principales:

1. **Requests y BeautifulSoup**: 
   - Hace una solicitud GET a la página web del Banco de España.
   - Parse el HTML utilizando BeautifulSoup.
   - Encuentra y extrae el valor del Euribor a un año.

2. **Selenium y BeautifulSoup**:
   - Inicializa un navegador utilizando Selenium.
   - Navega a la misma página web.
   - Espera a que el contenido se cargue.
   - Parse el HTML de la página cargada utilizando BeautifulSoup.
   - Encuentra y extrae el valor del Euribor a un año.
   - Cierra el navegador.

## Dependencias

Puedes instalar todas las dependencias ejecutando:

```bash
pip install -r requirements.txt
```


## Notas

- Asegúrate de tener instalado el controlador del navegador correspondiente (por ejemplo, `chromedriver` para Google Chrome).
- Puedes reemplazar `webdriver.Chrome()` con el navegador de tu preferencia.
- Modifica el tiempo de espera (`implicitly_wait`) si es necesario, dependiendo de la velocidad de tu conexión a internet.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
