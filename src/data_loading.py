import pandas as pd
from pathlib import Path

def cargar_datos_excel(ruta_archivo: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Carga un archivo Excel desde una ruta.
    
    Args:
        ruta_archivo (str): Ruta al archivo .xlsx
        sheet_name (str, opcional): Nombre de la hoja. Si None, carga la primera hoja.

    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    try:
        df = pd.read_excel(ruta_archivo, sheet_name=sheet_name)
        return df
    except Exception as e:
        raise RuntimeError(f"Error al cargar el archivo: {e}")

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

def guardar_procesado(df: pd.DataFrame, nombre_archivo: str) -> None:
    """
    Guarda el DataFrame procesado en data/processed/.
    
    Args:
        df (pd.DataFrame): DataFrame a guardar
        nombre_archivo (str): nombre del archivo de salida .csv
    """
    ruta_salida = Path("data/processed") / nombre_archivo
    df.to_csv(ruta_salida, index=False)
