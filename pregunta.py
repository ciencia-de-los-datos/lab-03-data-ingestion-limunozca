"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""


    # #


    # # Inserte su código aquí

import re
import pandas as pd


#definimos la función que nos permitirá leer el archivo y convertirlo en un dataframe
def ingest_data():

#procesa cada linea utilizando el patrón de expresión regular y divide las lineas 
    patterns = r'(\d+)\s+(\d+)\s+([\d,]+\s%\s+)\s+(.*\s*)'
    data='clusters_report.txt'
    with open(data, 'r') as f:
        bd = f.read()
    lines = bd.split('\n')

#iteramos sobre cada linea de la lista
    index_num=[]  #almacena los indices de las lineas que contienen números
    for i,element in enumerate(lines): # iteramos sobre cada linea de la lista, devuelve el indice como el elemento 
        if any(caracter.isdigit() for caracter in element): # itera sobre cada carácter en la línea element y verifica si ese carácter es un dígito utilizando el método isdigit()
            index_num.append(i) # si la línea actual contiene al menos un dígito, el índice i de esa línea se agrega a la lista index_num utilizando el método append().

    list_concat=[]    #almacena las lineas concatenadas
    for a,b in zip(index_num, index_num[1:]+[100]): # hay 2 listas y zip combina los 2 iterables
        list_concat.append(' '.join(lines[a:b])) #  une todas las líneas de texto en esa lista en una sola cadena, separando cada línea por un espacio en blanco.

    info=[]  #almacenará las coincidencias encontradas
    for i in (list_concat):
        info.append(re.findall(patterns, i))  # busca todas las coincidencias de la expresión regular patterns dentro de esa cadena y las almacena en la lista info.
    data1=[list(cont[0]) for cont in  info]
    for cont in range(len(data1)):
        data1[cont][3]=re.sub('\s+', ' ', data1[cont][3]).strip()

    columns=lines[:2] #tomas las 2 primeras lineas
    name_columns=columns[0].split('  ')[:2]+columns[0].split('  ')[3:-2]
    name_columns[1]=name_columns[1]+' palabras clave'
    name_columns[2]=name_columns[2]+' palabras clave'
    name_columns=[i.lower().strip().replace(' ','_') for i in name_columns]  # contiene los nombres de la columnas normalizadas, en minúsculas y con guiones bajos en lugar de espacios.

    report=pd.DataFrame(data1,columns=name_columns)
    report['cluster']=report.cluster.astype('int')
    report['cantidad_de_palabras_clave']=report.cantidad_de_palabras_clave.astype('int')
    report['porcentaje_de_palabras_clave']=report['porcentaje_de_palabras_clave'].str.replace('%', '').str.replace(',', '.').astype(float)
    report['principales_palabras_clave']=report['principales_palabras_clave'].astype(str).str.replace('.','')

    return report

    







    # #
