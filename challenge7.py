aluno = input('Aluno: ')
nota1 = int(input('Primeira nota do aluno: '))
nota2 = int(input('Segunda nota do aluno: '))

media = (nota1 + nota2) / 2
resultado = ''

if media >= 6:
    resultado = 'Aprovado'
else:
    resultado = 'reprovado'

print('O aluno {} possui a primeira nota {} e segunda nota {}, correspondendo a media de {}'.format(aluno, nota1, nota2, media))
print('O aluno {} esta {}!'.format(aluno, resultado))