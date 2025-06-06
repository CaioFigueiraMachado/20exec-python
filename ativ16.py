def menu():
    while True:
        print("Menu:")
        print("1 - Saque")
        print("2 - Depósito")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("Você escolheu Saque.")
        elif opcao == '2':
            print("Você escolheu Depósito.")
        elif opcao == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
    # Caio Figueira Machado