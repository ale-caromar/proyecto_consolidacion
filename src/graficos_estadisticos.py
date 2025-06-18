import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras_rentabilidad(resumen, columna='utilidad', top_n=10):
    """
    Gráfico de barras de la rentabilidad (utilidad) por producto.
    """
    top = resumen.sort_values(columna, ascending=False).head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top, x='id_producto', y=columna, palette='viridis')
    plt.title(f'Top {top_n} productos por {columna}')
    plt.xlabel('ID Producto')
    plt.ylabel(columna.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_linea_ventas(df, fecha_col='fecha_salida', ventas_col='ventas'):
    """
    Gráfico de línea de ventas a lo largo del tiempo.
    """
    df_fechas = df.dropna(subset=[fecha_col])
    df_fechas = df_fechas.groupby(fecha_col)[ventas_col].sum().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_fechas, x=fecha_col, y=ventas_col)
    plt.title('Ventas a lo largo del tiempo')
    plt.xlabel('Fecha')
    plt.ylabel('Ventas')
    plt.tight_layout()
    plt.show()

def boxplot_margen(resumen):
    """
    Boxplot del margen por producto.
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=resumen, y='margen')
    plt.title('Distribución del margen por producto')
    plt.ylabel('Margen')
    plt.tight_layout()
    plt.show()