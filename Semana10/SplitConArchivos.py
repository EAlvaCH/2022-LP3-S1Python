# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:13:32 2022

@author: edson
"""

noticia=open("noticia.txt","rt",encoding='utf-8-sig')
datos_noticia= noticia.read()
lista =datos_noticia.split()
print(datos_noticia)
print(lista)
