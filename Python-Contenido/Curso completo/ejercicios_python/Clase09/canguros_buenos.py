# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:42:35 2021

@author: Yamila
"""

class Canguro:
    def __init__(self, nombre, contenido = None):
        self.nombre = nombre
        if contenido == None:
            self.contenido_marsupio = []
        else:
            self.contenido_marsupio = contenido

    def meter_en_marsupio(self, items):
        self.contenido_marsupio.append(items)

    def __str__(self):
        objetos = [item for item in self.contenido_marsupio]
        data = f'{self.nombre} tiene en su marsupio: {", ".join(objetos)}'
        return data

# %%

# canguro_malo.py
# """Este código continene un 
# bug importante y dificil de ver
# """


# class Canguro:
#     """Un Canguro es un marsupial."""

#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         items = []
#         for i in contenido:
#             items.append(i)
#         self.contenido_marsupio = items

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [self.nombre + ' tiene en su marsupio:']
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)


# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

'''El error estaba en en el parámetro opcional que acepta el 
constructor __init__. El mismo al no ser inmutable se inicia una vez y guarda 
el valor para todo objeto que corresponda a la clase Canguto.
Se puede corregir cambiando el parámetro a inmutable (contenido = None) y luego 
definiendo cómo va a hacer self.contenido_marsupio en función si el parámetro
se ingresa con algún valor o no. Esta resolución es por la que opté en mi
código.
Para no tocar los parámetros del constructor, como solicitaba el enunciado,
lo que se puede hacer es una nueva lista a partir del parámetro para 
inicializarla nuevamente cada vez que se genera una nueva instancia de la 
clase Canguro. Esta resolución está incorporada en el código comentado.'''