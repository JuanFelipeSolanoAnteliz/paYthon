# edad

from time import localtime

def calcularEdad(diaAct,mesAct,añoAct,dia_n,mes_n,año_n):
  

# ladiferencia entre el año de natalidad y el año actual lo que me dara la edad en años del usuario
    edad = añoAct - año_n

#se verifica por medio de un condicional if si el mes y dia de actuales es menor que el mes y dia actual es
#lo cual determina que el cumpleaños no ha ocurrido, si se cumple la condicion e le resta uno al valor dado en edad
    
    if (mesAct, diaAct) < (mes_n, dia_n):
        edad = edad -1
    return edad

def main():
  # obtener fecha actual
    fechaAct = localtime()
    diaAct = fechaAct.tm_mday
    mesAct = fechaAct.tm_mon
    añoAct = fechaAct.tm_year

    dia_n=int(input("Ingrese el dia de su nacimiento (solo numeros. ej: 9): "))
    mes_n=int(input("Ingrese el mes de su nacimiento (solo numeros. ej: 9): "))
    año_n=int(input("Ingrese el año de su nacimiento (solo numeros. ej: 2006): "))

    edad = calcularEdad(diaAct,mesAct,añoAct,dia_n,dia_n,año_n)
    

    print(f"Usted tiene {edad} años.")

if __name__ == "__main__":
    main()


