import os
import re
from typing import List, Optional
import pandas as pd


# ---------- Utilidades ----------

def leer_csv(ruta_csv):
    try:
        # Leer el archivo CSV
        df = pd.read_csv(ruta_csv)

        print("Columnas detectadas en el archivo:")
        print(df.columns.tolist())

        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_csv}")
        raise
    except Exception as e:
        print(f"Ocurrió un error durante la lectura del archivo: {e}")
        raise



def sanitize(name: str) -> str:
    """Convierte un nombre de columna en un nombre de archivo seguro."""
    return re.sub(r"[^a-zA-Z0-9_-]+", "_", name).strip("_")


def ensure_outdir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def select_numeric(df: pd.DataFrame, columns: Optional[List[str]]) -> pd.DataFrame:
    """Filtra columnas numéricas; si 'columns' se da, valida y filtra esas."""
    if columns:
        missing = [c for c in columns if c not in df.columns]
        if missing:
            raise ValueError(f"Columnas no encontradas en el CSV: {missing}")
        df = df[columns]
    # solo numéricas
    df_num = df.select_dtypes(include="number")
    if df_num.empty:
        raise ValueError("No hay columnas numéricas para graficar.")
    return df_num


