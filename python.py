print("¿Que moneda desea cambiar?")
print("1.-Dolares a Pesos Chilenos")
print("2.-UF a Pesos Chilenos")
print("3.-Pesos Chilenos a Dolares")
print("4.-Pesos Chilenos a UF")
print("5.-No Deseo hacer un cambio")
desicion = int(input("Seleccione la opcion"))

if desicion == 1:
    cantidad = int(input("¿Cuantos dolares desea cambiar?"))
    dolar_clp = cantidad * 846 
    print("$",dolar_clp)

if desicion == 2:
    cantidad = int(input("¿Cuantas UF desea cambiar?"))
    uf_clp = cantidad * 32095
    print("$",uf_clp)

if desicion == 3:
    cantidad = int(input("¿Cuantas Pesos desea cambiar?"))
    peso_dolar =  cantidad / 846
    print("$",peso_dolar)

if desicion == 4:
    cantidad = int(input("¿Cuantas Pesos desea cambiar?"))
    clp_uf =  cantidad / 32095
    print("$", clp_uf)

if desicion == 5:
    print("Vayase a la verga pariente :D")


