# camion.py

from lote import Lote


class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def precio_total(self):
        return sum([l.costo() for l in self.lotes])

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    def costo_total(self):
        costo_total = 0
        for l in self.lotes:
            costo_total += l.costo()
        return costo_total
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, index):
        return self.lotes[index]
    
    def __repr__(self):
        return f'Camion([{", ".join(repr(l) for l in self.lotes)}])'

    def __str__(self):
        print(f'Camion con {len(self)} lotes:')
        for l in self.lotes:
            print(f'    {l.nombre} {l.cajones} cajones a ${l.precio} cada uno')
        return '' #Debe retornar un string, sino TypeError: __str__ returned non-string (type NoneType)

archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'
