# -*- coding: utf-8 -*-

header = range(10)
print(f'{" ":>6s} {0:>5d} {1:>5d} {2:>5d} {3:>5d} {4:>5d} {5:>5d} {6:>5d} {7:>5d} {8:>5d} {9:>5d}')

print(f'{"------------------------------------------------------------------------":>5s}')

for i in header:
    print(f'{i:>5d}: {0*i:>5d} {1*i:>5d} {2*i:>5d} {3*i:>5d} {4*i:>5d} {5*i:>5d} {6*i:>5d} {7*i:>5d} {8*i:>5d} {9*i:>5d}')
    
#%%

print(' ',end='')
for i in range(10):
    print(f'{i:>4d}', end=' ')
print(' ')
print('-'*54)

for i in range(10):
    print(i, end=':')
    s = 0
    for j in range(10):
        print(f'{s:>4d}', end=' ')
        s += i
    print(' ')