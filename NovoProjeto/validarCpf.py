#1) Função para validar CPF (salve como atividade34)
#Objetivo: Criar uma função que receba um CPF como string e valide se ele é válido conforme os dígitos verificadores.
#Desafio extra: Permitir entrada com ou sem pontuação e retornar o CPF formatado corretamente.

import re

def validar_cpf():
    while True:
        print("=" * 32)
        cpf = input("Digite seu CPF: ")

        cpflimpo = re.sub(r"[.,-]","", cpf)
        if len(cpflimpo) != 11 or not cpflimpo.isdigit():
            print('CPF inválido! Digite apenas números (com ou sem . e -) e com 11 digitos\n')
            continue


        if cpflimpo == cpflimpo[0] * len(cpflimpo):
            print('CPF inválido!, não pode ter todos os digitos iguais.\n')
            continue
        
        valido = True

        for i in range(9, 11):
            if i == 9:
                pesos = range (10, 1, -1)
            else: 
                pesos = range (11, 1, -1) 
            soma = sum(int(cpflimpo[num])* peso for num, peso in zip(range(0, i), pesos))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
                
            if digito != int(cpflimpo[i]):
                valido = False
                break
        
        if valido:
            cpf_formatado = f"{cpflimpo[:3]}.{cpflimpo[3:6]}.{cpflimpo[6:9]}-{cpflimpo[9:]}"
            return cpf_formatado
        else:
            print("CPF inválido! Digite apenas números (com ou sem . e -) e com 11 dígitos.\n")


print(f"O seu CPF foi validado: {validar_cpf()}")
    