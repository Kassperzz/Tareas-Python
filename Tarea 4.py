print("Bienvenido a La Yogueria")
desc = int(input("Usted es parte de Duoc 1.-Si/2.-No "))
print("¿Que vela Desea?")
v_1 = int(input("¿Desea Velas Aromaticas de Limon? 1.-Si/2.-No"))
v_2 = int(input("¿Desea Velas Aromaticas de Lavanda? 1.-Si/2.-No"))
v_3 = int(input("¿Desea Velas Aromaticas de Rosa? 1.-Si/2.-No"))
n_d = int(input("No deseo Velas 1.-Si/2.-No"))
 
desc_10 = 10/100
total = 0

if v_1 == 1:
    c_1 = int(input("¿Cuantas Velas de limon desea?"))
    total_F += c_1 * 3500