class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio


    def __repr__(self):
        '''
        Devuelve una representación en string del objeto Lote
        >>> a = Lote('Naranja', 100, 490.1)
        >>> a
        Lote(Naranja, 100, 490.1)
        Sin esto, imprime <lote.Lote object at 0x00000279B7BAF4D0>
        '''
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

    def costo(self):
        return self.cajones * self.precio

    def vender(self, cajones):
        if cajones <= self.cajones:
            self.cajones -= cajones
        else:
            print("No hay suficientes cajones para vender.")


class MiLote(Lote): # Herencia + Extension de metodos
    '''
    >>> f = Milote('Fruta', 100, 490.1, 1.5)
    >>> isinstance(f, Lote)
    True
    '''
    def __init__(self, nombre, cajones, precio, factor):
        super().__init__(nombre, cajones, precio) # Llamo al constructor de la clase padre
        self.factor = factor

    def rematar(self):
        self.vender(self.cajones)

    def costo(self):
        return self.factor * super().costo() 


        
    

    


