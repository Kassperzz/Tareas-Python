from math import prod
import os
os.system('cls')

carrito=[]
cantidades=[]
precio=[]
total=0
des=0
while des != 3:
    print("\n")
    print("Bienvenido a Supermercado Duoc")
    print("1)Agregar producto")
    print("2)Ver canasta")
    print("3)Pagar")
    des=int(input("Seleccione una opcion: "))
    print("\n")

    if des == 1:
        print("PRODUCTOS")
        print("1.-Arroz    $1390")
        print("2.-Fideos   $970")
        print("3.-Salsa    $700")
        print("4.-Atun     $1120")
        print("5.-Sal      $1000")
        print("6.-Azucar   $1250")
        print("7.-Cereales $2150")
    
        pro=int(input("Elija el producto que desea añadir: "))
        
        if pro == 1:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Arroz")
            cantidades.append(cant)
            precio.append(cant*1390)
            total=cant*1390
    
        if pro == 2:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Fideos")
            cantidades.append(cant)
            precio.append(cant*970)
            total=cant*970
        
    
        if pro == 3:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Salsa")
            cantidades.append(cant)
            precio.append(cant*700)
            total=cant*700
    
        if pro == 4:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Atun")
            cantidades.append(cant)
            precio.append(cant*1120)
            total=cant*1120
        
        if pro == 5:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Sal")
            cantidades.append(cant)
            precio.append(cant*1000)
            total=cant*1000
                
        if pro == 6:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Azucar")
            cantidades.append(cant)
            precio.append(cant*1250)
            total=cant*1250
    
        if pro == 7:
            cant=int(input("Cuantos desea añadir: "))
            carrito.append("Cereales")
            cantidades.append(cant)
            precio.append(cant*2150)
            total=cant*2150
    
    
    if des == 2:
        print(carrito)
    
    if des == 3:
        print("\n")
        print("BOLETA")
        for i in range (len(carrito)):
            print(f"{carrito[i]} x{cantidades[i]} ${precio[i]}")
        print(f"TOTAL            ${total}")
        input("Presione enter para continuar")