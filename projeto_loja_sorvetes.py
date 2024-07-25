print("Bem-vindo a Loja de gelados do Henrique")

total_pedidos=0

while True:
    # SAbores
    sabor = input("Digite o sabor (CP para Cupuaçu / AC para Açaí): ").upper()
    if sabor not in ['CP', 'AC']:
        #Sabor invalido
        print("Sabor inválido. Tente novamente")
        continue
    #Tamanhos
    tamanho = input("Digite o tamanho (P, M, G): ").upper()
    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente") #sabor invalido
        continue

    # Sabor preço e sabores
    if sabor == 'CP':
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        else:  # tamanho == 'G'
            preco = 18
    elif sabor == 'AC':
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        else:  # tamanho == 'G'
            preco = 20

    total_pedidos += preco

    # Pergunta ao usuário se deseja continuar pedindo
    mais_alguma_coisa = input("Deseja pedir mais alguma coisa? (sim/não): ").lower()
    if mais_alguma_coisa != 'sim':
        break

print(f"O total do seu pedido é: R${total_pedidos:}")
print("1. Cupuaçu (CP), Tamanho P (9 reais)")
print("2. Açaí (AC), Tamanho M (16 reais)")
