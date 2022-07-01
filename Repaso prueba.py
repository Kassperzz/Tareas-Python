from numpy import array
from os import system
from random import randint
suma=0
pares=0
system ('cls')

mall=array([
    #0    1   2   3 c
    [" "," "," "," "], #0  f
    [" "," "," "," "], #1
    [" "," "," "," "], #2
    [" "," "," "," "]  #3
])
for fila in range(4):   #para completar la matriz con elementos aleatorios
    for colu in range(4):
        mall[fila][colu]=randint(1,5)
print(mall)
for fila in range(4):
    for colu in range(4):
        if fila==colu:
            print(mall[fila][colu])

#b
for fila in range(4):
    for colu in range(4):
        suma=suma+int(mall[fila][colu])
print(f"el proedio es: {suma/16}")        

#c
for fila in range(4):
    for colu in range(4):
        if int(mall[fila][colu])%2==1:
            pares=pares+1
print(f"cantidad de n° pares {pares}")
print(f"cantidad de n° impares {16-pares}")