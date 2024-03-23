def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)

def determinar_condicion_riesgo(edad, imc):
    if edad < 45:
        if imc < 22.0:
            return "bajo"
        else:
            return "medio"
    else:
        if imc < 22.0:
            return "medio"
        else:
            return "alto"

# Solicitar al usuario que ingrese la estatura, el peso y la edad
estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
edad = int(input("Ingrese su edad: "))

imc = calcular_imc(peso, estatura)


condicion_riesgo = determinar_condicion_riesgo(edad, imc)
print("Su condición de riesgo es:", condicion_riesgo)
