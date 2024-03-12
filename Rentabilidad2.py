P = float(input("Ingrese el precio de suscripción: "))
U_normal = int(input("Ingrese el número de usuarios normales: "))
U_premium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese el gasto total: "))

# Cálculo Utilidad

utilidad = (P * U_normal) + (P * 1.5 * U_premium) - GT

print("La utilidad del proyecto es: ", utilidad)