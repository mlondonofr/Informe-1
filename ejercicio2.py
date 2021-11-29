print("Aplicativo de millas-kilómetros")
print(" "*12 + "1. Millas a Km")
print(" "*12 + "2. Km a millas")
opcion = input("Elija la opción: ")
longitud = float(input("Ingrese la longitud "))

if (opcion=="1"):
    print(" "*12 + "1. Millas a Km")
    print(longitud, "millas", "son", longitud*1.61, "kilómetros")
elif (opcion=="2"):
    print(" "*12 + "2. Km a Millas")
    print(longitud, "Km", "son", round(longitud/1.61, 3 ), "millas")

