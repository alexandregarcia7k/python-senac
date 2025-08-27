#Função que gera senha segura (salve como atividade36)
#Objetivo: Criar uma função que gere senhas aleatórias com letras, números e símbolos.
#Desafio extra: Permitir ao usuário escolher o tamanho e os tipos de caracteres.
import secrets
import string

def senha_segura():
    print('=='*32)

    maiscula = input('Deseja letras maiúsculas? (S/N) ').lower() == 's'
    minuscula = input('Deseja letras minúsculas? (S/N) ').lower() == 's'
    numeros = input('Deseja números? (S/N) ').lower() == 's'
    simbolos = input('Deseja símbolos? (S/N) ').lower() == 's'
    
    tamanho = int(input('Qual o tamanho da senha? '))

    caracteres = ''
    if maiscula:
        caracteres += string.ascii_uppercase
    if minuscula:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Você deve selecionar pelo menos um tipo de caractere!")

    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

# Chamada
senha = senha_segura()
print(f'A senha gerada é: {senha}')
