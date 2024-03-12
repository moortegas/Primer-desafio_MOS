import math

radio_km = float(input("Ingrese el radio en kilometros [Kms] : "))
constante_g = float (input("Ingrese constante g [m/s2] : "))

rm = radio_km * 1000
ve = math.sqrt(2 * constante_g * rm)

print ("La velocidad de escape es {:.1f} [m/s]".format(ve))
