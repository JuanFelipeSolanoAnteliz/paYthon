num = int(input("Ingrese un numero entero para saber si es par o impar: "))

par = num % 2 

if par == 0:
    print(f"{num} es par.")
else:
    print(f"{num} es impar.")
    
    