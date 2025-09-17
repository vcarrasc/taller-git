import pandas as pd

def estadisticas(df: pd.DataFrame):
    # Seleccionar solo columnas numéricas
    df_numericas = df.select_dtypes(include=['number'])

    if df_numericas.empty:
        raise ValueError('No numeric columns found in the dataset')

    print("\nEstadísticas básicas de las columnas numéricas:\n")
    print(df_numericas.describe().transpose())
    print("\nEstadísticas de valores faltantes:\n")
    print(df.isna().sum())

    return df_numericas
