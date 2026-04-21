# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:41:07 2021

@author: Yamila
"""


class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cantidad):
        self.cajones -= cantidad

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'


if __name__ == '__main__':
    a = Lote('Pera', 100, 490.10)
    b = Lote('Manzana', 50, 122.34)
    c = Lote('Naranja', 75, 91.75)
#     lotes = [a, b, c]
#     for c in lotes:
#          print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
    import fileparse

    with open('../Data/camion.csv') as lineas:
        camion_dicts = fileparse.parse_csv(
            lineas, select=['nombre', 'cajones', 'precio'], types=[str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio'])
              for d in camion_dicts]

    coto_total = sum([c.costo() for c in camion])
