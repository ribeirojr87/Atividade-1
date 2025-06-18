#Calcular o preço total da cadeira infantil

nome = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço do produto: ")) 
quantidade = int(input("Digite a quantidade: ")) 
total = preco_unitario * quantidade

print(f"O preço do {nome} é: R${total:.2f}")
