import pandas as pd

def estandarizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normaliza nombres de columnas: minúsculas, sin espacios ni acentos.
    
    Args:
        df (pd.DataFrame): DataFrame original
    
    Returns:
        pd.DataFrame: DataFrame con columnas normalizadas
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )
    return df

def convertir_fechas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea columnas de fechas unificadas si existen día, mes, año separados.
    
    Returns:
        pd.DataFrame con columnas 'fecha_salida' y 'fecha_entrega' si aplica.
    """
    for col in ['ano_salida', 'mes_salida', 'dia_salida', 'ano_entrega', 'mes_entrega', 'dia_entrega']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')
    
    if {'ano_salida', 'mes_salida', 'dia_salida'}.issubset(df.columns):
        df['fecha_salida'] = pd.to_datetime(
            df[['ano_salida', 'mes_salida', 'dia_salida']]
            .rename(columns={'ano_salida': 'year', 'mes_salida': 'month', 'dia_salida': 'day'}),
            errors='coerce'
        )
    if {'ano_entrega', 'mes_entrega', 'dia_entrega'}.issubset(df.columns):
        df['fecha_entrega'] = pd.to_datetime(
            df[['ano_entrega', 'mes_entrega', 'dia_entrega']]
            .rename(columns={'ano_entrega': 'year', 'mes_entrega': 'month', 'dia_entrega': 'day'}),
            errors='coerce'
        )
    return df


