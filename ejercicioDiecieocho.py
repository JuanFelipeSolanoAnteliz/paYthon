def determinarGanador(juegoA, juegoB):
    if abs(juegoA -juegoB) > 2 or max(juegoA, juegoB)>7:
        return "invalido"
    if min(juegoA, juegoB)< 6 or (juegoA == juegoB == 6):
        return "Aun no termina"
    if juegoB>= 6 and juegoB - juegoA >= 2:
        return "Gano B"
        # Verificar si A ganó el set
    if juegoA >= 6 and juegoB - juegoB >= 2:
        return "Gano A"
juegoA = int(input("Juegos ganados por A: "))
juegoB = int(input("Juegos ganados por B: "))

# Determinar el resultado del set e imprimirlo
resultado_set = determinarGanador(juegoA, juegoB)
print(resultado_set)