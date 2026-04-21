# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:02:02 2021

@author: Yamila
"""


class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()
    
    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self,a):
        return self.lotes[a]
    
    def __str__(self):
        string = ''
        print(f'Camion con {len(self.lotes)} lotes:')
        for lote in self.lotes:
            string += f'Lote de {lote.cajones} cajones de {lote.nombre}, pagados a ${lote.precio} cada uno.\n'
        return string
        
    def __repr__(self):
        return f'Camion({self.lotes})'