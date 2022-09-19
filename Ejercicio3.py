empleados = 500
estadoCivil = ''
cargaFamiliar = 0
edadCargaFamiliar = 0

while empleados <= 500:
    nombre = input("Ingrese su nombre: ")
    estadoCivil = input("Ingrese su estado civil (casado o soltero): ")
    cargaFamiliar = int(input("Ingrese el número de cargas familiares: "))
    if cargaFamiliar >= 1:
        edadCargaFamiliar = int(
            input("Ingrese la edad de su carga familiar: "))
    empleados = empleados - 1

    if (estadoCivil == "soltero") and (cargaFamiliar == 0):
        print("Recibes $25.000")
    elif (estadoCivil == "casado") and (cargaFamiliar == 0):
        print("Recibes $30.000")
    elif ((estadoCivil == "soltero") or (estadoCivil == "casado") and (cargaFamiliar == 1)):
        print("Recibes $36.000")
    elif ((estadoCivil == "soltero") or (estadoCivil == "casado") and (cargaFamiliar == 2)):
        print("Recibes $42.000")
    elif ((estadoCivil == "soltero") or (estadoCivil == "casado") and (cargaFamiliar >= 3)):
        print("Recibes $42.000")
        if (edadCargaFamiliar > 2):
            print("Recibes $5.500 adicionales por carga excede 2 años")
