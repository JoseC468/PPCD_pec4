"""Funciones que realizan proceso de filtrado en la data"""

import pandas as pd

def filter1_overview(data: pd.DataFrame):
    """
    Esta función retorna una lista de nombres de las series cuyo idioma original 
    (original_language) sea el inglés y en cuyo resumen (overview) aparezcan las 
    palabras “mystery” o “crime”, sin tener en cuenta mayúsculas ni minúsculas.

    Parameters:
    - data (pd.DataFrame): El conjunto de datos

    Returns:
    - name_serie (list): Retorna la lista de nombres que cumple con la condición
    """
    # Creamos un nuevo dataframe con los filtros
    df_filter = data[(data['original_language'] == 'en') &
                     (data['overview'].notna()) &
                     (data['overview'].str.lower().str.contains('mystery|crime'))]

    # Almacenamos en una lista el nombre de las series
    name_serie: list = df_filter['name'].tolist()

    # Imprimir los nombres de las series
    print("P.3.1. Tenemos", len(name_serie),
          "series y películas que cumplen con las condiciones mencionadas. Agunos de ellos son:",
          df_filter['name'].values)

    return name_serie

def filter2_status(data: pd.DataFrame):
    """
    Esta función devuelve la lista de series que han empezado en 2023 y han sido canceladas.
    
    Parameters:
    - data (pd.DataFrame): El conjunto de datos

    Returns:
    - name_serie (list): Retorna la lista de nombres que cumple con la condición
    """
    # Generamos un dataset de las series y peliculas canceladas en el 2023
    df_series_canceled_23 = data[(data['first_air_date'].dt.year == 2023) &
                                 (data['status'] == 'Canceled')]

    # Capturamos las primeras 20 series y películas
    view_20_name = df_series_canceled_23['name'].head(20).tolist()

    # Imprimir los nombres de las series
    print("P.3.2. Tenemos", len(df_series_canceled_23['name']),
        "series y películas que fueron canceladas en el 2023. Los 20 primeros son:",
        view_20_name)

    return view_20_name

def filter3_languaje(data: pd.DataFrame):
    """
    Esta función devuelve la lista de series que han empezado en 2023 y han sido canceladas.
    
    Parameters:
    - data (pd.DataFrame): El conjunto de datos

    Returns:
    - name_serie (list): Retorna la lista de nombres que cumple con la condición
    """
    # Generamos el filtro del lenguaje
    df_languaje_jap = data[data['languages'] == 'ja' ][['name', 'original_name',
                                                        'networks', 'production_companies']]

    # Mostramos los 20 primeros registros
    print('P.3.3. Los 20 primeros registros.')
    print(df_languaje_jap.head(20))

    return df_languaje_jap
