import math 

pequeño = 47
grande = 67

rho = 1.038
c = 3.7
k = 5.4 * 10 ** (-3)
tw = 100

grande = input(f"El huevo es grande? ( Si / No ): ").lower
if grande == "si":
    M = grande
    To = float(input("escriba la temperatura original en grados Celsius: "))
    t = (M**(2/3) * c * rho ** (1/3)) / (k * 3.1416 /3) ** (2/3) * (4 * 3.1416  / 3) ** (2/3) * math.log(0.76 * (To - tw) / (70 - tw))
    
else: 
    M = pequeño
    To = float(input(f"Escriba la temperatura original del huevo en grado Celsius: "))
    t = (M**(2/3) * c * rho ** (1/3)) / (k * 3.1416 /3) ** (2/3) * (4 * 3.1416  / 3) ** (2/3) * math.log(0.76 * (To - tw) / (70 - tw))
    
    print(f"El tiempo necesario para preparar el huevo a la copa es aproximadamente {t:.2f} segundos.")
    