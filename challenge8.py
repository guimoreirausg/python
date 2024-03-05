# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

m = int(input('Digite a metragem: '))

cm = m * 100
mili = m * 1000

print('{}m corresponde a {} centrimetros e a {} milimetros!'.format(m, cm, mili))
