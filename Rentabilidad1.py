P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo Utilidad

utilidad = P * U - GT

print("La utilidad del proyecto es: ", utilidad)