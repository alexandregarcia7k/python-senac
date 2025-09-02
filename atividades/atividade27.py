def validar_senha():

    tentativas = 3
    
    print("\n=== SISTEMA DE ACESSO ===")
    print("Critérios da senha:")
    print("- Mínimo de 8 caracteres")
    print("- Pelo menos 1 número")
    print("- Pelo menos 1 letra maiúscula")
    print("- Pelo menos 1 caractere especial (@, #, $, etc.)\n")
    
    while tentativas > 0:
        senha = input(f"Digite sua senha ({tentativas} tentativas restantes): ")
        
        if len(senha) < 8:
            print("Senha muito curta! Mínimo de 8 caracteres.")
        elif not any(c.isdigit() for c in senha):
            print("A senha deve conter pelo menos 1 número.")
        elif not any(c.isupper() for c in senha):
            print("A senha deve conter pelo menos 1 letra maiúscula.")
        elif not any(c in '@#$%&*!' for c in senha):
            print("A senha deve conter pelo menos 1 caractere especial (@, #, $, etc.)")
        else:
            print("\nAcesso concedido! Senha válida.")
            return True
        
        tentativas -= 1
        if tentativas > 0:
            print("Tente novamente.\n")
    
    print("\nAcesso bloqueado! Número máximo de tentativas excedido.")
    return False

if __name__ == "__main__":
    validar_senha()