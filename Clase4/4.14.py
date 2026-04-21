import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)] 

''' 
    Lo que hace convertes es:
        zipea los tipor con la fila de datos
        aplica el tipo de datos a cada valor (func(val)) <- esto me da los datos ya convertidos
'''
# IMPORTANTE: Si tengo mas de una fila, tendria que hacer .append a converted, en este caso tengo solo una fila
record = dict(zip(headers, converted))
# Luego hago un zipeo y diccionario de lo que tengo