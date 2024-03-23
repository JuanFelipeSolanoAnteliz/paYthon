def tipo_triangulo(a, b, c):
    # Verificar si el triángulo es inválido
    if a >= b + c or b >= a + c or c >= a + b:
        return "No es un triángulo válido"
    
    # Verificar si el triángulo es equilátero
    if a == b == c:
        return "El triángulo es equilátero"
    
    # Verificar si el triángulo es isósceles
    if a == b or a == c or b == c:
        return "El triángulo es isósceles"
    
    # Si no es ninguno de los anteriores, es un triángulo escaleno
    return "El triángulo es escaleno"

# Solicitar los lados del triángulo al usuario
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))