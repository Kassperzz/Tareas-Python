import os
os.system('cls')

aux = 0
hora = []

while aux != 5:
    print("1.-Solicitar Hora")
    print("2.-Cancelar Hora")
    print("3.-Mostrar Personas")
    print("4.-Ver Cantidad")
    print("5.-Salir")
    aux = int(input("Seleccione una opcion: "))
    
    if aux == 1:
        hora.append(input("Ingrese su nombre: "))
        
    if aux == 2:
        hora.remove(input("Ingrese su nombre: "))
    
    if aux == 3:
        for i in hora:
            print(i)

    if aux == 4:
        print("\n")
        print(len(hora)),print("Personas en la Lista")
        print("\n")
    
    if aux== 5:
        print("Que tenga un buen dia")
        input("Presione enter para Salir")
        