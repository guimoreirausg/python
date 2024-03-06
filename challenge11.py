largura = float(input('qual a largura da parede: '))
altura = float(input('qual a altura da parede: '))
m2 = largura * altura
pintura = m2 / 2

print('Sua parede corresponde a {:.3f}m2, voce ira gastar {:.4f}litros de tinta para pintar essa parede!'.format(m2, pintura))
