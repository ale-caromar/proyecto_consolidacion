def exportar_excel(df, ruta_salida):
    df.to_excel(ruta_salida, index=False)
