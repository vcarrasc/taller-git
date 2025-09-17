from typing import List, Optional, Tuple, Dict, Any
import pandas as pd

def preprocesar_df(df: pd.DataFrame, strategy_num: str = "mean") -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Preprocesa el DataFrame:
      - Numéricos: rellena NaN con mean o median
      - Categóricos: rellena NaN con mode

    Parámetros:
      df : DataFrame original
      strategy_num : "mean" o "median" (para columnas numéricas)

    Devuelve:
      df_limpio : DataFrame procesado
      reporte : diccionario con detalles
    """
    df = df.copy()
    reporte: Dict[str, Any] = {"filled_numeric": {}, "filled_categorical": {}}

    # --- Numéricas ---
    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        n_missing = df[col].isna().sum()
        if n_missing > 0:
            if strategy_num == "median":
                val = df[col].median()
            else:
                val = df[col].mean()
            df[col] = df[col].fillna(val)
            reporte["filled_numeric"][col] = {"missing": int(n_missing), "value_used": float(val)}

    # --- Categóricas ---
    cat_cols = df.select_dtypes(exclude="number").columns
    for col in cat_cols:
        n_missing = df[col].isna().sum()
        if n_missing > 0:
            mode_val = df[col].mode(dropna=True)
            val = mode_val.iloc[0] if not mode_val.empty else "Unknown"
            df[col] = df[col].fillna(val)
            reporte["filled_categorical"][col] = {"missing": int(n_missing), "value_used": str(val)}

    return df, reporte