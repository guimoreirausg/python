produto = float(input('Valor do produto: '))
desconto = 5
novoPrecoProduto = produto - ((produto / 100) * 5)

print('{}% de desconto'.format(desconto))
print('Valor do produto atualizado R${:.2f}'.format(novoPrecoProduto))
