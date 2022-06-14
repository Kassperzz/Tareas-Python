def vNumInt(mini,maxi,texto):
    num = -1
    while num < mini or num > maxi:
        try:
            num = int(input(f"Ingrese {texto}"))
            if num < mini or num > maxi:
                print(f"Error , rango no permitido({mini}\{maxi})")
        except:
            print("Error, ingreso texto...")
    print("Ingreso correctamente ")
    return num

def vNumfloat(mini,maxi,texto):
    num = -1
    while num < mini or num > maxi:
        try:
            num = float(input(f"Ingrese {texto}"))
            if num < mini or num > maxi:
                print(f"Error , rango no permitido({mini}\{maxi})")
        except:
            print("Error, ingreso texto...")
    print("Ingreso correctamente ")
    return num

def cImc():
    peso = vNumfloat(40,300,"Peso: ")
    estatura = vNumfloat(1,2.5,"Estatura: ")
    imc = peso / (estatura*estatura)
    return imc 