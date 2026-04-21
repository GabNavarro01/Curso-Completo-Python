
#%%Ejercicio 2.7
import csv

def buscar_precio(fruta, verbose=True):
    
    
    precio=None
    
    with open('../Data/precios.csv','rt') as archivo:
        archivo_csv =csv.reader(archivo)
        
        for line in archivo_csv:      
            
                if line:
                    if line[0]==fruta:
                        precio = float(line[1])
        if verbose:
            if precio !=None:
            
                print(f'El precio de un cajón de {fruta} es: {precio}')
            else:
                print(f'{fruta} no figura en el listado de precios.')
            
       
        return precio