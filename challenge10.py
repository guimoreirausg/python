valorDolar = float(3.27)
reais = float(input('Quantos reais possui em carteira? '))
conv = reais / valorDolar

print('a cotacao do dolar esta no valor de ${}, entao se voce possui R${}! Voce pode comprar ${:.2f}'. format(valorDolar, reais, conv))

293523