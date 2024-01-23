"""Generación de funciones para la integración de data"""

import os
import time
import csv
import pandas as pd


# Pregunta 1.2
def integrated_dataframe(path_file: str):
    """
    Integra varios archivos CSV ubicados en una carpeta y los integra en 
    un único DataFrame.

    Parameters:
    - path_file: Ruta de la carpeta que contiene los archivos CSV.

    Returns:
    - df_final: DataFrame resultante de la integración.
    """
    # Medimos el tiempo de ejecución
    start = time.time()

    # Capturamos la lista de nombres de los archivos CSV en el directorio
    list_csv: list = [j for j in os.listdir(path_file) if j.endswith('.csv')]

    # Creamos el dataframe vacio
    df_final = pd.DataFrame()

    # Leemos cada archivo CSV y lo integramos
    for i in list_csv:
        route_file = os.path.join(path_file, i)
        df_temporal: pd.DataFrame = pd.read_csv(route_file)
        df_final: pd.DataFrame = pd.concat([df_final, df_temporal], axis = 1)

    # Calculamos el tiempo de ejeción
    finish = time.time()
    time_process = finish - start
    print(f"P.1.2. Tiempo de procesamiento en la integración en un DataFrame: {round(time_process,3)} segundos")
    return df_final


# Pregunta 1.3
def integrated_dictionary(path_file: str):
    """
    Integra varios archivos CSV ubicados en una carpeta y almacenarlos 
    en un único diccionario usando el 'ID' como clave.

    Parameters:
    - path_file: Ruta de la carpeta que contiene los archivos CSV.

    Returns:
    - dict: Diccionario integrado con "id" como clave.
    """
    # Medimos el tiempo de ejecución
    start = time.time()

    # Generamos un diccionario vacio
    integrate_dict = {}

    # Obtener la lista de archivos CSV en la carpeta
    file_csv: list = [file for file in os.listdir(path_file) if file.endswith(".csv")]

    for i in file_csv:
        directory = os.path.join(path_file, i)
        with open(directory, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id_valor = row.get('id')
                if id_valor is not None:
                    integrate_dict[id_valor] = row
    # Calculamos el tiempo de ejeción
    finish = time.time()
    time_process = finish - start
    print(f"P.1.3. Tiempo de procesamiento en la integración en un diccionario: {round(time_process,3)} segundos")
    return integrate_dict
