x = input('Digite algo: ')
print('o tipo primitivo desse valor e: ', type(x))

print('Esse valor possui numeros e letras? ', x.isalnum())
print('somente texto? ', x.isalpha())
print('somente numero? ', x.isdigit())
print('Somente letras minusculas: ', x.islower())
print('Possui somente numeros? ', x.isnumeric())
print('LETRAS MAIUSCULAS? ', x.isupper())

