n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma e {}, o produto e {} e a divisao e {:.2f}'.format(s, m, d))
print('divisao inteira {} e a potencia {}'.format(di, e))