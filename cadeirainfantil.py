#Calcular o preço total da cadeira infantil

nome = "cadeira infantil"
preco_unitario = float(input("Digite o preço do produto: ")) #float = converte texto em número decimal.
quantidade = int(input("Digite a quantidade: ")) #int = converte texto em número inteiro.
total = preco_unitario * quantidade

print(f"O preço final é: R${total:.2f}")
