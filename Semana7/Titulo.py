# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:44 2022

@author: edson
"""

# Importamos la librería

import camelcase

# Tenemos una cadena llamada nombre y se desea 
# que se muestre en formato título

nombre = "edson alcides alva chanta"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam= camelcase.CamelCase()
print("Con Camelcase...")

# Imprimimos el nombre en formato título
# Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto, incluimos los argumentos 
# 'alva' y 'chanta'

cam2=camelcase.CamelCase('alva','chanta')
print(cam2.hump(nombre))
