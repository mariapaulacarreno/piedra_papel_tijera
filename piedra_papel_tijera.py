# INICIO
print("--------------")
print("==BIENVENIDO==")
print("--------------")

import random

print("=== ELIGE : PIEDRA, PAPEL O TIJERA ===")

opciones = ["piedra", "papel", "tijera"]

E_u = input("Elige piedra, papel o tijera: ").lower()
E_C = random.choice(opciones)

print("La computadora eligió:", E_C)
# PROCESO
if E_u == E_C:
    print("¡Es un empate!")
elif (E_u == "piedra" and E_C == "tijera"):
    (E_u == "tijera" and E_C == "papel")
    (E_u == "papel" and E_C == "piedra")
    print("¡Ganaste!")
elif E_u in opciones:
    print("perdiste")
else:
    print("opción no válida.")


