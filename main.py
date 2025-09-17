import os
from estadisticas import estadisticas
from utils import select_numeric, leer_csv
from plots import (
    plot_histograms,
    plot_boxplots,
    plot_scatter_matrix,)

if __name__ == "__main__":
    archivo = input("Introduce la ruta del archivo CSV: ")
    # Validar la ruta del archivo
    if not os.path.isfile(archivo):
        print("Error: El archivo especificado no existe o no es un archivo válido.")
        exit(1)

    df = leer_csv(archivo)
    df_numericas = estadisticas(df)

    # 2) Usar el DataFrame ya generado (se pasa entre funciones; no se relee)
    df_num = select_numeric(df, df_numericas.columns.tolist())

    # 3) Generar gráficas
    plot_histograms(df_num, ".", bins=30, show=True)
    plot_boxplots(df_num, ".", show=True)
    plot_scatter_matrix(df_num, ".", show=True)

    print(f"✅ Gráficas guardadas en el actual directorio.")