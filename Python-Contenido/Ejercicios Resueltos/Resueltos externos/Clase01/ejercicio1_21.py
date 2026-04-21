texto = 'Hoy es 6/8/2020. Mañana será 7/8/2020.'

# Encontrar las apariciones de una fecha en el texto

import re

print(re.findall(r'\d+/\d+/\d+', texto))

# Reemplazá esas apariciones, cambiando el formato
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto))
