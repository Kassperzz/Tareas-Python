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
        matrix[fila][colu] = "O"

aux = 0
while aux != 4:
    
    print("Bienvendio a Cine Duoc")
    print("1.-Ver Disponibilidad")
    print("2.-Reservar")
    print("3.-Cancelar Reserva")
    print("4.-Salir")
    aux = int(input("Seleccione una opcion: "))
    
    if aux == 1:
        print(matrix)
    
    if aux == 2:
        f = int(input("Elija una Fila: "))
        c = int(input("Elija una Columna: "))
        if matrix[fila][colu] == "X":
            print("Este Asiento esta ocupado intente nuevamente")
            print("Presione enter...")
        else:
            matrix[fila][colu] = "X"
    
    if aux == 3:
        f = int(input("Ingrese una Fila: "))
        c = int(input("Ingrese una columna: "))
        
        if matrix [fila][colu] == "O":
            print("Este Asiento no esta reservado")
            print("Presione enter...")
        else:
            matrix[fila][colu] = "O"
    
    if aux == 4:
        print("Presione enter para salir")