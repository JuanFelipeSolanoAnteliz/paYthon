num = int(input("Ingrese un numero mayor que 1: "))
a = 1
b = 0

while a <= num :
    if num % a == 0 :
        b = b + 1
        
    a = a +1
    
if b == 2:
    print("El número", num, "es primo")
else : print("el número", num, "no es primo")

