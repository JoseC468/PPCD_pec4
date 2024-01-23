"""Creación de las funciones para el análisis gráfico"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def graph_bar(data: pd.DataFrame, path_save_fig: str=None, col: str = '#2CD5D5'):
    """
    Crea un gráfico de barras y, opcionalmente, lo guarda en una ruta específica.

    Parameters:
    - data (pd.DataFrame): El conjunto de datos que nos permitirá realizar el gráfico.
    - path_save_fig (str): Ruta donde se guardará el gráfico. Si es None, el gráfico 
        se mostrará en lugar de guardarse.
    - col: Indica el color del gráfico.

    Returns: No hay un valor que se retorna
    """
    # Creamos una serie que contiene la producción de series, por año de paso a producción
    year_num_serie: pd.Series=data[['first_air_date',
                                    'name']]['first_air_date'].dt.year.value_counts().sort_index()

    # Construcción del gráfico de barras
    plt.bar(year_num_serie.index, year_num_serie.values, color= col)
    plt.xlabel('Año de lanzamiento')
    plt.ylabel('Número de Series')
    plt.title('Número de Series por Año de lanzamiento')

    # Guardar el gráfico en la ruta especificada (si se proporciona)
    if path_save_fig is not None:
        path_save_graph = path_save_fig + r'\P4_1_graph_bar.png'
        print(f'P.4.1. Gráfico de barras almacenado en \n {path_save_graph}')
        plt.savefig(path_save_graph)
    else:
        plt.show()


def graph_line(data: pd.DataFrame, path_save_fig: str=None):
    """
    Crea un gráfico de líneas y se añade la opción de almacenado en ruta específica.

    Parameters:
    - data (pd.DataFrame): El conjunto de datos que nos permitirá realizar el gráfico.
    - path_save_fig (str): Ruta donde se guardará el gráfico. Si es None, el gráfico 
        se mostrará en lugar de guardarse.

    Returns: No hay un valor que se retorna
    """
    # Generamos las decadas a partir del 1940
    data['decada'] = pd.cut(data['first_air_date'].dt.year,
                            bins=range(1940, int(data['first_air_date'].dt.year.max()), 10),
                            right=False)

    # Contar el número de series por categoría de 'type' y por década
    serie_count_dec = data.groupby(['decada', 'type'], observed=False).size().unstack()

    # Crear el gráfico de líneas
    serie_count_dec.plot(kind='line', marker='o', figsize=(10, 6))
    plt.xlabel('Década')
    plt.ylabel('Número de Series')
    plt.title('Número de Series por Categoría y Década')
    plt.legend(title='Categoría')

    # Guardar el gráfico en la ruta especificada (si se proporciona)
    if path_save_fig is not None:
        path_save_graph = path_save_fig + r'\P4_2_graph_line.png'
        print(f'P.4.2. Gráfico de líneas almacenado en \n {path_save_graph}')
        plt.savefig(path_save_graph)
    else:
        plt.show()

def graph_circle(data: pd.DataFrame, path_save_fig: str=None, col: str = "pastel"):
    """
    Crea un gráfico circular y se añade la opción de almacenado en ruta específica.

    Parameters:
    - data (pd.DataFrame): El conjunto de datos que nos permitirá realizar el gráfico.
    - path_save_fig (str): Ruta donde se guardará el gráfico. Si es None, el gráfico 
        se mostrará en lugar de guardarse.
    - col (str): Indica el conjunto de colores del gráfico. 

    Returns: No hay un valor que se retorna
    """
    # Eliminar las filas con 'genres' vacío
    df_genres_not_null: pd.DataFrame = data.dropna(subset=['genres']).reset_index(drop=True)

    # Generamos una lista que contendra los géneros de una película por aparte
    df_genres_not_null['genres_sep'] = df_genres_not_null['genres'].apply(lambda x: x.split(', '))

    # Creamos una lista con todos los géneros
    all_genres: list = [genre for genres_list
                        in df_genres_not_null['genres_sep'] for genre in genres_list]

    # Conbilizamos el número de series por género
    count_series_genero: pd.Series = pd.Series(all_genres).value_counts()

    # Calcular el porcentaje respecto al total
    prop_genero = count_series_genero / len(all_genres) * 100

    # Filtrar los valores menores de 10 y sumarlos
    prop_men_10 = prop_genero[prop_genero < 1]
    sum_prop_men_10 = prop_men_10.sum()

    # Crear una nueva serie con los valores actualizados
    new_prop_genero = prop_genero[prop_genero >= 1]
    new_prop_genero['Otros'] = sum_prop_men_10

    # Crear el gráfico circular con ajustes de letra, leyenda y orientación

    plt.figure(figsize=(8, 8))
    colors = sns.color_palette(col)
    plt.pie(new_prop_genero, labels=new_prop_genero.index, autopct='%1.1f%%', colors = colors,
            textprops={'fontsize': 10}, counterclock=True, startangle=90,  rotatelabels=True)
    plt.title('Porcentaje de Series por Género', loc = 'left')

    # Guardar el gráfico en la ruta especificada (si se proporciona)
    if path_save_fig is not None:
        path_save_graph = path_save_fig + r'\P4_3_graph_circle.png'
        print(f'P.4.3. Gráfico circular almacenado en \n {path_save_graph}')
        plt.savefig(path_save_graph)
    else:
        plt.show()
