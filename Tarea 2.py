print("¿Usted pertenece a duoc?")
desc = int(input("1.-Si/ 2.-No"))
print("¿Que libro deseraria llevar?")
l_inf = int(input("¿Desea uno infantil? 1.-Si/ 2.-No"))
l_rom = int(input("¿Desea uno de Romance? 1.-Si/ 2.-No"))
l_cien = int(input("¿Desea uno de Ciencia Ficcion? 1.-Si/ 2.-No"))
l_inv = int(input("¿Desea uno de Investigacion? 1.-Si/ 2.-No"))

total = 0
porcentaje = 40/100

if l_inf == 1:
    total += 3500

if l_rom == 1:
    total += 4500

if l_cien == 1:
    total += 6000

if l_inv == 1:
    total += 15000

if desc == 1:
    print(f"Su total a pagar es de ${total}")
    total_con_desc = total * porcentaje
    print(f"Su total a pagar con descuento es de ${total_con_desc}")

if desc != 1:
    print(f"Su total a pagar es de ${total}")
   
