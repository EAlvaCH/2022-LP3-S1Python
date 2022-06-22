# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:48:24 2022

@author: edson
"""
archivo=open("archivo_de_prueba.txt","wt")
contenido="Línea1 hola amigos ¿Cómo están?\nLínea2 Bienvenidos a la Untels"
archivo.write(contenido)
archivo.close()

