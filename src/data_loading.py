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

