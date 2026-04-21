# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:01:27 2021

@author: Yamila
"""

class TorreDeControl:
    def __init__(self):
        self.arribos = []
        self.partidas = []
    
    def nuevo_arribo(self, arribo):
        self.arribos.append(arribo)
    
    def nueva_partida(self, partida):
        self.partidas.append(partida)
        
    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {", ".join(self.arribos)}.')
        print(f'Vuelos esperando para despegar: {", ".join(self.partidas)}.')
        
    def asignar_pista(self):
        if len(self.arribos) != 0:
            print(f'El vuelo {self.arribos[0]} aterrizó con éxito.')
            self.arribos.pop(0)
        elif len(self.arribos) == 0 and len(self.partidas) != 0:
            print(f'El vuelo {self.partidas[0]} despegó con éxito.')
            self.partidas.pop(0)
        elif len(self.arribos) == 0 and len(self.partidas) == 0:
            print('No hay vuelos en espera.')