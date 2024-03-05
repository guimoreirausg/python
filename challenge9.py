# faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

num = int(input('digite um numero para saber sua tabuada: '))
i = int(0)


while i <= 10:
    multi = num * i
    # print(multi)
    print('{} x {} = {}'.format(num, i , multi))
    # print(num, 'x', i, '=', num * i)
    i += 1