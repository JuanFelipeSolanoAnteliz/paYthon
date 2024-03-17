num1 = int(input(f"Escriba el numerador: "))
num2 = int(input(f"Escriba el denominador: "))

cociente = num1 / num2
rest = num1 % num2

if rest == 0: 
    print (f"""
           la division es exacta.
           cociente = {int(cociente)}.
           resto = {rest}
           """)
else: 
    print (f"""
           la division NO es exacta.
           cociente = {int(cociente)}.
           resto = {rest}
           """)
   