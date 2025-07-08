print('Hello, World')
print('Welcome to Python')

#podemos utilizar % e a letra do tipo s para string ou f para float ou i para inteiro e depois % e o nome das variaveis 
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 10000.98776
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (15, 15))

#sempre lembrar de salvar ou dar control s para salvar para dar run