"""Fase de preprocesamiento"""

import pandas as pd

## Ejercicio 2.1.

def calculate_days(data: pd.DataFrame, feature_date_start: str, feature_date_fin:str,
                   name_new_var: str ='air_days'):
    """
    Crear una nueva variable e introducirlo en dataframe, esta variable registra el número 
    de días que una serie estuvo en emisión.

    Parameters:
    - data (pd.DataFrame): DataFrame que contiene los datos integrados.
    - feature_date_start (str): Es la fecha de emisión.
    - feature_date_fin (str): Es la última fecha de emisión.
    - name_new_var (str): El nombre de la nueva variable.
    
    Returns:
    - data (pd.DataFrame): Retorna el mismo DataFrame incluyendo la nueva variable.
    """
    # Transformamos el tipo de variables a formato fecha
    data[feature_date_start] = pd.to_datetime(data[feature_date_start], format = '%Y-%m-%d')
    data[feature_date_fin] = pd.to_datetime(data[feature_date_fin], format = '%Y-%m-%d')

    # Creamos la variable air_days
    data[name_new_var] = (data[feature_date_fin] - data[feature_date_start]).dt.days

    # Mostramos los 10 primeros registros que tienen más días en emisión
    print('P.2.1: Los 10 registros del dataset que más días han estado en emisión.')
    print(data.sort_values(by = name_new_var, ascending=False).head(10))

    return data

## Ejercicio 2.2.

def create_dict_ordered(data):
    """
    Crea un diccionario ordenado a partir de un DataFrame.

    Parameters:
    - data (pd.DataFrame): DataFrame que contiene las columnas 'name', 'homepage' y 'poster_path'.
    Returns:
    - dict: Diccionario ordenado con información de 'homepage' y 'poster_path' para cada serie.
    """
    dict_name = {}

    for _, row in data.iterrows():
        serie_name = row['name']
        homepage = row['homepage'] if not pd.isna(row['homepage']) and row['homepage'] != '' else 'NOT AVAILABLE'
        poster_path = row['poster_path'] if not pd.isna(row['poster_path']) and row['poster_path'] != '' else 'NOT AVAILABLE'

        dict_name[serie_name] = f"Homepage: {homepage}, Poster Path: {poster_path}"

    print('P.2.2: Los primeros 5 registros del diccionario.')
    # Mostrar los primeros 5 registros del diccionario
    for serie, info in list(dict_name.items())[:5]:
        print(f"{serie}: {info}")

    return dict_name
