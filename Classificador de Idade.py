idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    categoria = "Criança"
elif idade >= 13 and idade <= 17:
    categoria = "Adolescente"
elif idade >= 18 and idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print("Idade:", idade)
print("Classificação:", categoria)