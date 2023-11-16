import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import re

li = [
    'menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-11384',
    'menu-item menu-item-type-taxonomy menu-item-object-category menu-item-has-children menu-item-451',
    'menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-21292'
    ]
    

def get_categorias_con_enlaces():
    """Obtiene una lista de las categorías del menú de Paulina Cocina haciendo scraping, incluyendo los enlaces de cada subcategoría."""
    
    for i in li:    
        # Crear una solicitud HTTP a la página web.
        response = requests.get("https://www.paulinacocina.net/")
        # Obtener el código HTML de la respuesta.
        html = response.content
        # Usar BeautifulSoup para parsear el código HTML.
        soup = BeautifulSoup(html, "html.parser")
        # Buscar las etiquetas `<li>` con la clase `categoria`.
        categorias = soup.find_all("li", class_=i)
        # Extraer los nombres de las categorías.
        nombres = [categoria.find("a").text for categoria in categorias]
        # Extraer los enlaces de las categorías.
        enlaces = [categoria.find("a")["href"] for categoria in categorias]
        # Devolver una lista con los nombres y enlaces de las categorías.
        print(list(zip(nombres, enlaces)))
        
        
        for j in enlaces:
            # Crear una solicitud HTTP a la página web.
            response = requests.get(j)
            # Obtener el código HTML de la respuesta.
            html = response.content
            # Usar BeautifulSoup para parsear el código HTML.
            soup = BeautifulSoup(html, "html.parser")
            # Buscar las etiquetas `<li>` con la clase `categoria`.
            categoriasSub = soup.find_all("li", class_=re.compile("menu-item"))
            # Iterar sobre las subcategorías y extraer nombres y enlaces.
            for categoria_sub in categoriasSub:
                nombre_sub = categoria_sub.find("a").text
                enlace_sub = categoria_sub.find("a")["href"]
                print(f"Subcategoría: {nombre_sub}, Enlace: {enlace_sub}")
    
        
get_categorias_con_enlaces()