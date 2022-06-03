import os
os.system('cls')

edad = int(input("Ingrese su edad: "))

while edad < 18 or edad > 70:
    print("edad incorrecta")
    edad = int(input("ingrese edad: "))
print(f"ingreso correctamente la edad {edad}")