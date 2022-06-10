from numpy import array, mat
from os import system
system('cls')

matrix = array([
    [" "*20," "*20," "*20], 
    [" "*20," "*20," "*20],
    [" "*20," "*20," "*20],
    [" "*20," "*20," "*20],
    [" "*20," "*20," "*20]
])
for fila in range (5):
    for colu in range (3):
        matrix[fila][colu] = ""
