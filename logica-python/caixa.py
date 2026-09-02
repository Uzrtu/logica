soma_total = 0
while True:
    valor_produto = float(input("Digite o valor do produto: "))
    soma_total += valor_produto
    print(f"Valor parcial R${soma_total}")
    continua = input("Finalizou? Pressione [f] para finalizar: ")
    if continua == "f":
        break
print(f"Total da compra = R${soma_total}")