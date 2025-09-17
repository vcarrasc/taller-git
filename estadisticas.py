import pandas as pd

def analizar_csv(ruta_csv):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(ruta_csv)

        print("Columnas detectadas en el archivo:")
        print(df.columns.tolist())

        # Seleccionar solo columnas numéricas
        df_numericas = df.select_dtypes(include=['number'])

        if df_numericas.empty:
            print("\nNo se encontraron columnas numéricas en el archivo.")
            return

        print("\nEstadísticas básicas de las columnas numéricas:\n")
        print(df_numericas.describe().transpose())

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_csv}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


