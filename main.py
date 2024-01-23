"""Ejecución de funciones"""

# Carga de funciones
from Modulos.lectura.unzip_file import decompress_file
from Modulos.lectura.read_csv import integrated_dataframe, integrated_dictionary
from Modulos.preprocesamiento.processing import calculate_days, create_dict_ordered
from Modulos.limpieza.filtrado import filter1_overview, filter2_status, filter3_languaje
from Modulos.analisis.descriptive import graph_bar, graph_line, graph_circle

# Generamos la ruta de los archivos y la de destino
PATH_ARCHIVE = r'D:\Master UOC\Clases\2do semestre\Programación para la ciencia de datos\PEC4\PEC4_sol\VALIDACION\pec4_sol\zip\TMDB.zip'
PATH_DECOMPRESS = r'D:\Master UOC\Clases\2do semestre\Programación para la ciencia de datos\PEC4\PEC4_sol\VALIDACION\pec4_sol\zip\unzip'
PATH_DATA=r'D:\Master UOC\Clases\2do semestre\Programación para la ciencia de datos\PEC4\PEC4_sol\VALIDACION\pec4_sol\data'
PATH_SAVE_GRAPH = r'D:\Master UOC\Clases\2do semestre\Programación para la ciencia de datos\PEC4\PEC4_sol\VALIDACION\pec4_sol\graph'

# Ejercicio 1: Descomprensión y lectura de ficheros.
## Ejercicio 1.1
"""Implementad una función que descomprima ficheros en formato zip y tar.gz."""
decompress_file(path_file = PATH_ARCHIVE, path_destination = PATH_DECOMPRESS)

## Ejercicio 1.2.
df_integrated = integrated_dataframe(PATH_DECOMPRESS)

### Exportamos el dataset
df_integrated.to_csv(PATH_DATA + r'\df_integrated.csv', index=False)

## Ejercicio 1.3.
resultado_diccionario = integrated_dictionary(PATH_DECOMPRESS)

# Ejercicio 2: Descomprensión y lectura de ficheros.
## Ejercicio 2.1.
df_integrated_new = calculate_days(data = df_integrated, feature_date_start = 'first_air_date',
                                   feature_date_fin = 'last_air_date', name_new_var ='air_days')

## Ejercicio 2.2.
# Crear el diccionario ordenado
new_dict_oreder = create_dict_ordered(data = df_integrated_new)

# Ejercicio 3: Filtrado de datos.

## Ejercicio 3.1.
list_name_filter1 = filter1_overview(data = df_integrated_new)

## Ejercicio 3.2.
list_name_filter2 = filter2_status(data = df_integrated_new)

## Ejercicio 3.3.
df_filter3 = filter3_languaje(data = df_integrated_new)

# Ejercicio 4: Análisis gráfico.
## Ejercicio 4.1.
graph_bar(data = df_integrated_new, path_save_fig = PATH_SAVE_GRAPH, col = '#2CD5D5')

## Ejercicio 4.2.
graph_line(data = df_integrated_new, path_save_fig = PATH_SAVE_GRAPH)

## Ejercicio 4.3.
graph_circle(data=df_integrated_new, path_save_fig=PATH_SAVE_GRAPH, col='pastel')
