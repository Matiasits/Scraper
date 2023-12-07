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

def buscar_recetas_por_ingrediente(url, ingrediente):
    response = requests.get(url + f"?s={ingrediente}")
    html = response.content
    soup = BeautifulSoup(html, "html.parser")

    # Expresión regular para encontrar enlaces de recetas.
    patron_recetas = re.compile(r'<a[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)<\/a>', re.IGNORECASE)

    # Encontrar todas las coincidencias usando la expresión regular.
    recetas_encontradas = [(a['href'], a.text.strip()) for a in soup.select('.entry-title a')]

    return recetas_encontradas

# URL de la página principal
url_principal = "https://www.paulinacocina.net/"

# Obtener información de la página principal
titulos_principales, enlaces_categorias, enlace_siguiente = scrape_pagina_principal(url_principal)

# Imprimir resultados generales
print(f"\nEnlaces de la Página Principal:\n{titulos_principales}\n \nEnlaces de Categorías:\n{enlaces_categorias}\n")

# Ingrediente a buscar (puedes cambiarlo según tus necesidades)
ingrediente_a_buscar = input("Ingrese un nombre de ingrediente: ")

# Si se proporcionó un ingrediente, buscar recetas por ingrediente
if ingrediente_a_buscar:
    recetas_por_ingrediente = buscar_recetas_por_ingrediente(url_principal, ingrediente_a_buscar)
    # Imprimir recetas encontradas
    print(f"\nRecetas que contienen '{ingrediente_a_buscar}':\n")
    for enlace, nombre in recetas_por_ingrediente:
        print(f"Nombre: {nombre}\nEnlace: {enlace}\n")
