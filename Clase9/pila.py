class Pila:
    '''Representa a una pila, con operaciones de apilar y desapilar.
    El ultimo en ser apilado es tambien el ultimo en ser desapilado.
    '''

    def __init__(self):
        '''Crea una pila vacia.'''
        self.items = []

    def apilar(self, x):
        '''Apila el elemento x.'''
        self.items.append(x)

    def desapilar(self):
        '''Elimina el ultimo elemento de la pila 
        y devuelve su valor. 
        Si la pila esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La pila esta vacia')
        return self.items.pop() # El ultimo elemento, append coloca siempre detras de este

    def esta_vacia(self):
        '''Devuelve 
        True si la pila esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    def leer_pila(self):
        '''
        Devuelve una lista con los elementos de la pila,  sin modificar la pila.
        >>> elemento.cola_a_leer.leer_cola()
        [elemento1, elemento2, ...]
        '''
        return self.items[:]