# para controle de 1 ate 10 faca
#     escreva("Informe a idade: ")
#      leia(idade)
   
#      soma <- soma + idade
#      se (idade > 18) entao
#         cont18 <- cont18 + 1
#      senao
#           se (idade < 5) entao
#             cont5 <- cont5 + 1
#           fimse
#      fimse
#      se (idade > maior_idade) entao
#         maior_idade <- idade
#      fimse
# fimpara
# media <- soma / 10
# escreval("A média das idades é:", media)
# escreval("A quantidade de pessoas com mais de 18 anos é:", cont18)
# escreval("A quantidade de pessoas com menos de 5 anos é:", cont5)
# escreva("A maior idade é:", maior_idade)
soma = 0
cont18 = 0
cont5 = 0
maior_idade = 0

for controle in range(1, 11):
    while True:
        try:
            idade = int(input(f"Informe a idade da pessoa {controle}: "))
            if idade >= 0:
                break
            print("Idade não pode ser negativa!")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    soma += idade
    
    if idade > 18:
        cont18 += 1
    elif idade < 5:
        cont5 += 1
    
    if idade > maior_idade:
        maior_idade = idade

media = soma / 10

print("\nResultados:")
print(f"A média das idades é: {media:.1f} anos") 
print(f"Quantidade de pessoas com mais de 18 anos: {cont18}")
print(f"Quantidade de pessoas com menos de 5 anos: {cont5}")
print(f"A maior idade informada: {maior_idade} anos")