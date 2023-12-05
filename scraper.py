import requests
from bs4 import BeautifulSoup
import re

def scrape_pagina_principal(url):
    # Crear una solicitud HTTP a la página principal.
    response = requests.get(url)
    # Obtener el código HTML de la respuesta.
    html = response.content
    # Usar BeautifulSoup para parsear el código HTML.
    soup = BeautifulSoup(html, "html.parser")
# Expresión regular para buscar etiquetas de encabezado <h1> a <h6>
    patron_encabezados = re.compile(r'<[hH](\d)[^>]*>(.*?)<\/[hH]\1>')

# Encontrar todas las coincidencias usando la expresión regular
    titulos_principales = [match[1].strip() for match in patron_encabezados.findall(str(soup))]
    # Encontrar enlaces de categorías desde la página principal.
    enlaces_categorias = [a['href'] for a in soup.select('.menu-item-type-taxonomy.menu-item-object-category a')]

    # Encontrar el enlace de "PÁGINA SIGUIENTE" del botón.
    enlace_siguiente = soup.find('a', class_='next')['href'] if soup.find('a', class_='next') else None

    return titulos_principales, enlaces_categorias, enlace_siguiente

# URL de la página principal
url_principal = "https://www.paulinacocina.net/"

# Obtener información de la página principal
titulos_principales, enlaces_categorias, enlace_siguiente = scrape_pagina_principal(url_principal)

# Imprimir resultados
print(f"\nEnlaces de la Pagina Principal:\n{titulos_principales}\n \nEnlaces de Categorias:\n{enlaces_categorias}\n")