# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:35 2022

@author: edson
"""

archivo = open("Noticia.txt","at")
#\n es para agregar el contenido en una línea final
contenido="\nFuente: RPP"

archivo.write(contenido)
archivo.close()