"""
Elemente comune
Avand doua liste, afisati o lista a elementelor comune ambelor liste

 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Rezultat

 = [1,2,3,5,8,13]
"""
from itertools import chain
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
# Reuniune
# for item in chain(a,b):
#     if item not in c:
#         c.append(item)
for numar in a:
    if numar not in c and numar in b:
        c.append(numar)

print(c)

# Rezolvare set
print(set(a).intersection(b))

