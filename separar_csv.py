import pandas as pd
import math
import sys
import os

def dividir_csv_en_partes(nombre_archivo, num_partes):
    if not os.path.isfile(nombre_archivo):
        print(f"Error: el archivo '{nombre_archivo}' no existe.")
        return

    try:
        num_partes = int(num_partes)
        if num_partes < 1:
            raise ValueError
    except ValueError:
        print("Error: el número de partes debe ser un entero mayor o igual a 1.")
        return

    df = pd.read_csv(nombre_archivo)
    total_filas = len(df)
    filas_por_parte = math.ceil(total_filas / num_partes)
    base_nombre = os.path.splitext(nombre_archivo)[0]
    for i in range(num_partes):
        inicio = i * filas_por_parte
        fin = inicio + filas_por_parte
        parte = df.iloc[inicio:fin]
        salida = f"{base_nombre}_parte_{i+1}.csv"
        parte.to_csv(salida, index=False)
        print(f"[✔] Guardado: {salida}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python dividir_csv.py <archivo.csv> <numero_de_partes>")
    else:
        _, archivo, partes = sys.argv
        dividir_csv_en_partes(archivo, partes)