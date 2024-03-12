P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese el gasto total: "))
Uañoanterior = float(input("Ingrese utilidad del año anterior: "))


# Cálculo Utilidad y razón de utilidades

utilidad = P * U - GT
razon_utilidad = utilidad/Uañoanterior

print("La utilidad del proyecto es: ", utilidad)
print("Razón entre la utilidad del año y la del año anterior es: {:.2f}".format(razon_utilidad))