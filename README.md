# PEC4 - Programación para la ciencia de datos - Aula 3
----------------------

Para esta PEC4 fue necesario poder revisar mucha documentación relacionada con clean code y la organización modular de funciones en archivos planos con extensión .py. Es así que a lo largo de está última PEC4 traté de aplicar lo principios de clean code y he estructurado mis funciones de manera modular en archivos .py, culminando en un programa ejecutable desde un archivo main.py. Es así que en este proceso de aprendizaje, he abordado no solo la sintaxis y las capacidades fundamentales de Python, sino también la importancia un código claro, eficiente y que facilité su mantenimiento a través del tiempo. 

Por este motivo, la organización de funciones en archivos .py ha sido una estrategia clave que he adoptado para mejorar la estructura de los resultados de la PEC4. Cada función cumple un propósito específico y se almacena en un archivo individual, lo que no solo facilita la comprensión del código, sino que también permite una gestión más eficiente y colaborativa. Es así que procedo a detallar y explicar el funcionamiento de los archivos .py y su procedimiento para una correcta ejecución. 

En una primera instancia es necesario crear una máquina virtual o como en mi caso trabajar con un entorno virtual creado en mi ordenador. Comencemos!!

1. Crear un entorno virtual, puedes usar el siguiente comando en el terminal: python3 -m venv name_venv (name_venv: define el nombre de tu proyecto, en nuestro caso lo llamaremos pec4_sol)
2. Luego seguiremos con la activación del entorno virtual: pec4_sol\Scripts\activate.bat
3. Finalmente, ingresaremos a trabajar en el entorno virtual ejecutando en el terminal el siguiente código: cd pec4_sol

Luego de tener crear y activar nuestro entorno virtual, en el caso de trabajar con Visual Studio Code es necesario ingresar directarmente al entorno virtual. Pero antes, debemos descomprimir el archivo que continene la solución de la PEC4 y llevar los siguientes archivos:

- archivo "data"
- archivo "graph"
- archivo "Modulos"
- archivo "process_image_execute"
- archivo "zip"
- archivo "LICENSE"
- archivo "main.py"
- archivo "README"
- archivo "requirements"

Adjunto unas imágenes explicando este proceso.

- Luego de crear el entorno virtual (venv) se puede ver que se muestra lo siguientes archivos.
![venv sin los archivos de ejecución](https://github.com/JoseC468/PPCD_pec4/blob/main/process_image_execute/venv-sin-archivos.png)

- Posterior a descomprimir el archivo .zip y copiar los archivos mencionados en el entorno virtual resulta lo siguiente.
![venv con los archivos de ejecución](https://github.com/JoseC468/PPCD_pec4/blob/main/process_image_execute/venv-con-archivos.png)

A continuación, pasaremos a instalar los paquetes necesarios para ejecutar sin problemas nuestro archivos .py. Para ello, podemos ejecutar en el terminal (Command Prompt) la siguiente sentencia "pip3 install -r requirements.txt". Este proceso de instalación de paquetes tarda a lo más 2 minutos.

El último procedimiento es realizar una modificación en el archivo main.py (<span style="color:red">**OBLIGATORIO**</span>). Es necesario cambiar la ruta de salida, ya que, de lo contrario se almacenará en otro archivo o producirá un error de ejecución. Para poder modificar la ruta de salida describiremos cada ruta y que es lo que almacena. Para ello, tenemos 4 rutas de salida:

* PATH_ARCHIVE: Esta ruta indica donde está ubicado el archivo a descompirmir ("TMDB.zip"), su ruta en el entorno virtual esta ubicado en la carpeta "zip" o "tar.gz.". 
* PATH_DECOMPRESS: Esta ruta indica la carpeta donde se descomprimirá el archivo ".zip" o "tar.gz.". En el entorno virtual es ta ubicado en la carpeta "zip\unzip".
* PATH_DATA: Esta ruta no permite almacenar el dataframe que integra los dataset que fueron descomprimidos del archivos "TMDB.zip". En el entorno virtual es ta ubicado en la carpeta "data".
* PATH_SAVE_GRAPH: Esta ruta nos permite almacenar los gráficos generados en el apartado del análisis. En el entorno virtual es ta ubicado en la carpeta "graph".

Finalmente, luego de hacer la modificación de las rutas de salida, pasaremos a ejecutar en el terminal el sript "main.py" con la siguiente sentencia: "python3 main.py"

Esta ejecución mostrará los resultados obtenidos por cada apartado de la PEC4, indicando el número de pregunta y una corta descripción, como se muestra en la siguiente imagen. 

![Resultado de la ejecución del archivo main.py](https://github.com/JoseC468/PPCD_pec4/blob/main/process_image_execute/result_execute_main.png)

--------------------

Sin embargo, en el resultado de la ejecución del archivo "main.py" podemos que solo se muestra los resultados operacionales como filtrado, listas y gráficos, pero no hay comentarios finales. Esto comentarios que son necesarios por algunas preguntas y las conclusiones de la última pregunta serán realizados por este archivo "README". 

Pregunta 1.4: ¿Qué diferencias se observan en la lectura de los ficheros siguiendo ambos métodos? ¿Si los ficheros tuvieran un tamaño de 10GB qué método sería más rápido? Justificad la respuesta.

R: Con respecto a la diferencia en la lectura de ficheros se puede ver que en visualización y comprensión, es más factible los resultados birndados por la integración por dataframe, ya que, la vizualización en una tabla es más interpretable y comprensible a simple vista, además, se puede ver que para que este conjunto de datos la integración de datos fue más rápido por dataframe (1.705 seg.) que el diccionario (2.181 seg.). Sin embargo, de las clases anteriores podemos hablar sobre el consumo de memoria, la integración por dataframe tiende a consumir mayor memoria, en especial si los archivos son de 10GB, en cuanto a la integración por diccionario es más eficiente en está parte, ya que, a nivel de memoria el diccionario pesa menos que un dataframe. Por último, si el consumo de memoria es ilimitado, el siguiente paso para seleccionar la mejor opción es la parte operacional, si se requieren operaciones complejas sobre todo el conjunto de datos sería más adecuado usar la integración por DataFrame y si se necesita acceder a datos específicos rápidamente mediante el 'id', la integración por diccionario es más adecuado. 

Pregunta 4.1: Mostrad en un gráfico de barras el número de series por año de inicio.

R: De acuerdo al gráfico de barras, podemos ver que existe una tendecia creciente, de tipo exponencial en la producción de series. Esta tendencia se puede ver reflejada desde 1940 en adelante. Llegando a su pico más alto alrededor del 2020. 

Pregunta 4.2: Construid un gráfico de líneas que muestre el número de series de cada categoría de la variable “type” producidas en cada década desde 1940. ¿Qué cambios de tendencia se observan?.

R: Del siguiente gráfico se tiene que para todos las categorías de películas producidas desde la década de los 40, se tiene una tendencia creciente. Por otro lado, la categoría de 'Scripted' es la única que tiene una tendencia creciente de tipo exponencial, es decir, que desde la década de los 40, está categoría tuvo mayor impacto en los televidentes por lo que se tuvieron que crear más series de ese tipo. Asimismo, las miniseries tuvo impacto regular hasta la década del 2010, donde era la segunda categoría con mayor demanda, pero en la última década paso a la 4ta posición. 

Pregunta 4.3: Obtened el número de series por género y mostrad el porcentaje respecto al total en un gráfico circular. Los géneros que representen menos del 1% del total se incluirán en la categoría "Other". Tened en cuenta que una serie que tenga más de un género deberá incluirse en todas las categorías en que esté clasificada y que las series con el campo "genres" vacío no se incluyen.

R: De acuerdo al siguiente gráfico circular podemos ver que las categorías con mayor demanda son del tipo de Drama (22.7%), Comedy (15.7%) y Documentary (14.8%). Estás 3 categorías representa más del 50% del total de audiencias. 

Pregunta 5: Conclusiones.

Luego de la revisión de los resultados obtenidos a partir de los gráficos de barras, líneas y el gráfico circular, se pueden extraer conclusiones significativas sobre la evolución y preferencias en la producción de series a lo largo del tiempo.

En primer lugar, la representación gráfica del número de series por año de inicio revela una clara tendencia creciente, sugiriendo un aumento exponencial en la producción de series desde la década de 1940. Este fenómeno podría estar vinculado a una creciente demanda y popularidad del formato a lo largo de las décadas, culminando en un pico destacado alrededor del año 2020.

El análisis detallado de la producción por categoría, representado en el gráfico de líneas, destaca la categoría 'Scripted' como la de mayor impacto, mostrando una tendencia creciente de tipo exponencial. Asimismo, se observan cambios en la posición relativa de la categoría de miniseries, indicando fluctuaciones en su popularidad a lo largo del tiempo, particularmente en la última década.

En cuanto a la distribución por género, el gráfico circular revela que los géneros de Drama, Comedy y Documentary son los más demandados, representando conjuntamente más del 50% del total de audiencias. Este hallazgo subraya la preferencia generalizada por estos géneros entre los espectadores. La inclusión de géneros menos representativos en la categoría "Other" facilita la interpretación visual y resalta la predominancia de ciertos géneros.

En conclusión, los datos analizados reflejan una evolución positiva en la producción de series a lo largo del tiempo, con ciertos géneros y categorías destacando como líderes en popularidad. Estos hallazgos proporcionan insights valiosos para la toma de decisiones en la industria televisiva, permitiendo adaptar la oferta de contenido a las preferencias cambiantes de la audiencia.

--------------------

En este apartado para evaluar el rendimiento y la modularidad del código usaremos el paquete pylint. Este paquete nos permite evaluar la calidad del código y para evaluar la calidad de los archivos .py, es necesario ejecutar en el terminal el siguiente código:

- pylint main.py

Sin embargo, existe un error que complica la legibilidad del código y esto está relacionado con  la longitud máxima de línea en la ruta de salida para los archivos como PATH_ARCHIVE, PATH_DECOMPRESS, PATH_DATA y PATH_SAVE_GRAPH. Además, para no distorsionar la legibilidad del código usaremos la siguiente sentencia que acepta una línea máxima de 130 y no 100 (por defecto). Esta opción se aplica para todos los archivos planos generados.  

- pylint --max-line-length=130 main.py
- pylint --max-line-length=130 Modulos\analisis\descriptive.py
- pylint --max-line-length=130 Modulos\lectura\read_csv.py
- pylint --max-line-length=130 Modulos\lectura\unzip_file.py
- pylint --max-line-length=130 Modulos\limpieza\filtrado.py
- pylint --max-line-length=130 Modulos\preprocesamiento\processing.py

