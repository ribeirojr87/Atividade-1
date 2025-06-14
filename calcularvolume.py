#O programa deve calcular o volume e exibir o resultado em cm³.

#Solicitar os seguintes dados: Comprimento: 12cm, Largura: 14cm e Altura: 20cm.

#Utilizar string para realizar a conversão
comprimento = int(input("Digite o comprimento do objeto: "))
largura = int(input("Digite a largura do objeto: "))
altura = int(input("Digite a altura do objeto: "))

#Função para realizar o calculo em cm³.
total_volume = comprimento * largura * altura

#Exibir resultado do volume cm³
print(f"O total do volume em cm³ é: {total_volume}")
