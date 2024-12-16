from pick import pick  # Librería para selección de opciones
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configuración de Selenium
chrome_options = Options()
chrome_options.add_argument('--log-level=3')  # Minimiza los logs
chrome_options.add_argument("--disable-logging")  # Deshabilita registros adicionales
chrome_options.add_argument("--headless")  # Ejecuta en modo headless (sin abrir ventana)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Evita logs de DevTools

# Lista de categorías con URLs predefinidas
categorias = {
    "Accesorios para Vehículos": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1747#origin=home#CATEGORY_ID=MPE1747&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ACCESORIOS-PARA-VEHICULOS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Agro": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1512#origin=home#CATEGORY_ID=MPE1512&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=AGRO&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Alimentos y Bebidas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1403#origin=home#CATEGORY_ID=MPE1403&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ALIMENTOS-Y-BEBIDAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Animales y Mascotas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1071#origin=home#CATEGORY_ID=MPE1071&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ANIMALES-Y-MASCOTAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Arte, Librería y Mercería": "https://www.mercadolibre.com.pe/mas-vendidos/MPE443829#origin=home#CATEGORY_ID=MPE443829&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ARTE,-LIBRERIA-Y-MERCERIA&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Bebés": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1384#origin=home#CATEGORY_ID=MPE1384&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=BEBES&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Belleza y Cuidado Personal": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1246#origin=home#CATEGORY_ID=MPE1246&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=BELLEZA-Y-CUIDADO-PERSONAL&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Celulares y Teléfonos": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1051#origin=home#CATEGORY_ID=MPE1051&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=CELULARES-Y-TELEFONOS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Computación": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1648#origin=home#CATEGORY_ID=MPE1648&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=COMPUTACION&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Consolas y Videojuegos": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1144#origin=home#CATEGORY_ID=MPE1144&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=CONSOLAS-Y-VIDEOJUEGOS-&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Construcción": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1500#origin=home#CATEGORY_ID=MPE1500&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=CONSTRUCCION&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Cámaras y Accesorios": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1039#origin=home#CATEGORY_ID=MPE1039&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=CAMARAS-Y-ACCESORIOS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Deportes y Fitness": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1276#origin=home#CATEGORY_ID=MPE1276&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=DEPORTES-Y-FITNESS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Electrodomésticos": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1575#origin=home#CATEGORY_ID=MPE1575&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ELECTRODOMESTICOS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Electrónica, Audio y Video": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1000#origin=home#CATEGORY_ID=MPE1000&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ELECTRONICA,-AUDIO-Y-VIDEO&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Herramientas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE127606#origin=home#CATEGORY_ID=MPE127606&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=HERRAMIENTAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Hogar, Muebles y Jardín": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1574#origin=home#CATEGORY_ID=MPE1574&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=HOGAR,-MUEBLES-Y-JARDIN&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Industrias y Oficinas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1499#origin=home#CATEGORY_ID=MPE1499&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=INDUSTRIAS-Y-OFICINAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Instrumentos Musicales": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1182#origin=home#CATEGORY_ID=MPE1182&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=INSTRUMENTOS-MUSICALES&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Joyas y Relojes": "https://www.mercadolibre.com.pe/mas-vendidos/MPE3937#origin=home#CATEGORY_ID=MPE3937&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=JOYAS-Y-RELOJES&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Juegos y Juguetes": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1132#origin=home#CATEGORY_ID=MPE1132&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=JUEGOS-Y-JUGUETES&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Libros, Revistas y Comics": "https://www.mercadolibre.com.pe/mas-vendidos/MPE3025#origin=home#CATEGORY_ID=MPE3025&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=LIBROS,-REVISTAS-Y-COMICS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Música y Películas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1168#origin=home#CATEGORY_ID=MPE1168&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=MUSICA-Y-PELICULAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Recuerdos, Cotillón y Fiestas": "https://www.mercadolibre.com.pe/mas-vendidos/MPE112701#origin=home#CATEGORY_ID=MPE112701&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=RECUERDOS,-COTILLON-Y-FIESTAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Ropa y Accesorios": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1430#origin=home#CATEGORY_ID=MPE1430&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=ROPA-Y-ACCESORIOS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Salud y Equipamiento Médico": "https://www.mercadolibre.com.pe/mas-vendidos/MPE409431#origin=home#CATEGORY_ID=MPE409431&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=SALUD-Y-EQUIPAMIENTO-MEDICO&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
    "Otras categorías": "https://www.mercadolibre.com.pe/mas-vendidos/MPE1953#origin=home#CATEGORY_ID=MPE1953&S=hc_mas-vendidos&c_id=undefined&c_element_order=undefined&c_campaign=OTRAS-CATEGORIAS&c_uid=ae44f340-b9dd-11ef-84dc-9322ca2d5e8a",
}
# Función para extraer productos de una URL
def extraer_productos(driver, url, categoria):
    print(f"\n🔎 Extrayendo datos de la categoría: {categoria}...")
    driver.get(url)
    time.sleep(5)  # Esperar a que cargue la página

    productos_list = []

    try:
        # Encuentra el contenedor principal de productos
        container = driver.find_element(By.CSS_SELECTOR, 'div.ui-search-layout--grid__grid')
    except:
        print(f"No se encontró el contenedor principal en {categoria}")
        return productos_list

    # Encuentra los productos dentro del contenedor
    productos = container.find_elements(By.CSS_SELECTOR, 'div.ui-search-layout--grid__item')
    print(f"Encontrado {len(productos)} productos en {categoria}")

    # Recorre los productos y obtiene el nombre y el precio
    for producto in productos:
        try:
            # Obtener el nombre del producto
            nombre = producto.find_element(By.CSS_SELECTOR, 'a.poly-component__title').text

            # Obtener precios
            precios = producto.find_element(By.CSS_SELECTOR, 'div.poly-price__current')

            try:
                precio_entero = precios.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__fraction').text
            except:
                precio_entero = "0"

            try:
                precio_centimos = precios.find_element(By.CSS_SELECTOR, 'span.andes-money-amount__cents').text
            except:
                precio_centimos = "00"

            # Almacenar el producto
            productos_list.append({
                'categoria': categoria,
                'nombre': nombre,
                'precio': f"{precio_entero}.{precio_centimos}"
            })
        except:
            print("No se pudo obtener información del producto")

    return productos_list

# Función para mostrar el menú de opciones al inicio
def mostrar_menu():
    opciones = ["Extraer productos", "Salir"]
    titulo = "¿Bienvenido a la aplicación de scraping de MercadoLibre.com.pe? 👋\n\n¿Qué deseas hacer?"
    seleccion = pick(opciones, titulo)
    
    if seleccion[0] == "Extraer productos":
        return True
    else:
        return False

# Función principal del programa
def main():
    while True:  # Bucle para ejecutar o salir
        if mostrar_menu():  # Preguntar al inicio qué hacer
            # Selección de categorías con Pick
            titulo = "📂 Selecciona las categorías para buscar productos (usa espacio para seleccionar):"
            opciones = list(categorias.keys())
            seleccionadas = pick(opciones, titulo, multiselect=True, min_selection_count=1, indicator="▶")

            # Obtener solo los nombres de las categorías seleccionadas
            categorias_seleccionadas = [opcion[0] for opcion in seleccionadas]

            print(f"Categorías seleccionadas: {categorias_seleccionadas}")

            # Inicialización del navegador
            driver = webdriver.Chrome(options=chrome_options)

            # Lista global para almacenar productos
            todos_los_productos = []

            # Recorre las categorías seleccionadas y extrae productos
            for categoria in categorias_seleccionadas:
                url = categorias[categoria]
                productos = extraer_productos(driver, url, categoria)
                todos_los_productos.extend(productos)  # Agregar a la lista global

            # Preguntar el nombre del archivo Excel
            nombre_archivo = input("\n¿Con qué nombre deseas guardar el archivo Excel? (sin extensión): ")
            nombre_archivo = f"{nombre_archivo}.xlsx"

            # Guardar los datos en un archivo Excel
            if todos_los_productos:
                df_productos = pd.DataFrame(todos_los_productos)
                df_productos.to_excel(nombre_archivo, index=False)
                print(f"\n📅 Datos guardados en '{nombre_archivo}'.")
            else:
                print("\n❌ No se encontraron productos para guardar.")

            # Cerrar el navegador
            driver.quit()
            print("\n🎉 ¡Proceso completado exitosamente! 🎉")

        else:
            print("\n🚶‍♂️ Saliendo del programa. ¡Hasta pronto!")
            break

# Ejecutar la función principal
if __name__ == "__main__":
    main()
