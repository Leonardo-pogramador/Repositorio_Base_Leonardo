carros = ["strada", "onix", "kwid", "gol", "palio"]
valor_aluguel = [300, 150, 50, 150, 150]

print("==================")
print("     catálogo     ")
print("==================")
print(" Carro   | Preços ")
print("         |        ")
print(" strada  |   300  ")
print(" onix    |   150  ")
print(" kwid    |   50   ")
print(" gol     |   150  ")
print(" palio   |   200  ")
print("==================")

carro = input("Qual carro será alugado??")
dias = int(input("Por quantos dias ele será alugado??"))

valor_total = valor_aluguel * dias

if carro == "strada":
    print(carro[0])
    valor_total = valor_aluguel[0] * dias
    print(valor_total)

elif carro == "onix":
    print(carro[1])
    valor_total = valor_aluguel[1] * dias
    print(valor_aluguel[1])

elif carro == "kwid":
    print(carro[2])
    valor_total = valor_aluguel[2] * dias
    print(valor_aluguel[2])

elif carro == "gol":
    print(carro[3])
    valor_total = valor_aluguel[3] * dias
    print(valor_aluguel[3])

elif carro == "palio":
    print(carro[4])
    valor_total = valor_aluguel[4] * dias
    print(valor_aluguel[4])
