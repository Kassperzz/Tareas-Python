import os
os.system('cls')

direccion = input("Ingresar Direccion: ")

while len(direccion) < 10 or len(direccion) > 25:
    print("Error al ingresar Direccion")
    direccion = input("Ingresar nombre: ")
print("Direccion adecuado")