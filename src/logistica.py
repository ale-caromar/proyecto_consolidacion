import pandas as pd

def calcular_tiempo_entrega(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el tiempo de entrega si no está presente, usando las fechas.
    """
    df = df.copy()
    if 'tiempo_entrega' not in df.columns or df['tiempo_entrega'].isnull().any():
        df['tiempo_entrega'] = (df['fecha_entrega'] - df['fecha_salida']).dt.days
    return df

def resumen_logistica(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea un resumen de logística por producto.
    Incluye tiempos de entrega y costos de envío.
    """
    columnas_requeridas = ['id_producto', 'costo_envio', 'tiempo_entrega']
    for col in columnas_requeridas:
        if col not in df.columns:
            raise ValueError(f"Falta la columna requerida: {col}")
    
    resumen = df.groupby('id_producto').agg({
        'costo_envio': ['sum', 'mean'],
        'tiempo_entrega': ['mean', 'max', 'min']
    })
    
    resumen.columns = ['_'.join(col).strip() for col in resumen.columns.values]
    resumen = resumen.reset_index()
    return resumen

def entregas_fuera_de_rango(df: pd.DataFrame, dias_max: int = 5) -> pd.DataFrame:
    """
    Filtra las entregas cuyo tiempo de entrega excede un valor máximo aceptable.
    """
    df = df.copy()
    df_lentas = df[df['tiempo_entrega'] > dias_max]
    return df_lentas

def eficiencia_entregas(df: pd.DataFrame) -> float:
    """
    Calcula el porcentaje de entregas dentro del rango esperado (<= 5 días por defecto).
    """
    total = len(df)
    dentro_del_plazo = len(df[df['tiempo_entrega'] <= 5])
    return round((dentro_del_plazo / total) * 100, 2) if total > 0 else 0.0
