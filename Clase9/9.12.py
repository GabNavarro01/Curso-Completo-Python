import cola

class TorreDeControl:
    '''Representa a una torre de control, con operaciones de agregar un avion
    a la cola de espera y de atender al siguiente avion en la cola.'''

    def __init__(self):
        '''Crea una torre de control sin aviones esperando.'''
        self.cola_de_espera_aterrizar = cola.Cola()
        self.cola_de_espera_despegar = cola.Cola()

    def nuevo_arribo(self, avion):
        '''Agrega el avion a la cola de espera.'''
        self.cola_de_espera_aterrizar.encolar(avion)

    def nueva_partida(self,avion):
        '''Atiende al siguiente avion en la cola de espera.
        Si no hay aviones esperando, levanta ValueError.'''
        return self.cola_de_espera_despegar.encolar(avion)

    def ver_estado(self):
        print('Vuelos esperando por aterrizar:')        
        for e in self.cola_de_espera_aterrizar.leer_cola():
            print(f'  - {e}')

        print('Vuelos esperando por despegar:')
        for e in self.cola_de_espera_despegar.leer_cola():
            print(f'  - {e}')

    def asignar_pista(self):
        '''Atiende al siguiente avion en la cola de espera.
        Si no hay aviones esperando, levanta ValueError.'''
        if not self.cola_de_espera_aterrizar.esta_vacia():
            print(f'El vuelo {self.cola_de_espera_aterrizar.desencolar()} aterriza.')
        elif not self.cola_de_espera_despegar.esta_vacia():
            print(f'El vuelo {self.cola_de_espera_despegar.desencolar()} despega.')
        else:
            print('No hay aviones esperando')


