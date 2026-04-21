# -*- coding: utf-8 -*-
"""

"""

cadena = 'boligoma'
capadepenapa = ''

for c in cadena:
     capadepenapa= cadena.replace("a","apa")
     capadepenapa= capadepenapa.replace("e","epe")
     capadepenapa= capadepenapa.replace("i","ipi")
     capadepenapa= capadepenapa.replace("o","opo")
     capadepenapa= capadepenapa.replace("u","upu")

print(capadepenapa)
    
#%% Geringoso v2

cadena = 'Geringoso'
capadepenapa =''

for c in cadena:
   capadepenapa += c
   if c in "aAeEiIoOuU":
       capadepenapa += 'p' + c
       
print(capadepenapa)
        
        
        