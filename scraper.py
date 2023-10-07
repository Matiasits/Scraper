import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la página web que deseas analizar
url = 'https://www.paulinacocina.net/'

# Realizar una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido de la página web con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Inicializar listas para los títulos y enlaces
    titulos_h1 = []
    titulos_h2 = []
    titulos_h3 = []
    enlaces = []
    
    # Encontrar todos los elementos de título (h1, h2, h3) en la página
    for nivel in range(1, 4):
        etiqueta = f'h{nivel}'
        titulos = soup.find_all(etiqueta)
        for titulo in titulos:
            texto = titulo.text.strip()
            if nivel == 1:
                titulos_h1.append(texto)
            elif nivel == 2:
                titulos_h2.append(texto)
            elif nivel == 3:
                titulos_h3.append(texto)
    
    # Encontrar todos los enlaces en la página
    enlaces = soup.find_all('a')
    
    # Mostrar los títulos h1, h2 y h3
    print("Títulos h1:")
    for titulo in titulos_h1:
        print(titulo)
    
    print("\nTítulos h2:")
    for titulo in titulos_h2:
        print(titulo)
    
    print("\nTítulos h3:")
    for titulo in titulos_h3:
        print(titulo)
    
    # Mostrar las URLs de los enlaces
    print("\nEnlaces:")
    for enlace in enlaces:
        # Obtener el atributo 'href' del enlace
        href = enlace.get('href')
        
        # Combinar la URL base con la URL relativa del enlace, si es necesario
        enlace_completo = urljoin(url, href)
        
        # Imprimir la URL completa
        print(enlace_completo)
        
else:
    print('No se pudo acceder a la página:', response.status_code)