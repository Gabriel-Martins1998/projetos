print("bem vindo a loja do Henrique")

valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

# calclo do valor total sem desconto
valorsemdesconto = valor * quantidade

# implementar if elif e else
if valorsemdesconto < 2500:
    desconto = 0
elif 2500 <= valorsemdesconto < 6000:
    desconto = 0.04
elif 6000 <= valorsemdesconto < 10000:
    desconto = 0.07
else:
    desconto = 0.11

valordesconto = valorsemdesconto * desconto
valorcomdesconto = valorsemdesconto - valordesconto

print(f"Valor total sem desconto: R${valorsemdesconto}")

# valores finais
if valorsemdesconto >= 2500:
    print(f"Desconto aplicado: {desconto * 100:}%")
    print(f"Valor total com desconto:{valorcomdesconto}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Valor total a pagar:{valorsemdesconto}")