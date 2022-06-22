# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:56:07 2022

@author: edson
"""

# Problema: Necesitamos mostrar los nombres de una cadena
# presentando las primeras letras en mayúscula
# En word se comoce como Formato Título

# Importar la librería

import camelcase

nombre="edson alcides alva chanta"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con Camelcase...")

# Imprimimos el nombre en formato titulo
# Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluimos los argumentos
# 'alva' y 'chanta'

cam2=camelcase.CamelCase('alva','chanta')
print(cam2.hump(nombre))

