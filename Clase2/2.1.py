
# Lee toda la data
with open('../Data/camion.csv' , 'rt') as file:
    data = file.read()

print(data)

file.close()
print("################################3 \n")
# Lee line por linea

with open('../Data/camion.csv' , 'rt') as file:
    for line in file:
        print( line , end = '')
print("################################3 \n")

file.close()
# Lee primero headers y luego file

file = open('../Data/camion.csv' , 'rt')

headers = next(file)
print(headers)
for line in file:
    print( line , end = '')
file.close()
    
print("################################3 \n")

f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)

f.close()