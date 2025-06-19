#Importar librerías necesarias, en este caso pandas
import pandas as pd
#----------------------------------------------------------------------------------------
#Normaliza nombres de columnas: minúsculas, sin espacios ni acentos 
def cargar_datos_excel(ruta_excel: str, sheet_name=0) -> pd.DataFrame:
    """Carga una hoja de un archivo Excel"""
    return pd.read_excel(ruta_excel, sheet_name=sheet_name)
# ----------------------------------------------------------------------------------------
def estandarizar_columnas(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
    )
    return df

# ----------------------------------------------------------------------------------------
def estandarizar_hojas(ruta_excel: str) -> dict:
    """Carga y estandariza las tres hojas clave del Excel"""
    ventas_df = pd.read_excel(ruta_excel, sheet_name="Ventas Supermercado")
    regiones_df = pd.read_excel(ruta_excel, sheet_name="Regiones")
    productos_df = pd.read_excel(ruta_excel, sheet_name="Productos")

    ventas_df = estandarizar_columnas(ventas_df)
    regiones_df = estandarizar_columnas(regiones_df)
    productos_df = estandarizar_columnas(productos_df)

    return {
        "ventas": ventas_df,
        "regiones": regiones_df,
        "productos": productos_df,
    }

#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
#Crea columnas de fechas unificadas si existen día, mes, año separados

def convertir_fechas(df: pd.DataFrame) -> pd.DataFrame:
    
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


