lado1 = float(input("lado 1: "))
lado2 = float(input("lado 2: "))
lado3 = float(input("lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if (lado1 == lado2) or (lado1 == lado3):  
        print("Triangulo Equilatero")
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        print("Triangulo Isóceles")
    else: 
        print("Triangulo escaleno")
