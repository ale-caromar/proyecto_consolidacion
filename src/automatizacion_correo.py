import pandas as pd
import unicodedata
archivo = "../data/Sales report completa.xlsx"
df = pd.read_excel(archivo, sheet_name="Ventas Supermercado")

def normalizar_columna (nombre):
    nombre = unicodedata.normalize('NFKD', nombre) .encode('ascii', 'ignore').decode('ASCII' , "ignore")
    nombre = nombre.lower() .replace(" ", "_") .replace("-", "_") .replace(".", "_")
    return nombre

df.columns = [normalizar_columna(col) for col in df.columns]

print("Columnas normalizadas:")
print(df.columns.tolist())
