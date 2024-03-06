salario = float(input('Valor do salario: '))
aumento = int(input('% de aumento: '))
valorAumento = ((salario / 100) * aumento)
attSalario = salario + valorAumento

print('R${:.2f} de aumento.'.format(valorAumento))
print('Valor do salario atualizado R${:.2f}!'.format(attSalario))
