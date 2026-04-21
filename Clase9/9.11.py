# canguros.py

class Canguro:
    def __init__(self, nombre, contenido_marsupio = []):
        self.nombre = nombre
        self.contenido_marsupio = contenido_marsupio

    def __str__(self):
        return f"Canguro('{self.nombre}', {self.contenido_marsupio})"
    
    def __repr__(self):
        return f"Canguro('{self.nombre}', {self.contenido_marsupio})"
    
    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)

    

