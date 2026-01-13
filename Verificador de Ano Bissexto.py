ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    resultado = "Ano bissexto"
else:
    resultado = "Ano não bissexto"

print("Ano:", ano)
print(resultado)






