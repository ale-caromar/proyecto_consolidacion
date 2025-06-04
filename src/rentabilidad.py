import pandas as pd

def calcular_rentabilidad(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula métricas de rentabilidad a partir de columnas existentes.
    Asume que 'ventas' es el total de venta y 'utilidad' ya está incluida.
    """ 
    df = df.copy()
    
    # Asegurarse de que ventas y utilidad sean numéricas
    df['ventas'] = pd.to_numeric(df['ventas'], errors='coerce')
    df['utilidad'] = pd.to_numeric(df['utilidad'], errors='coerce')
    
    # Calcular margen: utilidad / ventas
    df['margen'] = df['utilidad'] / df['ventas']
    
    # Renombrar columnas para mantener consistencia
    df['total_venta'] = df['ventas']
    df['total_costo'] = df['total_venta'] - df['utilidad']
    
    return df # Redondear columnas para presentación
    resumen = resumen.round({
        'total_venta': 2,
        'total_costo': 2,
        'utilidad': 2,
        'margen': 4
    })


def resumen_rentabilidad(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resume la rentabilidad agrupando por id_producto.
    """
    columnas_necesarias = ['id_producto', 'total_venta', 'total_costo', 'utilidad', 'margen']
    for col in columnas_necesarias:
        if col not in df.columns:
            raise ValueError(f"Falta la columna requerida: {col}")
    
    resumen = df.groupby('id_producto').agg({
        'total_venta': 'sum',
        'total_costo': 'sum',
        'utilidad': 'sum',
        'margen': 'mean'
    }).reset_index()
    
     # Redondear columnas para presentación
    resumen = resumen.round({
        'total_venta': 2,
        'total_costo': 2,
        'utilidad': 2,
        'margen': 4
    })
    
    return resumen
