opcao = 0

while opcao != 3:
    print("\nMenu:")
    print("[1] Olá")
    print("[2] Ajuda")
    print("[3] Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("opção 1: Olá, seja bem vindo")
    elif opcao == 2:
        print("opção 2: Esta é a seção de ajuda, como posso ajudar?")
    elif opcao == 3:
        print("Saindo do programa")
    else:
        print("Opção inválida")