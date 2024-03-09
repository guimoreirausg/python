dia = int(input('Quantos dias esteve com o carro: '))
km = float(input('Km rodados: '))
valorKm = float(0.15)
valorDia = 60
resul = (km * valorKm) + (dia * valorDia)

print('Valor a pagar R${:.2f}'.format(resul))
