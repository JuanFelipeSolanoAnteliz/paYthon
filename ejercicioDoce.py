año = int(input("Ingrese un año: "))
if año < 1582:
    if año %4 == 0:
        print(f"{año} es año bisiesto.")
    else:
        print(f"{año} mo es bisiesto")

else: 
    if ((año % 4 == 0 ) and ( año % 100 != 0 )) or año % 400 == 0:
        print(f"{año} es año bisiesto.")
        
    else: print(f"{año} mo es bisiesto")
