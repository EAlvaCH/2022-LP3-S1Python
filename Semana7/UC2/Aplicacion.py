# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:43:05 2022

@author: edson
"""

import Gestion_archivos

def menu():
    print("*** MENU PRINCIPAL ***")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Contenido")
    print("4. Mostrar Contenido de Archivo")
    print("5. Salir")
    
def crear():
    print("** CREAR ARCHIVO **")
    archivo = input("Crear archivo: ")
    contenido = input("Contenido del archivo: ")
    Gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("** ELIMINAR ARCHIVO **")
    archivo = input("Quiero eliminar el archivo: ")
    Gestion_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("** AGREGAR ARCHIVO **")
    archivo = input("Quiero agregar contenido al archivo: ")
    contenido = input("El contenido adicional del archivo sera: ")
    Gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("** MOSTRAR CONTENIDO DE UN ARCHIVO **")
    archivo = input("Quiero mostrar el contenido del archivo: ")
    print(Gestion_archivos.leer_archivo(archivo))
    
def salir():
    print("** Gracias por su visita **")
    
def error():
    print("Opcion incorrecta")
    
# La lógica para el menú de opciones
opcion = 1
while opcion !=5:
    menu()
    opcion = int(input("Seleccione una opción [1-5]: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
        