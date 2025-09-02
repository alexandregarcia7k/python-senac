#Objetivo: Criar uma função que receba peso (kg) e altura (m) e retorne o Índice de Massa Corporal (IMC) com a classificação (baixo peso, normal, sobrepeso, obesidade).
#Desafio extra: Validar os dados de entrada e permitir que o usuário insira os valores como strings (ex: "70kg", "1.75m").
import re

def imc():
    while True:
        peso = input('Informe o seu Peso (Kg): ').replace(",", ".")
        altura = input('Informe a sua Altura (m): ').replace(",", ".")
        
        peso_limpo = re.sub(r"[^0-9.\-]", "", peso)
        altura_limpo = re.sub(r"[^0-9.\-]", "", altura)
        
        try:
            peso = float(peso_limpo)
            altura = float(altura_limpo)
            
            if altura > 3:
                altura = altura / 100
            
            if altura <= 0 or peso <= 0:
                print("Altura inválida, tente novamente.\n")
                continue
            
            imc_valor = peso / (altura ** 2)
            print(f"Seu IMC é: {imc_valor:.2f}")
            
            
            if imc_valor <= 18.5:
                print("Abaixo do peso")    
            elif imc_valor <= 24.9:
                print("Peso Normal")    
            elif imc_valor <= 29.9:
                print("Sobrepeso")    
            elif imc_valor <= 34.9:
                print("Obesidade I")    
            elif imc_valor <= 39.9:
                print("Obesidade II")    
            elif imc_valor >= 40:
                print("Obesidade III")  
            break
        except ValueError:
            print('Peso ou altura inválidos. Tente novamente.\n')
        
imc()