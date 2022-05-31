import os
os.system('cls')
edad = int(input("Ingrese su edad: "))
while edad < 14 or edad > 50:
    print("eddad en rango incorrecto")
    edad = int(input("ingrese edad: "))
print(f"ingreso correctamente la edad {edad}")

sexo = input("ingrese sexo ('f' o 'm'): ")
while sexo != 'f' or sexo != 'm':
    print("error al ingresar el sexo: ") 
    sexo = input("ingrese su sexo ('f' o 'm'): ")
print("dato ingresado correctamente")