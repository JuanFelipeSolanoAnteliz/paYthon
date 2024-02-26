num = int(input("Ingrese el número del cual desea conocer el factorial: "))
fact = 1
for i in range(1, num+1):
    fact*=i
    print("El factorial de ",num, "es: ", fact) 
