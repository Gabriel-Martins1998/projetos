
def main():
    #  Mensagem de boas-vindas
    print("Bem-vindo à copiadorado Henrique")

    # escolher serviço
    def escolha_servico():
        while True:
            servico = input("Escolha o serviço desejado (DIG/ICO/IPB/FOT): ").lower()
            if servico == 'dig':
                return 1.10
            elif servico == 'ico':
                return 1.00
            elif servico == 'ipb':
                return 0.40
            elif servico == 'fot':
                return 0.20
            else:
                # Pedido no qual o usuário errou a opção de serviço
                print("Opção de serviço inválida. Tente novamente.")

    # Função para obter o número de páginas e calcular o desconto
    def num_pagina():
        while True:
            try:
                num_pagina = int(input("Digite o número de páginas: "))
                if num_pagina >= 20000:
                    #  Pedido no qual o usuário ultrapassou o número de páginas
                    print("Não aceitamos tantas páginas de um só vez. Tente novamente.")
                elif num_pagina >= 2000:
                    return num_pagina * 0.75
                elif num_pagina >= 200:
                    return num_pagina * 0.80
                elif num_pagina >= 20:
                    return num_pagina * 0.85
                else:
                    return num_pagina
            except ValueError:
                print("Valor inválido. Por favor, digite um número inteiro.")

    # Função para escolher o serviço extra
    def servico_extra():
        while True:
            try:
                opcao = int(input("Escolha um serviço extra (1 - Encadernação Simples, 2 - Encadernação Capa Dura, 0 - Nenhum): "))
                if opcao == 1:
                    return 15
                elif opcao == 2:
                    return 40
                elif opcao == 0:
                    return 0
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Valor inválido. Por favor, digite 1, 2 ou 0.")

    # Obtenção das escolhas do usuário
    valor_servico = escolha_servico()
    num_paginas = num_pagina()
    valor_extra = servico_extra()

    # Cálculo do total a pagar
    total = (valor_servico * num_paginas) + valor_extra

    # Exibição do resultado final
    print(f"Serviço escolhido: {valor_servico:} por página")
    print(f"Número de páginas : {num_paginas:}")
    print(f"Serviço extra: R${valor_extra:}")
    print(f"Total a pagar: R${total:}")

# Execução do programa
if __name__ == "__main__":
    main()
