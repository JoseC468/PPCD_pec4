"""Generación de funciones para descomprimir archivos .zip y tar.gz"""

import os
import zipfile
import tarfile

def decompress_file(path_file: str, path_destination: str = None):
    """
    Función para descomprimir un archivo que se encuentra en formato zip o tar.gz.

    Parameters:
    - path_file (str): La ruta donde se encuentra el archivo a descomprimir.
    - path_destination (str): La ruta del directorio donde se descomprimirán los 
        archivos, en caso contrario, se usará el directorio actual.

    Returns: En este caso no hay un valor de retorno, pero se devolverá un mensaje que 
        indica la ruta donde se descomprimió el archivo.
    """
    if path_destination is None:
        path_destination = os.path.splitext(path_file)[0]

    extension = os.path.splitext(path_file)[1]

    if extension == '.zip':
        with zipfile.ZipFile(path_file, 'r') as zp:
            zp.extractall(path_destination)
        print('P1.1. Se descomprimio el archivo .zip con éxito, el archivo esta ubicado en:\n',path_destination)
    elif extension == '.tar.gz':
        with tarfile.open(path_file, 'r:gz') as tar_gz:
            tar_gz.extractall(path_destination)
        print('P1.1. Se descomprimio el archivo .tar.gz con éxito, el archivo esta ubicado en:\n',path_destination)
    else:
        raise ValueError("Tipo de archivo no compatible. Solo se descomprime archivos '.zip' o '.tar.gz'.")
