altura_de_caida = 100 * 3/5
rebote = 1

while rebote + 1 <= 11:
    print(rebote , altura_de_caida)
    rebote = rebote + 1
    altura_de_caida = round(altura_de_caida * 3/5, 4)