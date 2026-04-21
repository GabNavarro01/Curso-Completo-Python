class Rectangulo:
    def __init__(self, punto_uno, punto_dos):
        self.punto_uno = punto_uno
        self.punto_dos = punto_dos

    def base(self):
        return abs(self.punto_uno.x - self.punto_dos.x)
    
    def altura(self):
        return abs(self.punto_uno.y - self.punto_dos.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def __str__(self):
        return f'Rectangulo {self.base()}, {self.altura()}'

    def __repr__(self):
        return f'Rectangulo({self.base()}, {self.altura()})'
    
    def desplazar(self, desplazamiento):
        self.punto_uno.x += desplazamiento.x
        self.punto_uno.y += desplazamiento.y
        self.punto_dos.x += desplazamiento.x
        self.punto_dos.y += desplazamiento.y

    def rotar(self): # Sobre la esquina inferior derecha
        # Obtengo el punto interseccion esquina inferior derecha
        esquina_inferior_derecha = Punto(self.punto_dos.x, self.punto_uno.y)
        self.punto_dos = Punto(esquina_inferior_derecha.x + self.altura(), esquina_inferior_derecha.y + self.base())
        self.punto_uno = esquina_inferior_derecha

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
