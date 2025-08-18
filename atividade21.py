# para controle de 1 ate 7 faca

#      escreva("Digite um numero: ")
#      leia(numero)

#      soma <- soma + numero

# fimpara

# escreva("A soma de todos os numeros é:", soma)
soma = 0

for controle in range(1, 8):
    numero = float(input("Digite um número: "))
    soma += numero 

print(f"A soma de todos os números é: {soma}")