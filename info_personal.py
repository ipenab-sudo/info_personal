edad = int(input("Ingrese su edad: "))
esta_graduado = input("Usted esta graduado: S/N: ")
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
if esta_graduado == "S":
    print("Y ya se graduo")
else:
    print("Y no se a graduado")