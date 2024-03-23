#calculadora
import os
while True:
    os.system("cls")
    try:
        num1= float(input("ingrese el primer numero: "))
        num2= float(input("Ingres el segundo numero: "))
        while True:  # Bucle para solicitar el operador hasta que sea válido
            operador = input("Ingrese un operador (+, -, * o /): ")
            if operador in ['+', '-', '*', '/']:
                break  # Sale del bucle si el operador es válido
            else:
                print("Operador no válido. Por favor, ingrese un operador válido.")
        
        if operador == "+" :
                    suma = num1 + num2
                    print(f"""
                        
    la suma de estos dos numeros es: {suma}""")
                
                    
        elif operador == "-":
                    resta = num1 - num2
                    print(f"""
                        
    la resta de estos dos numeros es: {resta}""")
                    
        elif operador == "*":
                    multiplicacion = num1 * num2
                    print(f"""
                        
    El resultado de la multiplicacion es. {multiplicacion}""")
                
        elif operador == "/":
                    if num2 or num1 == 0:
                        raise ZeroDivisionError("No se puede dividir entre cero.")
                        division = num1 / num2
                    else:
                        division = num1/num2
                        
                    print(f"""
                        
    el resultado de la division es: {division}""")
            

        elif operador != "+" or "-" or "*" or "/":
                print("""
                        
    Opcion no valida.""")
                
                raise Exception("""
                                
    El operador indicado no es valido.""")
                
        input("""
                    
                    presione una tecla para continuar...""")
    except Exception as error:
            print(error)



    

     


