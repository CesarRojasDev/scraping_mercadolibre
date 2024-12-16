# **Scraping MercadoLibre**

Script de consola para realizar *scraping* de datos de la web de **MercadoLibre** y exportarlos en un archivo Excel.

---

## **Requisitos**

Antes de ejecutar el script, asegúrate de contar con los siguientes requisitos:  
- **Google Chrome** (última versión recomendada).  
- **Python 3.10** o superior.  
- Librerías de Python:  
  - Selenium  
  - Pandas  
  - Openpyxl  
  - Pick  
  - Pyinstaller  

---

## **Instalación de dependencias**

Instala todas las dependencias necesarias ejecutando el siguiente comando en la terminal:

```bash
pip install selenium pandas pyinstaller openpyxl pick
```

## Uso 

Ejecutar el script con Python
```bash
python scraping_mercadolibre.py
```
 
 Pasos para realizar scraping:
 1. Selecionar entre las opciones [Extraer productos, Salir]
 2. Seleccionar las categorías a extraer(usa espacio para seleccionar)
 3. Escribir el nombre del archivo de salida
 
 
## Crear un ejecutable

Para ejecutar el script en modo de consola, ejecutar el siguiente comando:
```bash
python  pyinstaller scraping_mercadolibre.py
```

Esto creará un archivo ejecutable llamado `scraping_mercadolibre.exe` en la carpeta `dist`.
