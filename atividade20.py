for controle in range(1, 11):
    numero = float(input("Digite um número: "))

    if controle == 1:
        menor = numero 
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
print("O maior número é:", maior)
print("O menor número é:", menor)