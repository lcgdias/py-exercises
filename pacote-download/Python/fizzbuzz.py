numero = int(input("Digite um número inteiro: "))

if ((numero%5) == 0) and ((numero%3) == 0):
	print("Fizzbuzz")
else:
	print(numero)