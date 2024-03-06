valorDolar = float(3.27)
reais = float(input('Quantos reais possui em carteira? '))
conv = reais / valorDolar

print('a cotacao do dolar esta no valor de ${:.2f}, entao se voce possui R${:.2f}! Voce pode comprar ${:.2f}'. format(valorDolar, reais, conv))
