# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:31:23 2022

@author: marcos
"""

# Importo la librería random para generar números aleatorios.

import random as rm

# Función que crea una lista con 20 números aleatorios del 1 al 200.

def crearlista():
    global lista
    lista=[]
    for _ in range(20):
        lista.append(rm.randint(1,200))
       
# Llamo a la función que genera la lista.

crearlista()

# Obtengo los números pares de mi lista.

lpares=list(filter(lambda x: True if x%2==0 else False,lista))

# Obtengo los números impares de mi lista.

limpares=list(filter(lambda x: True if x%2!=0 else False,lista))