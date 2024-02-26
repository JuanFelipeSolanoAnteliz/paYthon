num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escriber el segundo número: "))
num3 = int(input("escribe el tercer número: "))

if num1 > num2 and num2 > num3:
    print("El número mayor es: ", num1)
elif num2 > num3 and num3 > num1:
    print("El número mayor es: ", num2)

elif num3 > num2 and num2 > num1:
    print("El número mayor es: ", num3)

else:
    num1 == num2 == num3
    print("Los números son equivalentes.")