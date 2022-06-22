# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:54:01 2022

@author: edson
"""

#Dado el total, calcular el IGV y el subtotal

import Financieros
total = 1000.49
print(f"Subtotal: {Financieros.obtenerSubTotalconTotal(total): 2f}")
print(f"IGV: {Financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")
