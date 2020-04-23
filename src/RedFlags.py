# -*- coding: utf-8 -*-


import pandas as pd
import json
import io
from pandas.io.json import json_normalize
import pymongo
from pymongo import MongoClient
import pprint
import flatten_json
import numpy as np


#Lector de Json.
with open("contratacionesDirectas2018.json","r",encoding="utf-8") as file:
    data=json.load(file)

# FUNCIONES DE EXTRACCIÓN.
def sacarTotal(s):
    for s in data:
        return s['total']

def leer(s):
    return s['buyer']['name']

z=0
y = []
for i in data:
    y.append(data[z]["total"])
    z=z+1

ocid=[]
z=0
for i in data:
    ocid.append(data[z]["ocid"])
    z=z+1

contracts=[]
z=0
for i in data:
    contracts.append(data[z]["contracts"][0]["title"])
    z=z+1

x = []
for i in data:
    x.append(leer(i))


#Creación del marco de datos
X = pd.DataFrame(x)

#Columnas del marco de datos
X["monto real"]=y
X['monto promedio(estandar 2018)'] = 346500
X["Ocid"]=ocid
X["Contracts"]=contracts
X["monto minimo"]=190000


#RedFlag de monto minimo
indicador_minimo=[]
p=0
z=0
for i in X["monto real"]:
    if i >= 190000:
        z=1
        indicador_minimo.append(z)
    else:
        z=0
        indicador_minimo.append(z)

X["indicador minimo"]=indicador_minimo


#RedFlag de indicador estandar
indicador_estandar=[]
p=0
z=0
for i in X["monto real"]:
    if i >= 346500:
        z=1
        indicador_estandar.append(z)
    else:
        z=0
        indicador_estandar.append(z)
X["indicador estandar"]=indicador_estandar


# Archivo final con RedFlags
X.to_csv('flag.csv', index=False)
