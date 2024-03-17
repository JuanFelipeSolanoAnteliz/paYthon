pal1 = input("escribe una palabra: ")
pal2 = input("escriba una segunda palabra: ")

letraP1 = len(pal1)
letrap2 = len(pal2)

if letraP1 > letrap2:
    print(f"la primera palabra es mas larga por {letraP1 - letrap2} letra (s)")
    
else: print(f"la segunda palabra es mas larga por {letraP1 - letrap2} letra (s)")