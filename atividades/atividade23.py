# para controle de 1 ate 6 faca
#
#      escreva("Digite um numero:")
#      leia(numero)
#      se (numero mod 2 = 0) entao
#        par <- par + 1
#      senao
#           impar <- impar + 1
#      fimse
# fimpara
# escreval("A quantidade de numero par é:", par)
# escreva("A quantidade de numero impar é:", impar)

par = 0
impar = 0

for i in range(1, 7):  
    while True:
        try:
            numero = int(input(f"Digite o {i}º número: "))
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    if numero % 2 == 0:  
        par += 1
    else:
        impar += 1

print("\nResultado:")
print(f"→ Quantidade de números pares: {par}")
print(f"→ Quantidade de números ímpares: {impar}")