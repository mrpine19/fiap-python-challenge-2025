# função para pedir usuário e senha
def solicitar_credenciais():
    print("\npasso 5: digite suas credenciais para continuar.")
    usuario = input("usuário: ")
    senha = input("senha: ")
    return usuario, senha

# função principal que simula o test drive da teleconsulta
def realizar_test_drive(): 
    print("\n==== simulação de test drive ====")
    passos = [
        "abra o aplicativo do hc saúde digital.",
        "localize e clique no botão 'acessar portal'.",
        "aparecerá a mensagem: 'deseja usar usp.br para iniciar sessão?'.",
        "clique na mensagem para iniciar sessão."
    ]

    # simula os primeiros passos com interação
    for i, passo in enumerate(passos, start=1):
        input(f"\npasso {i}: {passo}\n(pressione enter para continuar...)")

    # solicita credenciais e continua
    usuario, senha = solicitar_credenciais()
    print(f"\ncredenciais recebidas para o usuário '{usuario}'. continuando...\n")

    passos_restantes = [
        "clique no botão para acessar.",
        "aguarde o carregamento da tela inicial do aplicativo.",
        "clique no ícone no canto superior direito.",
        "no menu, selecione 'teleconsultas'.",
        "veja a lista de teleatendimentos disponíveis.",
        "clique no teleatendimento desejado.",
        "você entrará numa sala de espera virtual.",
        "aguarde o profissional da saúde entrar na sala.",
        "será aberta uma nova aba no aplicativo."
    ]

    # simula os passos finais
    for i, passo in enumerate(passos_restantes, start=6):
        input(f"\npasso {i}: {passo}\n(pressione enter para continuar...)")

    # verifica permissão de câmera e microfone
    print("\npasso 15: o aplicativo está solicitando permissão para acessar câmera e microfone.")
    resposta = input("você permite o uso da câmera e microfone? (sim/não): ").strip().lower()

    if resposta != "sim":
        print("\n atenção: sem essa permissão, a consulta não poderá ser realizada.")
        print("reinicie o test drive quando estiver pronto para permitir o acesso.\n")
        return

    input("\npasso 16: clique em 'ver webcams' para iniciar a consulta.\n(pressione enter para continuar...)")
    print("\nsimulação finalizada! você concluiu o test drive com sucesso!\n")

# função do chatbot com respostas simples
def chatbot():
    print("\n===== chatbot de suporte (simulação) =====")
    print("como posso te ajudar hoje?")
    print("1 - não consigo entrar na consulta")
    print("2 - esqueci minha senha")
    print("3 - voltar depois")

    escolha = input("digite o número da opção desejada: ")

    if escolha == "1":
        print("\n  tente fazer o test drive para simular o acesso à consulta.")
        print("caso o erro persista, contate o nosso suporte!")
    elif escolha == "2":
        print("\n para redefinir sua senha, clique no 'esqueci minha senha' em nossa tela de login.")
    elif escolha == "3":
        print("\n tudo bem! estaremos aqui quando precisar.")
    else:
        print("\n opção inválida. tente novamente.")

    print()

# menu principal que chama as funções
def menu():
    while True:
        print("==== menu principal ====")
        print("1 - realizar test drive da teleconsulta")
        print("2 - chatbot de suporte (simulação)")
        print("3 - sair")

        opcao = input("escolha uma opção: ")

        match opcao:
            case "1":
                realizar_test_drive()
            case "2":
                chatbot()
            case "3":
                print("encerrando o programa. até logo!")
                break
            case _:
                print("opção inválida. tente novamente.\n")

# início do programa
menu()