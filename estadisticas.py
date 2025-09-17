import pandas as pd

def estadisticas(df: pd.DataFrame):
    # Seleccionar solo columnas numéricas
    df_numericas = df.select_dtypes(include=['number'])

    if df_numericas.empty:
        print("\nNo se encontraron columnas numéricas en el archivo.")
        exit(1)

    print("\nEstadísticas básicas de las columnas numéricas:\n")
    print(df_numericas.describe().transpose())

    return df_numericas


