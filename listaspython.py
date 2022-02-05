# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:31:23 2022

@author: marcos
"""

# Importo la librería random para generar números aleatorios.

import random as rm

# Importo la librería functools para sumar todos los números de mi lista.

import functools as fun

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

# Guardo en una variable el número de pares que tiene mi lista.

numpares=len(lpares)

# Guardo en una variable el número de impares que tiene mi lista.

numimpares=len(limpares)

# Sumo todos los números que contiene mi lista.

sumat=fun.reduce(lambda x,y:x+y,lista)

# Multiplico por dos todos los números de mi lista.

listax2=list(map(lambda x:x*2,lista))

# Divido entre dos todos los números de la lista y redondeo a dos decimales.

listaentre2=list(map(lambda x:round(x/2,2),lista))

# Ordeno mi lista de menor a mayor.

listaordenada=sorted(lista)