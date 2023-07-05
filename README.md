# Web Scraping de Datos 

Este script de Python se utiliza para realizar web scraping y extraer información relevante de cada página. La información extraída se guarda en un archivo de texto llamado "URL_EXPORT.txt".

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python antes de ejecutar el script:
- requests
- BeautifulSoup

Puedes instalar estas bibliotecas utilizando el administrador de paquetes pip. Ejecuta el siguiente comando en tu terminal:

```
pip install requests beautifulsoup4
```

## Uso

1. Abre el archivo `scraping_script.py` en tu editor de código.
2. Modifica la ruta del archivo de exportación según tus necesidades. La ruta actual es `C:\\Users\URL_EXPORT.txt`.
3. Dentro del bucle `for`, puedes ajustar el rango de páginas que deseas analizar modificando los valores `1` y `48` en la línea `for i in range(1, 48):`. Actualmente, el script recorre las páginas desde 1 hasta 47.
4. Ejecuta el script. Los datos extraídos se guardarán en el archivo especificado.

## Resultados

El script realiza las siguientes acciones:

1. Realiza una solicitud HTTP a cada URL de página de prueba.
2. Analiza el contenido HTML de cada página utilizando BeautifulSoup.
3. Extrae la información relevante de cada página, incluyendo el título, el precio y el año.
4. Guarda la información extraída en el archivo de exportación especificado.

Cada línea en el archivo de exportación contendrá la siguiente información separada por comas:
```
Number: {número}, Title: {título}, Price: {precio}, Year: {año}
```

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacerlo. Puedes abrir un problema o enviar una solicitud de extracción con tus mejoras.


