import os
from estadisticas import analizar_csv
if __name__ == "__main__":
    archivo = input("Introduce la ruta del archivo CSV: ")
    # Validar la ruta del archivo
    if not os.path.isfile(archivo):
        print("Error: El archivo especificado no existe o no es un archivo válido.")
    else:
        analizar_csv(archivo)