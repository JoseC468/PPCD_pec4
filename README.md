# PEC4 - Programación para la ciencia de datos - Aula 3

Para esta PEC4 fue necesario poder revisar mucha documentación relacionada con clean code y la organización modular de funciones en archivos planos con extensión .py. Es así que a lo largo de está última PEC4 traté de aplicar lo principios de clean code y he estructurado mis funciones de manera modular en archivos .py, culminando en un programa ejecutable desde un archivo main.py. Es así que en este proceso de aprendizaje, he abordado no solo la sintaxis y las capacidades fundamentales de Python, sino también la importancia un código claro, eficiente y que facilité su mantenimiento a través del tiempo. 

Por este motivo, la organización de funciones en archivos .py ha sido una estrategia clave que he adoptado para mejorar la estructura de los resultados de la PEC4. Cada función cumple un propósito específico y se almacena en un archivo individual, lo que no solo facilita la comprensión del código, sino que también permite una gestión más eficiente y colaborativa. Es así que procedo a detallar y explicar el funcionamiento de los archivos .py y su procedimiento para una correcta ejecución. 

En una primera instancia es necesario crear una máquina virtual o como en mi caso trabajar con un entorno virtual creado en mi ordenador. Comencemos!!

1. Crear un entorno virtual, puedes usar el siguiente comando en el terminal: python3 -m venv name_venv (name_venv: define el nombre de tu proyecto, en nuestro caso lo llamaremos pec4_sol)
2. Luego seguiremos con la activación del entorno virtual: pec4_sol\Scripts\activate.bat

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
![venv sin los archivos de ejecución](https://github.com/JoseC468/PPCD_pec4/blob/main/venv-sin-archivos.png)

- Posterior a descomprimir el archivo .zip y copiar los archivos mencionados en el entorno virtual resulta lo siguiente.
![venv con los archivos de ejecución](https://github.com/JoseC468/PPCD_pec4/blob/main/venv-con-archivos.png)

A continuación, pasaremos a instalar los paquetes necesarios para ejecutar sin problemas nuestro archivos .py. Para ello, podemos ejecutar en el terminal (Command Prompt) la siguiente sentencia "pip3 install -r requirements.txt". Este proceso de instalación de paquetes tarda a lo más 2 minutos.

El último procedimiento es realizar una modificación en el archivo main.py (<span style="color:red">OBLIGATORIO</span>). Es necesario cambiar la ruta de salida, ya que, de lo contrario se almacenará en otro archivo o producirá un error de ejecución. Para poder modificar la ruta de salida describiremos cada ruta y que es lo que almacena. Para ello, tenemos 4 rutas de salida:
PATH_ARCHIVE: Esta ruta indica donde está ubicado el archivo a descompirmir ("TMDB.zip"), su ruta en el entorno virtual esta ubicado en la carpeta "zip" o "tar.gz.". 
PATH_DECOMPRESS: Esta ruta indica la carpeta donde se descomprimirá el archivo ".zip" o "tar.gz.". En el entorno virtual es ta ubicado en la carpeta "zip\unzip".
PATH_DATA: Esta ruta no permite almacenar el dataframe que integra los dataset que fueron descomprimidos del archivos "TMDB.zip". En el entorno virtual es ta ubicado en la carpeta "data".
PATH_SAVE_GRAPH: Esta ruta nos permite almacenar los gráficos generados en el apartado del análisis. En el entorno virtual es ta ubicado en la carpeta "graph".




